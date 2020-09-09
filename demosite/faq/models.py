from django.db import models


class FaqItem(models.Model):
    question_text = models.CharField(max_length=3000)
    answer_text = models.CharField(max_length=3000)
    pub_date = models.DateTimeField('date published')
    # history = audit.AuditTrail() TODO+ zrobiłem zapisywanie historii zmian

    def __str__(self):
        return '%s %s' % (self.question_text, self.answer_text)
