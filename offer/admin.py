from django.contrib import admin
from .models import OfferItem


@admin.register(OfferItem)
class OfferItemAdmin(admin.ModelAdmin):
    save_as = True

