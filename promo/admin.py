from django.contrib import admin

from .models import PromoItem


@admin.register(PromoItem)
class PromoItemAdmin(admin.ModelAdmin):
    save_as = True
