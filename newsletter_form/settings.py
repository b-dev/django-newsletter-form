# coding=utf-8
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

NEWSLETTER_FORM_SEND_WELCOME_MAIL = getattr(settings, 'NEWSLETTER_FORM_SEND_WELCOME_MAIL', False)

NEWSLETTER_FORM_BUTTON_SUBSCRIBE_TEXT_SENDING = getattr(settings, 'NEWSLETTER_FORM_BUTTON_SUBSCRIBE_TEXT_SENDING',
                                                        _("Send..."))

NEWSLETTER_FORM_BUTTON_SUBSCRIBE_TEXT = getattr(settings, 'NEWSLETTER_FORM_BUTTON_SUBSCRIBE_TEXT',
                                                _("SUBSCRIBE"))

NEWSLETTER_FORM_TITLE_MODAL_ERROR_DIALOG = getattr(settings, 'NEWSLETTER_FORM_TITLE_MODAL_ERROR_DIALOG',
                                                   _("Subscription failed"))
NEWSLETTER_FORM_ERROR_MESSAGE = getattr(settings, 'NEWSLETTER_FORM_ERROR_MESSAGE',
                                        _(u"Error during the subscription process. Administrator are already informed"))

NEWSLETTER_FORM_TITLE_MODAL_SUCCESS_DIALOG = getattr(settings, 'NEWSLETTER_FORM_TITLE_MODAL_SUCCESS_DIALOG',
                                                     _("Subscription confirmed"))
NEWSLETTER_FORM_CONFIRM_SUBSCRIBE_MESSAGE = getattr(settings, 'NEWSLETTER_FORM_CONFIRM_SUBSCRIBE_MESSAGE',
                                                    _(u"Great! From now you'll receive our newsletter!"))

NEWSLETTER_FORM_MAIL_SUBJECT_ISCRIZIONE_CONFERMATA = getattr(settings, 'NEWSLETTER_FORM_MAIL_SUBJECT_ISCRIZIONE_CONFERMATA',
                                                             _("Subscription to our newsletter confirmed!"))

NEWSLETTER_FORM_INVALID_EMAIL_MESSAGE = getattr(settings, 'NEWSLETTER_FORM_INVALID_EMAIL_MESSAGE',
                                                _(u"Insert a valid email address"))
NEWSLETTER_FORM_ALREADY_SUBSCRIBE_MESSAGE = getattr(settings, 'NEWSLETTER_FORM_ALREADY_SUBSCRIBE_MESSAGE',
                                                    _(u"You're already subscribed to our newsletter"))

NEWSLETTER_FORM_MAILCHIMP_USERNAME = getattr(settings, 'NEWSLETTER_FORM_MAILCHIMP_USERNAME', '')
NEWSLETTER_FORM_MAILCHIMP_API_KEY = getattr(settings, 'NEWSLETTER_FORM_MAILCHIMP_API_KEY', '')
NEWSLETTER_FORM_MAILCHIMP_LIST_ID = getattr(settings, 'NEWSLETTER_FORM_MAILCHIMP_LIST_ID', '')

NEWSLETTER_FORM_MANAGE_FIRST_NAME = getattr(settings, 'NEWSLETTER_FORM_MANAGE_FIRST_NAME', False)
NEWSLETTER_FORM_MANAGE_LAST_NAME = getattr(settings, 'NEWSLETTER_FORM_MANAGE_LAST_NAME', False)

# MANAGED ONLY IF NEWSLETTER_FORM_MANAGE_FIRST_NAME = True
NEWSLETTER_FORM_FIRST_NAME_MANDATORY = getattr(settings, 'NEWSLETTER_FORM_FIRST_NAME_MANDATORY', True)

# MANAGED ONLY IF NEWSLETTER_FORM_MANAGE_LAST_NAME = True
NEWSLETTER_FORM_LAST_NAME_MANDATORY = getattr(settings, 'NEWSLETTER_FORM_LAST_NAME_MANDATORY', True)
