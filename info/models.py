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
