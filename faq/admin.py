from django.contrib import admin

from .models import FaqItem, FaqConfiguration


@admin.register(FaqItem)
class FaqItemAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(FaqConfiguration)
class FaqConfigurationAdmin(admin.ModelAdmin):
    save_as = True