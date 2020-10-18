from django.db import models
from djrichtextfield.models import RichTextField
from phonenumber_field.modelfields import PhoneNumberField


class ContactConfiguration(models.Model):
    app_name = "Contact"
    map_url = models.CharField(max_length=400, help_text='Url (adres) do mapy google')
    phone_number = PhoneNumberField()
    email = models.EmailField()
    on_site_client_info = RichTextField(help_text='Informacja o tym, ze dojezdzasz do klienta', default='')
    have_questions = RichTextField(help_text='Informacja nad formularzem "czy masz pytania?"', default='')
    working_hours = RichTextField(help_text='Godziny pracy')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return self.app_name + " page configuration"


class Contact(models.Model):
    message = RichTextField()
    email = models.EmailField(max_length=300, help_text='Email klienta')
    phone = models.CharField(max_length=400, help_text='Telefon klienta')
    name = models.CharField(max_length=400, help_text='Imie klienta')
    attachment_img = models.ImageField(max_length=400, help_text='Klient moze zalaczyc obrazek, screen', upload_to='images/')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return '%s %s %s' % (self.name, self.email, self.phone)
