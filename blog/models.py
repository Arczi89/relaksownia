from django.db import models
from djrichtextfield.models import RichTextField
from datetime import datetime


class BlogConfiguration(models.Model):
    app_name = "Blog"
    main_image = models.ImageField(upload_to='images/', help_text='Obrazek wyswietlany na gorze strony pod menu')
    main_image_alt = models.CharField(max_length=400, help_text='Tekst wyświetlany w przypadku gdyby obrazek sie nie zaladowal')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return self.app_name + " page configuration"


class BlogPost(models.Model):
    photo = models.ImageField(upload_to='images/', help_text='Glowny obrazek posta')
    photo_alt = models.CharField(max_length=400, help_text='Tekst wyświetlany w przypadku gdyby obrazek sie nie zaladowal')
    description = RichTextField(help_text='Glowny tekst posta')
    publication_date = models.DateTimeField(default=datetime.now(), help_text='Data publikacji posta')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return "main blog"
