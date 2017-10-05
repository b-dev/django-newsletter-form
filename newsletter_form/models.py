# coding=utf-8
import logging
from django.core.mail import EmailMessage
from django.contrib.sites.models import Site
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse
from django.template.loader import render_to_string
from mailchimp3 import MailChimp

from newsletter_form import settings as newsletter_settings

log = logging.getLogger('newsletter')


class EmailAddress(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    key = models.CharField(max_length=40, blank=True, null=True)

    set_at = models.DateTimeField(
        default=timezone.now,
        help_text=_('When the confirmation key expiration was set'),
    )
    confirmed_at = models.DateTimeField(
        blank=True, null=True,
        help_text=_('First time this email was confirmed'),
    )
    external_recipient_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Email Addresses"

    def __unicode__(self):
        return '{}'.format(self.email)

    @staticmethod
    def subscribe(email):
        email_address, created = EmailAddress.objects.get_or_create(email=email)

        if not created:
            if email_address.is_confirmed:
                return False, newsletter_settings.NEWSLETTER_FORM_ALREADY_SUBSCRIBE_MESSAGE

        client = MailChimp(newsletter_settings.NEWSLETTER_FORM_MAILCHIMP_USERNAME,
                           newsletter_settings.NEWSLETTER_FORM_MAILCHIMP_API_KEY)

        try:
            response = client.lists.members.create(newsletter_settings.NEWSLETTER_FORM_MAILCHIMP_LIST_ID, {
                'email_address': email_address.email,
                'status': 'subscribed'
            })
        except Exception, e:
            log.error(u"[SubscribeUserView] Errore durate la chiamata a Mailchimp. Errore: %s" % str(e))
            return False, newsletter_settings.NEWSLETTER_FORM_ERROR_MESSAGE

        log.debug(u"[SubscribeUserView] Chiamata a mailchimp inviata correttamente. Response: %s" % str(response))
        if response['status'] == 'subscribed':
            email_address.mailchimp_recipient_id = response['id']
            email_address.confirmed_at = timezone.now()
            email_address.save()

            site = Site.objects.get_current()
            tname = 'newsletter_form/emails/iscrizione_confermata.html'
            confirmation_email = render_to_string(tname, {'site': site})

            mail_subject = _(newsletter_settings.NEWSLETTER_FORM_MAIL_SUBJECT_ISCRIZIONE_CONFERMATA)

            msg = EmailMessage(subject=mail_subject, body=confirmation_email, to=[email_address.email])
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
            return True, response
        else:
            return False, newsletter_settings.NEWSLETTER_FORM_ERROR_MESSAGE

    @property
    def is_confirmed(self):
        return self.confirmed_at is not None

    @property
    def key_expires_at(self):
        # By default, keys don't expire. If you want them to, set
        # settings.SIMPLE_EMAIL_CONFIRMATION_PERIOD to a timedelta.
        period = getattr(
            settings, 'NEWSLETTER_FORM_EMAIL_CONFIRMATION_PERIOD', None
        )
        return self.set_at + period if period is not None else None

    @property
    def is_key_expired(self):
        return self.key_expires_at and timezone.now() >= self.key_expires_at

    def reset_confirmation(self):
        """
        Re-generate the confirmation key and key expiration associated
        with this email.  Note that the previou confirmation key will
        cease to work.
        """
        self.key = get_random_string()
        self.set_at = timezone.now()

        self.confirmed_at = None
        self.save(update_fields=['key', 'set_at', 'confirmed_at'])
        return self.key
