# django-newsletter-form

Simple Django newsletter form for Mailchimp

Follow this step to integrate the form:

- Inserire 'newsletter_form' nelle INSTALLED_APPS

- Aggiungere negli urls.py:

    url(r'^newsletter/', include('newsletter_form.urls')),

- Aggiungere nel template dove si vuole visualizzare il form per l'iscrizione:
    {% load newsletter_form_tags %}

    {% newsletter_form %}

- Impostare i dati di collegamento con Mailchimp:

NEWSLETTER_FORM_MAILCHIMP_USERNAME = ''
NEWSLETTER_FORM_MAILCHIMP_API_KEY = ''
NEWSLETTER_FORM_MAILCHIMP_LIST_ID = ''

- OPZIONALE: personalizzare i vari messaggi visualizzati (di seguito i default):

NEWSLETTER_FORM_BUTTON_SUBSCRIBE_TEXT_SENDING = "Invio..."
NEWSLETTER_FORM_BUTTON_SUBSCRIBE_TEXT = "ISCRIVITI"
NEWSLETTER_FORM_TITLE_MODAL_ERROR_DIALOG = "Iscrizione non riuscita"
NEWSLETTER_FORM_TITLE_MODAL_SUCCESS_DIALOG = "Iscrizione avvenuta con successo"
NEWSLETTER_FORM_MAIL_SUBJECT_ISCRIZIONE_CONFERMATA = "Iscrizione confermata"
NEWSLETTER_FORM_INVALID_EMAIL_MESSAGE = "Inserire un indirizzo email valido"
NEWSLETTER_FORM_ALREADY_SUBSCRIBE_MESSAGE = "Sei già iscritto alla nostra newsletter"
NEWSLETTER_FORM_CONFIRM_SUBSCRIBE_MESSAGE = "ISCRIZIONE CONFERMATA CON SUCCESSO"
NEWSLETTER_FORM_ERROR_MESSAGE = "Errore durante l'iscrizione alla newsletter. L'amministratore è già stato avvisato.
NEWSLETTER_FORM_CONFIRM_EMAIL = False
