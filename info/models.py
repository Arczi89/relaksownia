from django.db import models
from djrichtextfield.models import RichTextField
from django.utils.translation import ugettext_lazy as _


class Info(models.Model):
    photo = models.ImageField(upload_to='images/', verbose_name=_('Twoje glowne zdjecie'))
    photo_alt = models.CharField(max_length=200, verbose_name=_('Alternatywny tekst przy braku zdjecia'))
    description = RichTextField(verbose_name=_('Opis'))
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)

    def __str__(self):
        return "Informacje o Tobie"

    class Meta:
        verbose_name = _('Informacja o Tobie')
        verbose_name_plural = _('Informacja o Tobie')


class CertItem(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name=_('Zdjecie certyfikatu'))
    image_alt = models.CharField(max_length=100, verbose_name=_('Nazwa certyfikatu'))
    element_order = models.IntegerField(default=0, verbose_name=_('Kolejnosc'))

    def __str__(self):
        return '%s ( %i )' % (self.image_alt, self.element_order)

    class Meta:
        verbose_name = _('Certyfikat')
        verbose_name_plural = _('Certyfikaty')