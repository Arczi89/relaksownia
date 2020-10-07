from django.db import models
from djrichtextfield.models import RichTextField


class Blog(models.Model):
    photo = models.ImageField(upload_to='images/')
    photo_alt = models.CharField(max_length=400)
    description = RichTextField()
    update_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return "main blog"
