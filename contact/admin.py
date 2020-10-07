from django.contrib import admin

from .models import Contact, ContactConfiguration


@admin.register(ContactConfiguration)
class ContactConfigurationAdmin(admin.ModelAdmin):
    save_as = True

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    save_as = True