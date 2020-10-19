from django.utils.translation import ugettext_lazy as _
from django import forms

from .models import Newsletter
from bootstrap_modal_forms.forms import BSModalModelForm


class NewsletterForm(BSModalModelForm):
    class Meta:
        model = Newsletter
        labels = {
            "permission": _('Wyrażam zgodę na przesyłanie mi ofert marketingowych i promocyjnych drogą elektroniczną'),
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': _('Adres e-mail')}),
            'name': forms.TextInput(attrs={'placeholder': _('Imię')}),
        }
        fields = "__all__"
