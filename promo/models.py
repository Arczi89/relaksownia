from django.db import models
from djrichtextfield.models import RichTextField
from django.utils.translation import ugettext_lazy as _


class PromoItem(models.Model):
    photo = models.ImageField(upload_to='images/', verbose_name=_('Glowny obrazek'))
    photo_alt = models.CharField(max_length=200, verbose_name=_('Nazwa'))
    photo_responsive1 = models.ImageField(upload_to='images/', verbose_name=_('Kawalek 1 - do wersji responsywnej'))
    photo_responsive1_alt = models.CharField(max_length=200, verbose_name=_('Nazwa 1'))
    photo_responsive2 = models.ImageField(upload_to='images/', verbose_name=_('Kawalek 2 - do wersji responsywnej'))
    photo_responsive2_alt = models.CharField(max_length=200, verbose_name=_('Nazwa 2'))
    photo_responsive3 = models.ImageField(upload_to='images/', verbose_name=_('Kawalek 3 - do wersji responsywnej'), blank=True)
    photo_responsive3_alt = models.CharField(max_length=200, verbose_name=_('Nazwa 3'), blank=True)
    photo_responsive4 = models.ImageField(upload_to='images/', verbose_name=_('Kawalek 4 - do wersji responsywnej'), blank=True)
    photo_responsive4_alt = models.CharField(max_length=200, verbose_name=_('Nazwa 4'), blank=True)
    text = RichTextField(verbose_name=_('Tekst'), blank=True)
    text_position = models.IntegerField(default=1, verbose_name="Pozycja tekstu, jeśli jest jakiś ustawiony 1 - przed obrazkami, 2+ po obrazkach")
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)
    element_order = models.IntegerField(default=0, verbose_name=_('Kolejnosc'))

    def __str__(self):
        return '%s ( %i )' % (self.photo_alt, self.element_order)

    class Meta:
        verbose_name = _('Element strony promocji')
        verbose_name_plural = _('Elementy strony promocji')
