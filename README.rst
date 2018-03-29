======================
Django Newsletter Form
======================

Integrate a simple newsletter form to subscribe users to Mailchimp.

Quick start
-----------
0. Install the package::

    pip install django-newsletter-form

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

7. Options you can customize::

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
