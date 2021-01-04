from django.db import models
from djrichtextfield.models import RichTextField
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


class BlogConfiguration(models.Model):
    app_name = "Blog"
    main_image = models.ImageField(upload_to='images/', verbose_name=_('Glowny obrazek'))
    main_image_alt = models.CharField(max_length=200, verbose_name=_('Nazwa'))
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)

    def __str__(self):
        return self.app_name + " konfiguracja"

    class Meta:
        verbose_name = _('Konfiguracja bloga')
        verbose_name_plural = _('Konfiguracja bloga')


class BlogPost(models.Model):
    photo = models.ImageField(upload_to='images/', verbose_name=_('Glowny obrazek'))
    photo_alt = models.CharField(max_length=200, verbose_name=_('Nazwa'))
    description = RichTextField(verbose_name=_('Glowny tekst posta'))
    publication_date = models.DateTimeField(auto_now=True, verbose_name=_('Data publikacji posta'))
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)
    element_order = models.IntegerField(default=0, verbose_name=_('Kolejnosc'))

    def __str__(self):
        return "Post"

    class Meta:
        verbose_name = _('Post na bloga')
        verbose_name_plural = _('Posty na bloga')
