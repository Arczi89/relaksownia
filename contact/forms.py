from django import forms
from djrichtextfield.widgets import RichTextWidget

from demosite.constants import field_required, email_or_phone_required
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        error_messages = {
            'message': {'required': "To pole jest wymagane"},
            'name': {'required': "To pole jest wymagane"}
        }

    message = forms.CharField(widget=RichTextWidget(), required=True)
    email = forms.EmailField(max_length=100, label='Email', required=False)
    phone = forms.CharField(max_length=9, label='Telefon', min_length=9, required=False)
    name = forms.CharField(max_length=40, label='Twoje imię', required=True)
    attachment_img = forms.ImageField(label='Opcjonalny załącznik', required=False)

    def clean(self):
        super().clean()
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
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