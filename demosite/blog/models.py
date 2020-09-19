from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=3000, default="")
    image = models.ImageField(upload_to='images')
    image_alternate_text = models.CharField(max_length=3000)
    description = models.CharField(max_length=3000)
    visible = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    tags = models.CharField(max_length=3000, default='ALL,')

    # history = audit.AuditTrail() TODO+ zrobiłem zapisywanie historii zmian

    def __str__(self):
        return '%s %s' % (self.image_alternate_text, self.description)
