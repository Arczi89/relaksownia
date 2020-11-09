from http import HTTPStatus

from django.contrib.messages import get_messages
from django.template.loader import render_to_string
from django.test import TestCase

from demosite.constants import email_or_phone_required, field_required, incorrect_email_format, incorrect_phone_format

from .forms import ContactForm


# TODO+ django data driven test - taki sam kształt testu, zmieniają się tylko dane
# TODO+ assertPy - biblioteka do asercji
# TODO+ klasa bazowa z metodami setupowymi do tworzenia wspólnych obiektów

class ContactRequestTests(TestCase):

    def setUp(self):
        self.baseUrl = "/contact/"
        self.valid_form_data = {
            "email": "test@test.pl",
            "message": "test message",
            "name": "Jan Kowalski",
            "phone": "123123123"
        }

    def test_contact_page_loaded(self):
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_should_contact_phone_not_required_when_email_provided(self):
        form_data = {
            "email": "test@test.pl",
            "message": "test message",
            "name": "Jan Kowalski",
            "phone": ""
        }

        form = ContactForm(data=form_data)

        self.assertEqual(len(form.errors), 0, "form should not have errors")
        self.assertTrue(form.is_valid(), "form should be valid with correct email, message and name provided")

    def test_should_contact_email_not_required_when_phone_provided(self):
        form_data = {
            "phone": "500400200",
            "message": "test message",
            "name": "Jan Kowalski",
            "email": ""
        }

        form = ContactForm(data=form_data)

        self.assertTrue(form.is_valid(), "form should be valid with correct phone, message and name provided")
        self.assertEqual(len(form.errors), 0, "form should not have error:")

    def test_should_message_and_name_be_required_fields(self):
        form_data = {
            "email": "test@test.pl",
            "phone": "512345678",
            "message": "",
            "name": ""
        }

        form = ContactForm(data=form_data)

        self.assertIn(field_required, form.errors['name'], "name should be required")
        self.assertIn(field_required, form.errors['message'], "message should be required")
        self.assertFalse(form.is_valid(), "name and massage should be required")

    def test_should_email_or_message_be_required(self):
        form_data = {
            "email": "",
            "phone": "",
            "message": "test",
            "name": "test"
        }

        form = ContactForm(data=form_data)

        self.assertFalse(form.is_valid(), "phone or email should be provided")
        self.assertIn(email_or_phone_required, form.errors['__all__'], "'email_or_phone_required' error should be added")

    def test_should_email_has_correct_format(self):
        form_data = {
            "email": "TEST",
            "phone": "123456789",
            "message": "test",
            "name": "test"
        }

        form = ContactForm(data=form_data)

        self.assertIn(incorrect_email_format, form.errors['email'])
        self.assertFalse(form.is_valid(), "email format should be valid")

    def test_should_phone_has_correct_format(self):
        form_data = {
            "email": "TEST@TEST.pl",
            "phone": "x234w562",
            "message": "test",
            "name": "test"
        }

        form = ContactForm(data=form_data)

        self.assertIn(incorrect_phone_format, form.errors['__all__'])
        self.assertFalse(form.is_valid(), "phone format should have 9 digits")

    def test_should_display_contact_form(self):
        # Arrange & Act
        response = self.client.get(self.baseUrl)
        # Assert
        self.assertTrue('form' in response.context, "form should be included in response")

    def test_should_return_success_message_on_valid_form_save(self):
        # Arrange & Act
        response = self.client.post(self.baseUrl, data=self.valid_form_data)
        # Assert
        self.assertEqual(response.status_code, 302, "page should be redirect/reload after save")
        self.assertEqual(len(list(get_messages(response.wsgi_request))), 1, "success message should be displayed after successfully contact form sent")

    def test_should_contact_data_be_saved_correctly_into_db(self):
        # Arrange
        form_data = self.valid_form_data
        form = ContactForm(data=form_data)
        # Act
        result = form.save()
        # Assert
        self.assertIsNotNone(result.pk, "object is not created in db")
        self.assertEqual(result.email, form.data['email'], "email is not saved correctly")
        self.assertEqual(result.message, form.data['message'], "message is not saved correctly")
        self.assertEqual(result.name, form.data['name'], "name is not saved correctly")
        self.assertEqual(result.phone, form.data['phone'], "phone is not saved correctly")

    def test_should_all_section_be_visible_in_page(self):
        # Arrange
        template_name = "contact.html"
        context = {
            "configuration": "not empty"
        }
        # Act
        result = render_to_string(template_name, context)
        # Assert
        self.assertTrue("iframe" in result, "there is map section on page")
        self.assertTrue("contact-left" in result, "there is no left section on page")
        self.assertTrue("contact-right" in result, "there is no right section on page")
