======================
Django Newsletter Form
======================

Integrate a simple newsletter form to subscribe users to Mailchimp.

Quick start
-----------

1. Add "newsletter_form" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'newsletter_form',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^newsletter/', include('newsletter_form.urls')),

3. Run `python manage.py migrate` to create the newsletter form models.

4. Set the Mailchimp data::

    NEWSLETTER_FORM_MAILCHIMP_USERNAME = ''
    NEWSLETTER_FORM_MAILCHIMP_API_KEY = ''
    NEWSLETTER_FORM_MAILCHIMP_LIST_ID = ''

5. Include the css and js in your base template::

    <link href="{% static "newsletter_form/css/newsletter_form.css" %}" rel="stylesheet">

    {# Must be included after jQuery script #}
    <script src="{% static "newsletter_form/js/newsletter_form.js" %}"></script>

6. Load the newsletter_form tag and include the form tag::

    {% load newsletter_form_tags %}
    {% newsletter_form %}

7. Optionally. Customize the messages::

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
