# coding=utf-8
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


NEWSLETTER_FORM_BUTTON_SUBSCRIBE_TEXT_SENDING = getattr(settings, 'NEWSLETTER_FORM_BUTTON_SUBSCRIBE_TEXT_SENDING',
                                                        _("Invio..."))

NEWSLETTER_FORM_BUTTON_SUBSCRIBE_TEXT = getattr(settings, 'NEWSLETTER_FORM_BUTTON_SUBSCRIBE_TEXT',
                                                _("ISCRIVITI"))

NEWSLETTER_FORM_TITLE_MODAL_ERROR_DIALOG = getattr(settings, 'NEWSLETTER_FORM_TITLE_MODAL_ERROR_DIALOG',
                                                   _("Iscrizione non riuscita"))

NEWSLETTER_FORM_TITLE_MODAL_SUCCESS_DIALOG = getattr(settings, 'NEWSLETTER_FORM_TITLE_MODAL_SUCCESS_DIALOG',
                                                     _("Iscrizione avvenuta con successo"))

NEWSLETTER_FORM_MAIL_SUBJECT_ISCRIZIONE_CONFERMATA = _("Iscrizione confermata")

NEWSLETTER_FORM_INVALID_EMAIL_MESSAGE = _(u"Inserire un indirizzo email valido")
NEWSLETTER_FORM_ALREADY_SUBSCRIBE_MESSAGE = _(u"Sei già iscritto alla nostra newsletter")
NEWSLETTER_FORM_CONFIRM_SUBSCRIBE_MESSAGE = _(u"ISCRIZIONE CONFERMATA CON SUCCESSO")
NEWSLETTER_FORM_ERROR_MESSAGE = _(u"Errore durante l'iscrizione alla newsletter. L'amministratore è già stato avvisato.")

NEWSLETTER_FORM_CONFIRM_EMAIL = False
NEWSLETTER_FORM_MAILCHIMP_USERNAME = ''
NEWSLETTER_FORM_MAILCHIMP_API_KEY = ''
NEWSLETTER_FORM_MAILCHIMP_LIST_ID = ''
