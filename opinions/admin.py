from django.contrib import admin
from .models import OpinionsConfiguration, OpinionItem


@admin.register(OpinionsConfiguration)
class OpinionsConfigurationAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(OpinionItem)
class OpinionItemAdmin(admin.ModelAdmin):
    save_as = True

