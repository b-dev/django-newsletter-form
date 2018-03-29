from django import template
from newsletter_form import settings as newsletter_settings


register = template.Library()


@register.inclusion_tag('newsletter_form/form_iscrizione_newsletter.html')
def newsletter_form():
    return {
        'text_newsletter_button_disabled': newsletter_settings.NEWSLETTER_FORM_BUTTON_SUBSCRIBE_TEXT_SENDING,
        'text_newsletter_button_enabled': newsletter_settings.NEWSLETTER_FORM_BUTTON_SUBSCRIBE_TEXT,
        'title_modal_error_dialog': newsletter_settings.NEWSLETTER_FORM_TITLE_MODAL_ERROR_DIALOG,
        'title_modal_success_dialog': newsletter_settings.NEWSLETTER_FORM_TITLE_MODAL_SUCCESS_DIALOG,
        'manage_first_name': newsletter_settings.NEWSLETTER_FORM_MANAGE_FIRST_NAME,
        'manage_last_name': newsletter_settings.NEWSLETTER_FORM_MANAGE_LAST_NAME,
        'first_name_mandatory': newsletter_settings.NEWSLETTER_FORM_FIRST_NAME_MANDATORY,
        'last_name_mandatory': newsletter_settings.NEWSLETTER_FORM_LAST_NAME_MANDATORY,
    }
