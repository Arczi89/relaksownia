from django.db import models
from djrichtextfield.models import RichTextField
from datetime import datetime


class OfferConfiguration(models.Model):
    main_title = models.TextField()
    main_text = RichTextField()
    update_date = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.main_title


class OfferItem(models.Model):
    title = models.TextField()
    text = RichTextField()
    image = models.ImageField()
    image_alt = models.TextField()
    conf = models.ForeignKey('OfferConfiguration', on_delete=models.CASCADE)
    update_date = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.title

