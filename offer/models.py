from django.db import models
from djrichtextfield.models import RichTextField


class OfferConfiguration(models.Model):
    app_name = "Offers"
    main_image = models.ImageField(upload_to='images/', help_text='Obrazek wyswietlany na gorze strony pod menu')
    main_image_alt = models.CharField(max_length=200, help_text='Tekst wyświetlany w przypadku gdyby obrazek sie nie zaladowal')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return self.app_name + " page configuration"


class OfferItem(models.Model):
    title = models.TextField()
    text = RichTextField()
    image = models.ImageField(upload_to='images/')
    image_alt = models.TextField(help_text='Tekst wyświetlany w przypadku gdyby obrazek sie nie zaladowal')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return self.title

