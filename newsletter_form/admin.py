from django.contrib import admin
from newsletter_form.models import EmailAddress


class EmailAddressAdmin(admin.ModelAdmin):
    list_display = ('email', 'external_recipient_id')
admin.site.register(EmailAddress, EmailAddressAdmin)
