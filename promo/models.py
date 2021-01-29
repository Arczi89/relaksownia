from django.db import models
from djrichtextfield.models import RichTextField
from django.utils.translation import ugettext_lazy as _


class PromoItem(models.Model):
    photo = models.ImageField(upload_to='images/', verbose_name=_('Glowny obrazek'))
    photo_alt = models.CharField(max_length=200, verbose_name=_('Nazwa'))
    photo_responsive1 = models.ImageField(upload_to='images/', verbose_name=_('Czesc pierwsza obrazka - do wersji responsywnej'))
    photo_responsive1_alt = models.CharField(max_length=200, verbose_name=_('Nazwa p1'))
    photo_responsive2 = models.ImageField(upload_to='images/', verbose_name=_('Czesc druga obrazka - do wersji responsywnej'))
    photo_responsive2_alt = models.CharField(max_length=200, verbose_name=_('Nazwa p2'))
    text = RichTextField(verbose_name=_('Tekst'), blank=True)
    text_position = models.IntegerField(default=1, verbose_name="Pozycja tekstu, jeśli jest jakiś ustawiony (1 - przed obrazkiem, 2 - po pierwszym obrazku, 3 - po drugim obrazku")
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)
    element_order = models.IntegerField(default=0, verbose_name=_('Kolejnosc'))

    def __str__(self):
        return "element strony promocji"

    class Meta:
        verbose_name = _('Element strony promocji')
        verbose_name_plural = _('Elementy strony promocji')
