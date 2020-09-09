from django.db import models


class SliderItem(models.Model):
    image_url = models.CharField(max_length=3000)
    image_alternate_text = models.CharField(max_length=3000)
    visible = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    # history = audit.AuditTrail() TODO+ zrobiłem zapisywanie historii zmian

    def __str__(self):
        return self.image_alternate_text


class ContainerItem(models.Model):
    image_url = models.CharField(max_length=3000)
    image_alternate_text = models.CharField(max_length=3000)
    description = models.CharField(max_length=3000)
    visible = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    # history = audit.AuditTrail() TODO+ zrobiłem zapisywanie historii zmian

    def __str__(self):
        return '%s %s' % (self.image_alternate_text, self.description)
