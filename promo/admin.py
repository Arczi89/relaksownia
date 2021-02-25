from django.contrib import admin

from .models import PromoPageComponent


@admin.register(PromoPageComponent)
class PromoItemAdmin(admin.ModelAdmin):
    save_as = True
