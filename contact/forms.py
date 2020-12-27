from django.utils.translation import ugettext_lazy as _
from django import forms

from demosite.constants import incorrect_email_format, field_name_required, field_message_required, field_email_required
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        error_messages = {
            'message': {'required': "To pole jest wymagane"},
            'name': {'required': "To pole jest wymagane"},
            'email': {'required': "To pole jest wymagane"}
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': _('Adres e-mail')}),
            'name': forms.TextInput(attrs={'placeholder': _('Imię')}),
            'phone': forms.TextInput(attrs={'placeholder': _('Numer telefonu')}),
            'message': forms.Textarea(attrs={'placeholder': _('Wpisz swoją wiadomość')}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages.update({
            'required': field_name_required
        })
        self.fields['message'].error_messages.update({
            'required': field_message_required
        })
        self.fields['email'].error_messages.update({
            'invalid': incorrect_email_format,
            'required': field_email_required
        })
