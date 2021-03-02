from enum import Enum

from django.db import models
from djrichtextfield.models import RichTextField
from django.utils.translation import ugettext_lazy as _

from demosite.constants import buy_permission_default, delivery_info_default, bank_account_number_default, \
    default_search_inpost_url


class DeliveryKind(Enum):
    COURIER = ("KURIER", _("KURIER"))
    INPOST = ("INPOST", _("INPOST"))

    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]


class PromoPageComponent(models.Model):
    photo = models.ImageField(upload_to='images/', verbose_name=_('Glowny obrazek'))
    photo_alt = models.CharField(max_length=100, verbose_name=_('Nazwa'))
    photo_responsive1 = models.ImageField(upload_to='images/', verbose_name=_('Kawalek 1 - do wersji responsywnej'))
    photo_responsive1_alt = models.CharField(max_length=100, verbose_name=_('Nazwa 1'))
    photo_responsive2 = models.ImageField(upload_to='images/', verbose_name=_('Kawalek 2 - do wersji responsywnej'))
    photo_responsive2_alt = models.CharField(max_length=100, verbose_name=_('Nazwa 2'))
    photo_responsive3 = models.ImageField(upload_to='images/', verbose_name=_('Kawalek 3 - do wersji responsywnej'),
                                          blank=True)
    photo_responsive3_alt = models.CharField(max_length=100, verbose_name=_('Nazwa 3'), blank=True)
    photo_responsive4 = models.ImageField(upload_to='images/', verbose_name=_('Kawalek 4 - do wersji responsywnej'),
                                          blank=True)
    photo_responsive4_alt = models.CharField(max_length=100, verbose_name=_('Nazwa 4'), blank=True)
    text = RichTextField(verbose_name=_('Tekst'), blank=True)
    text_position = models.IntegerField(default=1,
                                        verbose_name="Pozycja tekstu, jeśli jest jakiś ustawiony 1 - przed obrazkami, 2+ po obrazkach")
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)
    element_order = models.IntegerField(default=0, verbose_name=_('Kolejnosc'))

    def __str__(self):
        return '%s ( %i )' % (self.photo_alt, self.element_order)

    class Meta:
        verbose_name = _('Element strony promocji')
        verbose_name_plural = _('Elementy strony promocji')


class PromoConfiguration(models.Model):
    permission_text = RichTextField(verbose_name=_('Treść zgody przy formularzu zamówienia'), blank=False,
                                    default=buy_permission_default)
    delivery_info = RichTextField(verbose_name=_('Informacja o dostawie'), blank=False,
                                    default=delivery_info_default)
    bank_account_number = models.CharField(max_length=26, verbose_name=_('Numer konta bankowego'), blank=False,
                                    default=bank_account_number_default)
    inpost_code_search_info = models.CharField(max_length=100, verbose_name=_('Link do wyszukiwarki paczkomatow INPOST'), blank=False,
                                    default=default_search_inpost_url)


class PromoClient(models.Model):
    contact_name = models.CharField(max_length=100, verbose_name=_('Imie i nazwisko osoby kontaktowej'), blank=True)
    email = models.CharField(max_length=100, verbose_name=_('Adres email'))
    phone = models.TextField(max_length=20, verbose_name=_('Telefon'))
    delivery_kind = models.CharField(choices=[x.value for x in DeliveryKind], default=DeliveryKind.get_value('INPOST'),
                                     verbose_name=_('Czy kurier czy paczkomat?'), max_length=30)
    street = models.TextField(max_length=100, verbose_name=_('Ulica i numer'), blank=True)
    postcode = models.TextField(max_length=6, verbose_name=_('Kod pocztowy'), blank=True)
    city = models.TextField(max_length=100, verbose_name=_('Miasto'), blank=True)
    inpost_code = models.CharField(max_length=20, verbose_name=_('Kod InPost'), blank=True)
    delivery_place = models.CharField(max_length=100, verbose_name=_('Miejsce InPost (alternatywa dla kodu)'), blank=True)
    is_vat = models.BooleanField(default=False, verbose_name=_('Czy faktura VAT? Czy to firma?'))
    company_name = models.CharField(max_length=100, verbose_name=_('Nazwa firmy'), blank=True)
    nip = models.CharField(max_length=30, verbose_name=_('Numer NIP'), blank=True)
    permission = models.BooleanField(default=False, verbose_name=_('Czy klient wyrazil konieczna zgode?'), blank=True)

