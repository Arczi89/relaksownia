from django.db import models
from djrichtextfield.models import RichTextField


class OpinionsConfiguration(models.Model):
    app_name = "Opinions"
    main_image = models.ImageField(upload_to='images/', help_text='Obrazek wyswietlany na gorze strony pod menu')
    main_image_alt = models.CharField(max_length=400, help_text='Tekst wyświetlany w przypadku gdyby obrazek sie nie zaladowal')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return self.app_name + " page configuration"


class OpinionItem(models.Model):
    opinion_text = RichTextField(help_text='Tekst rekomendacji')
    customer_name = models.CharField(max_length=400, help_text='Imie osoby polecajacej')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return self.customer_name
