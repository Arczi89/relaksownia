from django.db import models
from djrichtextfield.models import RichTextField
from datetime import datetime


class FaqItem(models.Model):
    question_text = RichTextField()
    answer_text = RichTextField()
    update_date = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return '%s %s' % (self.question_text, self.answer_text)
