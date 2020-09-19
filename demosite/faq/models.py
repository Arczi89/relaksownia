from django.db import models
from djrichtextfield.models import RichTextField


class FaqItem(models.Model):
    question_text = RichTextField()
    answer_text = RichTextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return '%s %s' % (self.question_text, self.answer_text)
