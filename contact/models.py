from django.db import models
from djrichtextfield.models import RichTextField
from phonenumber_field.modelfields import PhoneNumberField


class ContactConfiguration(models.Model):
    app_name = "Contact"
    map_url = models.CharField(max_length=350, help_text='Url (adres) do mapy google')
    phone_number = PhoneNumberField()
    email = models.EmailField()
    on_site_client_info = RichTextField(help_text='Informacja o tym, ze dojezdzasz do klienta', default='')
    have_questions = RichTextField(help_text='Informacja nad formularzem "czy masz pytania?"', default='')
    working_hours = RichTextField(help_text='Godziny pracy')
    facebook = models.CharField(max_length=200, help_text='Url (adres) do facebooka', default='', blank=True)
    twitter = models.CharField(max_length=200, help_text='Url (adres) do twittera', default='', blank=True)
    linkedin = models.CharField(max_length=200, help_text='Url (adres) do LinkedIn', default='', blank=True)
    instagram = models.CharField(max_length=200, help_text='Url (adres) do Instagrama', default='', blank=True)
    snapchat = models.CharField(max_length=200, help_text='Url (adres) do Snapchat', default='', blank=True)
    youtube = models.CharField(max_length=200, help_text='Url (adres) do YouTube', default='', blank=True)
    google_plus = models.CharField(max_length=200, help_text='Url (adres) do Google+', default='', blank=True)
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return self.app_name + " page configuration"


class Contact(models.Model):
    message = models.TextField(max_length=2000, help_text='Wiadomosc od klienta')
    email = models.EmailField(max_length=300, help_text='Email klienta', blank=True)
    phone = models.CharField(max_length=400, help_text='Telefon klienta', blank=True)
    name = models.CharField(max_length=400, help_text='Imie klienta')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return '%s %s %s' % (self.name, self.email, self.phone)

