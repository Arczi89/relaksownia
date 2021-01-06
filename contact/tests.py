from http import HTTPStatus

from django.contrib.messages import get_messages
from django.template.loader import render_to_string
from django.test import TestCase
from demosite.constants import incorrect_email_format, field_name_required, field_message_required, \
    field_email_required, field_permission_required
from .forms import ContactForm
from .models import ContactConfiguration


class ContactRequestTests(TestCase):

    def addBasicConfiguration(self):
        configuration = ContactConfiguration(
            phone_number="123456789",
            email="test@test.pl"
        )
        configuration.save()
        return configuration.pk

    def removeBasicConfiguration(self):
        obj = ContactConfiguration.objects.get(pk=self.configurationPk)
        obj.delete()

    def setUp(self):
        self.baseUrl = "/contact/"
        self.valid_form_data = {
            "email": "test@test.pl",
            "message": "test message",
            "name": "Jan Kowalski",
            "permission": True
        }
        self.configurationPk = self.addBasicConfiguration()

    def test_contact_page_loaded(self):
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_should_message_name_email_and_permission_be_required_fields(self):
        form_data = {
            "email": "",
            "message": "",
            "name": "",
            "permission": False
        }

        form = ContactForm(data=form_data)

        self.assertIn(field_name_required, form.errors['name'], "name should be required")
        self.assertIn(field_message_required, form.errors['message'], "message should be required")
        self.assertIn(field_email_required, form.errors['email'], "email should be required")
        self.assertIn(field_permission_required, form.errors['permission'], "permission should be required")
        self.assertFalse(form.is_valid(), "name and massage and email should be required")

    def test_should_email_has_correct_format(self):
        form_data = {
            "email": "TEST",
            "phone": "123456789",
            "message": "test",
            "name": "test",
            "permission": True
        }

        form = ContactForm(data=form_data)

        self.assertIn(incorrect_email_format, form.errors['email'])
        self.assertFalse(form.is_valid(), "email format should be valid")

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
