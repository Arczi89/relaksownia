from django.contrib import admin

from .models import MainConfiguration, MainSliderConfiguration, MainSliderItem, MainBoxItem


@admin.register(MainConfiguration)
class MainConfigurationAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(MainSliderConfiguration)
class MainSliderConfigurationAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(MainSliderItem)
class MainSliderItemAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(MainBoxItem)
class MainBoxItemAdmin(admin.ModelAdmin):
    save_as = True
