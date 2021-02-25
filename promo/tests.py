import tempfile
from http import HTTPStatus

from django.test import TestCase

from demosite.constants import field_required, inpost_code_or_delivery_place_required
from demosite.tests import SortAssert
from promo.forms import PromoClientForm
from promo.models import PromoPageComponent
from promo.tests_data import retrieve_correct_form_data, retrieve_incorrect_form_data_inpost_to_company, \
    retrieve_incorrect_form_data_inpost_to_person, retrieve_incorrect_form_data_courier_to_company, \
    retrieve_incorrect_form_data_courier_to_person


class PromoTests(TestCase):

    def addPromoComponent(self, order=0):
        promo_item = PromoPageComponent(
            photo=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_alt="main_image_alt",
            photo_responsive1=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_responsive1_alt="photo_responsive1_alt",
            photo_responsive2=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_responsive2_alt="photo_responsive2_alt",
            element_order=order
        )
        promo_item.save()

    def setUp(self):
        self.baseUrl = "/promo/"

    def test_promo_page_loaded(self):
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_promo_elements_are_in_incorrect_order(self):
        # Arrange
        self.addPromoComponent(0)
        self.addPromoComponent(2)
        self.addPromoComponent(1)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        SortAssert(response, 'promoItems').checkOrderOfElements()

    def test_promo_elements_with_the_same_order_number_are_incorrect_ordered(self):
        # Arrange
        self.addPromoComponent(6)
        self.addPromoComponent(6)
        self.addPromoComponent(1)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        SortAssert(response, 'promoItems').checkOrderOfElements()

    def test_form_required_fields_courier_to_person(self):
        # Arrange && Act
        data = retrieve_incorrect_form_data_courier_to_person()
        form = PromoClientForm(data=data)

        # Assert
        self.assertIn(field_required, form.errors['contact_name'])
        self.assertIn(field_required, form.errors['phone'])
        self.assertIn(field_required, form.errors['street'])
        self.assertIn(field_required, form.errors['postcode'])
        self.assertIn(field_required, form.errors['city'])
        self.assertIn(field_required, form.errors['permission'])

    def test_form_required_fields_courier_to_company(self):
        # Arrange && Act
        data = retrieve_incorrect_form_data_courier_to_company()
        form = PromoClientForm(data=data)
        # Assert
        self.assertIn(field_required, form.errors['contact_name'])
        self.assertIn(field_required, form.errors['company_name'])
        self.assertIn(field_required, form.errors['phone'])
        self.assertIn(field_required, form.errors['street'])
        self.assertIn(field_required, form.errors['postcode'])
        self.assertIn(field_required, form.errors['city'])
        self.assertIn(field_required, form.errors['nip'])
        self.assertIn(field_required, form.errors['permission'])

    def test_form_required_fields_inpost_to_person(self):
        # Arrange && Act
        data = retrieve_incorrect_form_data_inpost_to_person()
        form = PromoClientForm(data=data)

        # Assert
        self.assertIn(field_required, form.errors['contact_name'])
        self.assertIn(field_required, form.errors['phone'])
        self.assertIn(inpost_code_or_delivery_place_required, form.errors['delivery_place'])
        self.assertIn(inpost_code_or_delivery_place_required, form.errors['inpost_code'])
        self.assertIn(field_required, form.errors['permission'])

    def test_form_required_fields_inpost_to_company(self):
        # Arrange && Act
        data = retrieve_incorrect_form_data_inpost_to_company()
        form = PromoClientForm(data=data)

        # Assert
        self.assertIn(field_required, form.errors['contact_name'])
        self.assertIn(field_required, form.errors['company_name'])
        self.assertIn(field_required, form.errors['phone'])
        self.assertIn(inpost_code_or_delivery_place_required, form.errors['delivery_place'])
        self.assertIn(inpost_code_or_delivery_place_required, form.errors['inpost_code'])
        self.assertIn(field_required, form.errors['nip'])
        self.assertIn(field_required, form.errors['permission'])

    def test_form_accept_delivery_place_instead_of_inpost_code(self):
        # Arrange && Act
        data = retrieve_correct_form_data()
        data['delivery_place'] = "some delivery place"
        data['inpost_code'] = ""
        form = PromoClientForm(data=data)
        # Act
        self.assertTrue(form.is_valid(), 'Form require inpost code when delivery place is provided but it should not')

    def test_form_accept_inpost_code_instead_of_delivery_place(self):
        # Arrange && Act
        data = retrieve_correct_form_data()
        data['delivery_place'] = ""
        data['inpost_code'] = "some inpost code"
        form = PromoClientForm(data=data)
        # Assert
        self.assertTrue(form.is_valid(), 'Form require delivery place when inpost code is provided but it should not')

    def test_form_accept_inpost_code_instead_of_delivery_place(self):
        # Arrange && Act
        data = retrieve_correct_form_data()
        data['inpost_code'] = ""
        data['delivery_place'] = ""
        form = PromoClientForm(data=data)
        # Assert
        self.assertFalse(form.is_valid(), 'Form require delivery place or inpost code')
