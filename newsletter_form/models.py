from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _


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
