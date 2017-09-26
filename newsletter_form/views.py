# coding=utf-8
import logging

from django.utils import timezone
from mailchimp3 import MailChimp

from django.core.mail import EmailMessage
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import View
from django.utils.translation import ugettext as _

from newsletter_form import settings as newsletter_settings
from newsletter_form.models import EmailAddress


log = logging.getLogger('newsletter')


class SubscribeUserView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email_newsletter', '')

        if not email:
            return JsonResponse({'results': 'ko', 'message': newsletter_settings.NEWSLETTER_FORM_INVALID_EMAIL_MESSAGE})

        validate_email = EmailValidator(newsletter_settings.NEWSLETTER_FORM_INVLID_EMAIL_MESSAGE, 'invalid')

        try:
           validate_email(email)
        except ValidationError:
            return JsonResponse({'results': 'ko', 'message': newsletter_settings.NEWSLETTER_FORM_INVALID_EMAIL_MESSAGE})

        ea, created = EmailAddress.objects.get_or_create(email=email)

        if not created:
            if ea.is_confirmed:
                return JsonResponse(
                    {'results': 'ko', 'message': newsletter_settings.NEWSLETTER_FORM_ALREADY_SUBSCRIBE_MESSAGE})

        success, error_message = self.subscribe_email(request, ea)

        if not success:
            return JsonResponse({'results': 'ko', 'message': error_message})

        response = JsonResponse({'results': 'ok',
                                 'message': newsletter_settings.NEWSLETTER_FORM_CONFIRM_SUBSCRIBE_MESSAGE})
        return response

    def subscribe_email(self, request, email_address):
        client = MailChimp(newsletter_settings.NEWSLETTER_FORM_MAILCHIMP_USERNAME,
                           newsletter_settings.NEWSLETTER_FORM_MAILCHIMP_API_KEY)

        try:
            response = client.lists.members.create(newsletter_settings.NEWSLETTER_FORM_MAILCHIMP_LIST_ID, {
                'email_address': email_address.email,
                'status': 'subscribed'
            })
        except Exception, e:
            return False, newsletter_settings.NEWSLETTER_FORM_ERROR_MESSAGE

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
