from django.db import models
from djrichtextfield.models import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _

from demosite.constants import newsletter_permission_text_default


class MainConfiguration(models.Model):
    app_name = "Strona glowna"
    is_modal_visible = models.BooleanField(default=False, verbose_name=_('Czy dialog newsletter ma sie wyswietlac?'))
    newsletter_info = RichTextField(verbose_name=_('Naglowek newslettera'))
    main_text = RichTextField(verbose_name=_('Tekst w newsletterze'))
    permission_text = models.TextField(verbose_name=_('Tresc zgody klienta na przesylanie newslettera'), default=newsletter_permission_text_default, blank=False)
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)

    def __str__(self):
        return self.app_name + " konfiguracja"

    class Meta:
        verbose_name = _('Konfiguracja strony glownej i newslettera')
        verbose_name_plural = _('Konfiguracja strony glownej i newslettera')


class MainSliderConfiguration(models.Model):
    change_image_time_ms = models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(10000)], verbose_name=_('Czas po ktorym zmieni sie obrazek w sliderze'))
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)

    def __str__(self):
        return "Konfiguracja slidera na stronie glownej"

    class Meta:
        verbose_name = _('Konfiguracja slidera na stronie glownej')
        verbose_name_plural = _('Konfiguracja slidera na stronie glownej')


class MainSliderItem(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name=_('Obrazek'))
    image_alt = models.CharField(max_length=200, verbose_name=_('Nazwa'))
    visible = models.BooleanField(default=False, verbose_name=_('Zaznacz jesli element ma byc widoczny i nie pomijany'))
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)
    element_order = models.IntegerField(default=0, verbose_name=_('Kolejnosc'))

    def __str__(self):
        return '%s ( %i )' % (self.image_alt, self.element_order)

    class Meta:
        verbose_name = _('Element slidera')
        verbose_name_plural = _('Elementy slidera')


class MainBoxItem(models.Model):
    header_text = models.CharField(max_length=400, verbose_name=_('Tekst naglowka'))
    image = models.ImageField(upload_to='images/', verbose_name=_('Obrazek'))
    image_alt = models.CharField(max_length=200, verbose_name=_('Nazwa'))
    description = RichTextField(verbose_name=_('Opis'))
    visible = models.BooleanField(default=False, verbose_name=_('Zaznacz jesli element ma byc widoczny i nie pomijany'))
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)
    element_order = models.IntegerField(default=0, verbose_name=_('Kolejnosc'))

    def __str__(self):
        return '%s ( %i )' % (self.header_text, self.element_order)

    class Meta:
        verbose_name = _('Box / karta')
        verbose_name_plural = _('Karty/boxy na stronie glownej')
