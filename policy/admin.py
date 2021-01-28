from django.contrib import admin

from .models import PolicyConfiguration


@admin.register(PolicyConfiguration)
class PolicyConfigurationAdmin(admin.ModelAdmin):
    save_as = True
