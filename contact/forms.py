from django.utils.translation import ugettext_lazy as _
from django import forms

from demosite.constants import incorrect_email_format, field_name_required, field_message_required, \
    field_email_required, field_permission_required, field_required
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        error_messages = {
            'message': {'required': field_required},
            'name': {'required': field_required},
            'email': {'required': field_required},
            'permission': {'required': field_required}
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': _('Adres e-mail')}),
            'name': forms.TextInput(attrs={'placeholder': _('Imię')}),
            'phone': forms.TextInput(attrs={'placeholder': _('Numer telefonu')}),
            'message': forms.Textarea(attrs={'placeholder': _('Wpisz swoją wiadomość')})
        }
        labels = {
            "permission": _('Korzystając z formularza zgadzam się na przechowywanie i przetwarzanie moich danych osobowych. '
                            'Dane są przechowywane w celu udzielenia odpowiedzi na przesłane zapytanie i nie są wykorzystywane w '
                            'celach marketingowych. Zapoznałem się z Polityką prywatności.'),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages.update({
            'required': field_name_required
        })
        self.fields['message'].error_messages.update({
            'required': field_message_required
        })
        self.fields['permission'].required = True
        self.fields['permission'].error_messages.update({
            'required': field_permission_required
        })
        self.fields['email'].error_messages.update({
            'invalid': incorrect_email_format,
            'required': field_email_required
        })
