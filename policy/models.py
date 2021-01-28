from django.db import models
from django.utils.translation import ugettext_lazy as _
from djrichtextfield.models import RichTextField


class PolicyConfiguration(models.Model):
    app_name = "Polityka"
    privacy_text = RichTextField(verbose_name=_('Tekst polityki prywatnosci'), blank=True)
    order_rules = RichTextField(verbose_name=_('Tekst zasad zamowien'), blank=True)
    update_date = models.DateTimeField(verbose_name=_('Data ostatniej modyfikacji'), auto_now=True)

    def __str__(self):
        return self.app_name + " konfiguracja"

    class Meta:
        verbose_name = _('Konfiguracja polityk')
        verbose_name_plural = _('Konfiguracja polityk')
