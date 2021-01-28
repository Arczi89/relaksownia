from django.db import models
from djrichtextfield.models import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _


class ContactConfiguration(models.Model):
    app_name = "Kontakt"
    map_url = models.CharField(max_length=350, verbose_name=_('Url (adres) do mapy google'))
    phone_number = PhoneNumberField(verbose_name=_('Twoj numer telefonu'), help_text='Bedzie on wyswietlany zarowno na stronie kontakt jak i w stopce')
    email = models.EmailField(verbose_name=_('Twoj email'))
    on_site_client_info = RichTextField(verbose_name=_('Informacja o tym, ze dojezdzasz do klienta'), default='')
    have_questions = RichTextField(verbose_name=_('Informacja nad formularzem "czy masz pytania?"'), default='')
    working_hours = RichTextField(verbose_name=_('Godziny pracy'))
    facebook = models.CharField(max_length=200, verbose_name=_('Url (adres) do facebooka'), default='', blank=True)
    twitter = models.CharField(max_length=200, verbose_name=_('Url (adres) do twittera'), default='', blank=True)
    linkedin = models.CharField(max_length=200, verbose_name=_('Url (adres) do LinkedIn'), default='', blank=True)
    instagram = models.CharField(max_length=200, verbose_name=_('Url (adres) do Instagrama'), default='', blank=True)
    snapchat = models.CharField(max_length=200, verbose_name=_('Url (adres) do Snapchat'), default='', blank=True)
    youtube = models.CharField(max_length=200, verbose_name=_('Url (adres) do YouTube'), default='', blank=True)
    google_map = models.CharField(max_length=200, verbose_name=_('Url (adres) do Google+'), default='', blank=True)
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)

    def __str__(self):
        return self.app_name + " konfiguracja"

    class Meta:
        verbose_name = _('Konfiguracja strony kontakt i informacji kontaktowych')
        verbose_name_plural = _('Konfiguracja strony kontakt i informacji kontaktowych')


class Contact(models.Model):
    message = models.TextField(max_length=2000, verbose_name=_('Wiadomosc od klienta'))
    email = models.EmailField(max_length=300, verbose_name=_('Email klienta'))
    name = models.CharField(max_length=400, verbose_name=_('Imie klienta'))
    permission = models.BooleanField(verbose_name=_('Zgoda na kontakt'))
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)

    def __str__(self):
        return '%s | %s | %s' % (self.name, self.email)

    class Meta:
        verbose_name = _('Zapisany kontakt do klienta')
        verbose_name_plural = _('Dane klientow')

