from http import HTTPStatus

from django.contrib.messages import get_messages
from django.test import TestCase

from demosite.constants import field_required, incorrect_email_format, newsletter_permission_required
from main.models import MainConfiguration

from .forms import NewsletterForm


# TODO+ django data driven test - taki sam kształt testu, zmieniają się tylko dane
# TODO+ assertPy - biblioteka do asercji
# TODO+ klasa bazowa z metodami setupowymi do tworzenia wspólnych obiektów
from .models import Newsletter


class NewsletterTests(TestCase):

    def addBasicConfiguration(self):
        configuration = MainConfiguration(
            newsletter_info="Newsletter info",
            main_text="Main text"
        )
        configuration.save()
        return configuration.pk

    def removeBasicConfiguration(self):
        obj = MainConfiguration.objects.get(pk=self.configurationPk)
        obj.delete()

    def setUp(self):
        self.baseUrl = "/newsletter/"
        self.valid_form_data = {
            "email": "test@test.pl",
            "name": "Jan Kowalski",
            "permission": True
        }
        self.configurationPk = self.addBasicConfiguration()

    def test_newsletter_modal_loaded_without_configuration(self):
        self.removeBasicConfiguration()
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_newsletter_modal_loaded_with_configuration(self):
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_should_message_and_name_and_permission_be_required_fields(self):
        form_data = {
            "email": "",
            "name": "",
            "permission": False
        }
        form = NewsletterForm(data=form_data)

        self.assertIn(field_required, form.errors['name'], "name should be required")
        self.assertIn(field_required, form.errors['email'], "email should be required")
        self.assertIn(newsletter_permission_required, form.errors['permission'], "permission should be accepted")
        self.assertFalse(form.is_valid(), "name and email should be required, permision should be accepted")

    def test_should_email_has_correct_format(self):
        form_data = {
            "email": "TEST",
            "name": "test"
        }
        form = NewsletterForm(data=form_data)
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
        # Arrange & Act
        self.client.post(self.baseUrl, data=self.valid_form_data)
        # Assert
        saved_obj = Newsletter.objects.get(name=self.valid_form_data['name'])
        self.assertIsNotNone(saved_obj.pk, "object is not created in db")
        self.assertEqual(saved_obj.email, saved_obj.email, "email is not saved correctly")
        self.assertEqual(saved_obj.name, saved_obj.name, "name is not saved correctly")

