# coding=utf-8
import logging
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.http import JsonResponse
from django.views.generic import View

from newsletter_form import settings as newsletter_settings
from newsletter_form.models import EmailAddress


log = logging.getLogger('newsletter')


class SubscribeUserView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email_newsletter', '')
        flag_terms_of_use = request.POST.get('flag_terms_of_use', '')
        first_name = None
        last_name = None
        if newsletter_settings.NEWSLETTER_FORM_MANAGE_FIRST_NAME:
            first_name = request.POST.get('first_name', '')
        if newsletter_settings.NEWSLETTER_FORM_MANAGE_LAST_NAME:
            last_name = request.POST.get('last_name', '')

        if not email:
            log.debug(u"[SubscribeUserView] Errore: %s" % newsletter_settings.NEWSLETTER_FORM_INVALID_EMAIL_MESSAGE)
            return JsonResponse({'results': 'ko', 'message': newsletter_settings.NEWSLETTER_FORM_INVALID_EMAIL_MESSAGE})

        if not flag_terms_of_use:
            log.debug(u"[SubscribeUserView] Errore: Flag terms of use not checked" % newsletter_settings.NEWSLETTER_FORM_INVALID_TERMS_OF_USE_MESSAGE)
            return JsonResponse({'results': 'ko', 'message': newsletter_settings.NEWSLETTER_FORM_INVALID_TERMS_OF_USE_MESSAGE})

        validate_email = EmailValidator(newsletter_settings.NEWSLETTER_FORM_INVALID_EMAIL_MESSAGE, 'invalid')

        try:
           validate_email(email)
        except ValidationError:
            log.debug(u"[SubscribeUserView] ValidationError: %s" % newsletter_settings.NEWSLETTER_FORM_INVALID_EMAIL_MESSAGE)
            return JsonResponse({'results': 'ko', 'message': newsletter_settings.NEWSLETTER_FORM_INVALID_EMAIL_MESSAGE})

        success, error_message = EmailAddress.subscribe(email, first_name=first_name, last_name=last_name)

        if not success:
            log.debug(u"[SubscribeUserView] subscribe_email -> success = False. Errore: %s" % error_message)
            return JsonResponse({'results': 'ko', 'message': error_message})

        response = JsonResponse({'results': 'ok',
                                 'message': newsletter_settings.NEWSLETTER_FORM_CONFIRM_SUBSCRIBE_MESSAGE})
        return response
