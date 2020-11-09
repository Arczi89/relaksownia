from django.utils.translation import ugettext_lazy as _
from django import forms

from demosite.constants import field_required, incorrect_email_format
from .models import Newsletter
from bootstrap_modal_forms.forms import BSModalModelForm


class NewsletterForm(BSModalModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"
        error_messages = {
            'message': {'required': "To pole jest wymagane"},
            'name': {'required': "To pole jest wymagane"}
        }
        labels = {
            "permission": _('Wyrażam zgodę na przesyłanie mi ofert marketingowych i promocyjnych drogą elektroniczną'),
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': _('Adres e-mail')}),
            'name': forms.TextInput(attrs={'placeholder': _('Imię')}),
        }

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages.update({
            'required': field_required
        })
        self.fields['email'].error_messages.update({
            'invalid': incorrect_email_format,
            'required': field_required
        })

