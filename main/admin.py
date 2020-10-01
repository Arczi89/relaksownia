from django.contrib import admin

from .models import SliderItem, ContainerItem, Info


@admin.register(SliderItem)
class SliderItemAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(ContainerItem)
class ContainerItemAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    save_as = True
