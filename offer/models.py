from django.db import models
from djrichtextfield.models import RichTextField
from django.utils.translation import ugettext_lazy as _


class OfferItem(models.Model):
    title = models.TextField(verbose_name=_('Tytul'))
    text = RichTextField(verbose_name=_('Tresc'))
    image = models.ImageField(upload_to='images/', verbose_name=_('Obrazek'))
    image_alt = models.TextField(verbose_name=_('Nazwa'))
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)
    order = models.IntegerField(default=0, verbose_name=_('Kolejnosc'))

    def __str__(self):
        return self.title + "(" + self.order .__str__() + ")"

    class Meta:
        verbose_name = _('Oferta')
        verbose_name_plural = _('Lista ofert')

