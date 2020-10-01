from django.contrib import admin
from .models import OfferItem, OfferConfiguration


@admin.register(OfferItem)
class OfferItemAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(OfferConfiguration)
class OfferConfigurationAdmin(admin.ModelAdmin):
    save_as = True

