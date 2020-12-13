from django.db import models
from django.utils.translation import ugettext_lazy as _


class Newsletter(models.Model):
    email = models.EmailField(max_length=300, verbose_name=_('Email klienta'))
    name = models.CharField(max_length=400, verbose_name=_('Imie klienta'))
    permission = models.BooleanField(verbose_name=_('Zgoda na marketing'))
    update_date = models.DateTimeField(verbose_name=_('Data modyfikacji'), auto_now=True)

    def __str__(self):
        return self.name + " - " + self.email + "; zapisany: " + self.update_date.__str__()

    class Meta:
        verbose_name = _('Klient')
        verbose_name_plural = _('Dane klientow zapisanych na newsletter')