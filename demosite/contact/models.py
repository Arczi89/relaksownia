from django.db import models


class Contact(models.Model):
    contact_id = models.IntegerField()
    message = models.CharField(max_length=2000)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    # history = audit.AuditTrail() TODO+ zrobiłem zapisywanie historii zmian

    def __str__(self):
        return '%s %s' % (self.message, self.email_text)
