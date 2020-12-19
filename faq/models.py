from django.db import models
from djrichtextfield.models import RichTextField
from django.utils.translation import ugettext_lazy as _


class FaqConfiguration(models.Model):
    main_image = models.ImageField(upload_to='images/', verbose_name=_('Glowny obrazek'))
    main_image_alt = models.CharField(max_length=200, verbose_name=_('Nazwa'))
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)

    def __str__(self):
        return "Konfiguracja pytan"

    class Meta:
        verbose_name = _('Konfiguracja pytan')
        verbose_name_plural = _('Konfiguracja pytan')


class FaqItem(models.Model):
    question_text = RichTextField(verbose_name=_('Tresc pytania'))
    answer_text = RichTextField(verbose_name=_('Tresc odpowiedzi'))
    update_date = models.DateTimeField('Data aktualizacji', auto_now=True)
    element_order = models.IntegerField(default=0, verbose_name=_('Kolejnosc'))

    def __str__(self):
        return '%s %s ( %i )' % (self.question_text, self.answer_text, self.element_order)

    class Meta:
        verbose_name = _('Pytanie i odpowiedz (faq)')
        verbose_name_plural = _('Pytania i odpowiedzi (faqs)')
