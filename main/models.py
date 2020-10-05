from django.db import models
from djrichtextfield.models import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator


class SliderConfiguration(models.Model):
    change_image_time_ms = models.PositiveIntegerField(validators=[MinValueValidator(100) ,MaxValueValidator(10000)])

class SliderItem(models.Model):
    image = models.ImageField(upload_to='images/')
    image_alt = models.CharField(max_length=400)
    visible = models.BooleanField(default=False)
    update_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.image_alt


class ContainerItem(models.Model):
    header_text = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/')
    image_alt = models.CharField(max_length=400)
    description = RichTextField()
    visible = models.BooleanField(default=False)
    update_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.header_text


class Info(models.Model):
    photo = models.ImageField(upload_to='images/')
    photo_alt = models.CharField(max_length=400)
    description = RichTextField()
    update_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return "main info"
