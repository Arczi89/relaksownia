from django.contrib import admin

from .models import PromoPageComponent, PromoConfiguration, PromoClient


@admin.register(PromoPageComponent)
class PromoItemAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(PromoConfiguration)
class PromoItemAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(PromoClient)
class PromoItemAdmin(admin.ModelAdmin):
    save = False
    save_as = False
