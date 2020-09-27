from django.db import models
from djrichtextfield.models import RichTextField


class SliderItem(models.Model):
    image = models.ImageField(upload_to='images/')
    image_alt = models.CharField(max_length=400)
    visible = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.image_alt


class ContainerItem(models.Model):
    header_text = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/')
    image_alt = models.CharField(max_length=400)
    description = RichTextField()
    visible = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.header_text


class Info(models.Model):
    photo = models.ImageField(upload_to='images/')
    photo_alt = models.CharField(max_length=400)
    description = RichTextField()

    def __str__(self):
        return "main info"
