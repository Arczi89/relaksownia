
from django.forms import ModelForm

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

    def __init__(self, *args, **kwargs):
        super(PromoClientForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PromoClientForm, self).clean()
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
        if data['is_vat'] and data['delivery_kind'] == DeliveryKind.INPOST:
            self.validate_delivery_place_or_inpost_code_required(data)
            if not data['contact_name']:
                self.add_error('contact_name', field_required)
            if not data['company_name']:
                self.add_error('company_name', field_required)
            if not data['nip']:
                self.add_error('nip', field_required)

    def validate_courier_to_company(self, data):
        if data['is_vat'] and data['delivery_kind'] == DeliveryKind.COURIER:
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
        if not data['is_vat'] and data['delivery_kind'] == DeliveryKind.COURIER:
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
        if not data['is_vat'] and data['delivery_kind'] == DeliveryKind.INPOST:
            self.validate_delivery_place_or_inpost_code_required(data)
            if not data['contact_name']:
                self.add_error('contact_name', field_required)

    def validate_delivery_place_or_inpost_code_required(self, data):
        if data is not None:
            if not data.get("inpost_code") and not data.get("delivery_place"):
                self.add_error("inpost_code", inpost_code_or_delivery_place_required)
                self.add_error("delivery_place", inpost_code_or_delivery_place_required)