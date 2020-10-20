from django.utils.translation import ugettext_lazy as _
from django import forms
import re

from demosite.constants import field_required, email_or_phone_required, incorrect_extension, incorrect_phone_format, \
    incorrect_email_format
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        error_messages = {
            'message': {'required': "To pole jest wymagane"},
            'name': {'required': "To pole jest wymagane"}
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': _('Adres e-mail')}),
            'name': forms.TextInput(attrs={'placeholder': _('Imię')}),
            'phone': forms.TextInput(attrs={'placeholder': _('Numer telefonu')}),
            'message': forms.Textarea(attrs={'placeholder': _('Wpisz swoją wiadomość')}),
        }

    def clean(self):
        super().clean()
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')

        phone_pattern = r"\d{9}"
        if phone and not re.search(phone_pattern, phone):
            raise forms.ValidationError(incorrect_phone_format)

        if not email and not phone:
            raise forms.ValidationError(email_or_phone_required)

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages.update({
            'required': field_required
        })
        self.fields['message'].error_messages.update({
            'required': field_required
        })
        self.fields['phone'].error_messages.update({
            'max_length': incorrect_phone_format
        })
        self.fields['email'].error_messages.update({
            'invalid': incorrect_email_format #TODO fix
        })
        self.fields['attachment_img'].error_messages.update({
            'file_extension': incorrect_extension  #TODO fix
        })
