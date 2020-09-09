from django.db import models


class ContactForm(models.Model):
    question_text = models.CharField(max_length=3000)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=20)
    # history = audit.AuditTrail() TODO+ zrobiłem zapisywanie historii zmian

    def __str__(self):
        return '%s %s' % (self.question_text, self.email_text)
