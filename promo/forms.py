from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from django import forms

from demosite.constants import field_required, inpost_code_or_delivery_place_required
from promo.models import PromoClient, DeliveryKind


class PromoClientForm(ModelForm):
    class Meta:
        model = PromoClient
        fields = '__all__'
        error_messages = {
            'phone': {'required': field_required},
            'permission': {'required': field_required}
        }
        widgets = {
            'contact_name': forms.TextInput(attrs={'placeholder': _('Imię i nazwisko osoby kontaktowej')}),
            'email': forms.TextInput(attrs={'placeholder': _('Adres e-mail')}),
            'phone': forms.TextInput(attrs={'placeholder': _('Telefon kontaktowy')}),
            'street': forms.TextInput(attrs={'placeholder': _('Ulica i numer mieszkania')}),
            'postcode': forms.TextInput(attrs={'placeholder': _('Kod pocztowy')}),
            'city': forms.TextInput(attrs={'placeholder': _('Miasto')}),
            'inpost_code': forms.TextInput(attrs={'placeholder': _('Kod INPOST')}),
            'delivery_place': forms.TextInput(attrs={'placeholder': _('Miejsce dostawy')}),
            'is_vat': forms.CheckboxInput(attrs={'placeholder': _('Czy faktura VAT (firma)?')}),
            'company_name': forms.TextInput(attrs={'placeholder': _('Nazwa firmy')}),
            'nip': forms.TextInput(attrs={'placeholder': _('Numer NIP')}),
            'permission': forms.CheckboxInput(attrs={'placeholder': _('Zgoda na przetwarzanie danych')})
        }
        labels = {
            "permission": _('Korzystając z formularza zgadzam się na przechowywanie i przetwarzanie moich danych osobowych. '
                            'Dane są przechowywane w celu udzielenia odpowiedzi na przesłane zapytanie i nie są wykorzystywane w '
                            'celach marketingowych. Zapoznałem się z Polityką prywatności.'),
            "is_vat": _('Czy faktura VAT (firma)?')
        }

    def __init__(self, *args, **kwargs):
        super(PromoClientForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PromoClientForm, self).clean()
        self.errors
        self.validate_permission(cleaned_data)
        self.validate_inpost_to_company(cleaned_data)
        self.validate_inpost_to_person(cleaned_data)
        self.validate_courier_to_company(cleaned_data)
        self.validate_courier_to_person(cleaned_data)
        return cleaned_data

    def validate_permission(self, data):
        if not data['permission']:
            self.add_error('permission', field_required)

    def validate_inpost_to_company(self, data):
        if data['is_vat'] and data['delivery_kind'] == DeliveryKind.get_value("INPOST"):
            self.validate_delivery_place_or_inpost_code_required(data)
            if not data['contact_name']:
                self.add_error('contact_name', field_required)
            if not data['company_name']:
                self.add_error('company_name', field_required)
            if not data['nip']:
                self.add_error('nip', field_required)

    def validate_courier_to_company(self, data):
        if data['is_vat'] and data['delivery_kind'] == DeliveryKind.get_value("COURIER"):
            self.validate_delivery_place_or_inpost_code_required(data)
            if not data['contact_name']:
                self.add_error('contact_name', field_required)
            if not data['company_name']:
                self.add_error('company_name', field_required)
            if not data['nip']:
                self.add_error('nip', field_required)
            if not data['street']:
                self.add_error('street', field_required)
            if not data['postcode']:
                self.add_error('postcode', field_required)
            if not data['city']:
                self.add_error('city', field_required)

    def validate_courier_to_person(self, data):
        if not data['is_vat'] and data['delivery_kind'] == DeliveryKind.get_value("COURIER"):
            self.validate_delivery_place_or_inpost_code_required(data)
            if not data['contact_name']:
                self.add_error('contact_name', field_required)
            if not data['street']:
                self.add_error('street', field_required)
            if not data['postcode']:
                self.add_error('postcode', field_required)
            if not data['city']:
                self.add_error('city', field_required)

    def validate_inpost_to_person(self, data):
        if not data['is_vat'] and data['delivery_kind'] == DeliveryKind.get_value("INPOST"):
            self.validate_delivery_place_or_inpost_code_required(data)
            if not data['contact_name']:
                self.add_error('contact_name', field_required)

    def validate_delivery_place_or_inpost_code_required(self, data):
        if data is not None:
            if not data.get("inpost_code") and not data.get("delivery_place"):
                self.add_error("inpost_code", inpost_code_or_delivery_place_required)
                self.add_error("delivery_place", inpost_code_or_delivery_place_required)