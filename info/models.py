from django.db import models
from djrichtextfield.models import RichTextField

# TODO+ zmienilem nazwę (na infoConfiguration) po zmianie modelu
class Info(models.Model):
    photo = models.ImageField(upload_to='images/')
    photo_alt = models.CharField(max_length=400)
    description = RichTextField()
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return "main info"
