from django.contrib import admin

from .models import Info, CertItem


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(CertItem)
class CertItemAdmin(admin.ModelAdmin):
    save_as = True