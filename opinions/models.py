from django.db import models
from djrichtextfield.models import RichTextField
from django.utils.translation import ugettext_lazy as _


class OpinionsConfiguration(models.Model):
    app_name = "Strona opinii"
    main_image = models.ImageField(upload_to='images/', verbose_name=_('Obrazek wyswietlany na gorze strony pod menu'))
    main_image_alt = models.CharField(max_length=200, verbose_name=_('Nazwa'))
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)
    tree_img = models.ImageField(upload_to='images/', verbose_name=_('Obrazek wyswietlany jako glowny w drzewku'))

    def __str__(self):
        return self.app_name + " konfiguracja"

    class Meta:
        verbose_name = _('Konfiguracja opinii')
        verbose_name_plural = _('Konfiguracja opinii')


class OpinionItem(models.Model):
    opinion_text = RichTextField(verbose_name=_('Tekst rekomendacji'))
    customer_name = models.CharField(max_length=400, verbose_name=_('Imie osoby polecajacej'))
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)
    element_order = models.IntegerField(default=0, verbose_name=_('Kolejnosc'))

    def __str__(self):
        return self.customer_name + "(" + self.element_order + ")"

    class Meta:
        verbose_name = _('Opinia')
        verbose_name_plural = _('Opinie')


class OpinionTreeItem(models.Model):
    text = RichTextField(verbose_name=_('Tekst wyswietlany w drzewku na podstronie opinii'))
    img = models.ImageField(upload_to='images/', verbose_name=_('Ilustracja wyswietlana w drzewku na podstronie opinii'))
    element_order = models.IntegerField(default=0, verbose_name=_('Kolejnosc'))

    def __str__(self):
        return self.text + "(" + self.element_order + ")"

    class Meta:
        verbose_name = _('Element drzewka na stronie opinii')
        verbose_name_plural = _('Elementy drzewka na stronie opinie')

