from django.utils.translation import ugettext_lazy as _
from django import forms

from demosite.constants import field_required, incorrect_email_format, newsletter_permission_required
from .models import Newsletter
from bootstrap_modal_forms.forms import BSModalModelForm


class NewsletterForm(BSModalModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"
        error_messages = {
            'message': {'required': field_required},
            'name': {'required': field_required},
            'permission': {'required': newsletter_permission_required}
        }
        labels = {
            "permission": _('Wyrażam zgodę na przetwarzanie podanych powyżej danych w celu otrzymywania newslettera. ' +
                            'Wyrażam zgodę na przesyłanie na mój adres e-mail informacji o nowościach, promocjach, produktach i usługach od firmy Justyna Pietraszek Mobilne Centrum Masażu Relaksownia. ' +
                            'Zapoznałem się z Polityką Prywatności.'),
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
        self.fields['permission'].required = True
        self.fields['permission'].error_messages.update({
            'required': newsletter_permission_required
        })
