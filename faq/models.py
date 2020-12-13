from django.db import models
from djrichtextfield.models import RichTextField


class FaqConfiguration(models.Model):
    main_image = models.ImageField(upload_to='images/', help_text='Obrazek wyswietlany na gorze strony pod menu')
    main_image_alt = models.CharField(max_length=200, help_text='Tekst wyświetlany w przypadku gdyby obrazek sie nie zaladowal')
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return "Faq page configuration"


class FaqItem(models.Model):
    question_text = RichTextField()
    answer_text = RichTextField()
    update_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return '%s %s' % (self.question_text, self.answer_text)
