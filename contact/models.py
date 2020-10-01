from django.db import models
from djrichtextfield.models import RichTextField


class Contact(models.Model):
    message = RichTextField()
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=400)
    name = models.CharField(max_length=400)

    def __str__(self):
        return '%s %s' % (self.name, self.email)
