from django.contrib import admin

from .models import FaqItem


@admin.register(FaqItem)
class FaqItemAdmin(admin.ModelAdmin):
    save_as = True
