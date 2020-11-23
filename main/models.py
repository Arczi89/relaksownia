from django.db import models
from djrichtextfield.models import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator


class MainConfiguration(models.Model):
    app_name = "Main"
    is_modal_visible = models.BooleanField(default=False)
    newsletter_info = RichTextField()
    main_text = RichTextField()
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return self.app_name + " page configuration"


class MainSliderConfiguration(models.Model):
    change_image_time_ms = models.PositiveIntegerField(validators=[MinValueValidator(100) ,MaxValueValidator(10000)], help_text='Czas po ktorym zmieni sie obrazek w sliderze')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return "Main page slider configuration"


class MainSliderItem(models.Model):
    image = models.ImageField(upload_to='images/')
    image_alt = models.CharField(max_length=400, help_text='Tekst wyświetlany w przypadku gdyby obrazek sie nie zaladowal')
    visible = models.BooleanField(default=False, help_text='Gdy False to dany obrazek jest niewidoczny i pomijany w sliderze')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return self.image_alt


class MainBoxItem(models.Model):
    header_text = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/')
    image_alt = models.CharField(max_length=400, help_text='Tekst wyświetlany w przypadku gdyby obrazek sie nie zaladowal')
    description = RichTextField()
    visible = models.BooleanField(default=False, help_text='Gdy False to dany obrazek jest niewidoczny i pomijany')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return self.header_text
