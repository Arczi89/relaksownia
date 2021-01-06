import tempfile
from http import HTTPStatus

from django.contrib.messages import get_messages
from django.test import TestCase
from demosite.constants import field_required, newsletter_permission_required, incorrect_email_format
from demosite.tests import SortAssert
from main.models import MainConfiguration
from newsletter.models import Newsletter
from .forms import NewsletterFaqForm
from .models import FaqItem, FaqConfiguration


class FaqTests(TestCase):

    def addBasicConfigurations(self):
        main_configuration = MainConfiguration(
            newsletter_info="Newsletter info",
            main_text="Main text"
        )
        main_configuration.save()

        faq_configuration = FaqConfiguration(
            main_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            main_image_alt="main_image_alt"
        )
        faq_configuration.save()

        return main_configuration.pk

    def addFaqItem(self, question, answer, order=0):
        faq_item = FaqItem(
            question_text=question,
            answer_text=answer,
            element_order=order
        )
        faq_item.save()

    def removeMainConfiguration(self):
        obj = MainConfiguration.objects.get(pk=self.mainConfigurationPk)
        obj.delete()

    def setUp(self):
        self.baseUrl = "/faq/"
        self.valid_form_data = {
            "email": "test@test.pl",
            "name": "Jan Kowalski",
            "permission": True
        }
        self.mainConfigurationPk = self.addBasicConfigurations()

    def test_faq_page_with_configuration_loaded(self):
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_faq_page_without_configuration_loaded(self):
        self.removeMainConfiguration()
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_should_message_and_name_and_permission_be_required_fields(self):
        form_data = {
            "email": "",
            "name": "",
            "permission": False
        }
        form = NewsletterFaqForm(data=form_data)

        CorrectFormAssert(self, form).checkFormRequiredFields()

    def test_should_validation_message_be_in_DOM_after_form_submitted(self):
        invalid_form_data = {
            "email": "",
            "name": "",
            "permission": False
        }
        self.addFaqItem("question?", "answer!")

        response = self.client.post(self.baseUrl, data=invalid_form_data)

        FaqTemplateAssert(self, response).checkIfTemplateIsCorrect()

    def test_should_email_has_correct_format(self):
        form_data = {
            "email": "TEST",
            "name": "test"
        }
        form = NewsletterFaqForm(data=form_data)

        CorrectFormAssert(self, form).checkEmailFormat()

    def test_should_display_contact_form(self):
        response = self.client.get(self.baseUrl)
        
        self.assertTrue('form' in response.context, "form should be included in response")

    def test_should_display_faq_items(self):
        question = "question?"
        answer = "answer!"
        self.addFaqItem(question, answer)

        response = self.client.get(self.baseUrl)

        self.assertContains(response, question, 1)
        self.assertContains(response, answer, 1)

    def test_should_return_success_message_on_valid_form_save(self):
        response = self.client.post(self.baseUrl, data=self.valid_form_data)
        
        self.assertEqual(response.resolver_match.route, "faq/", "page should be redirect/reload after save to faq page")
        self.assertEqual(len(list(get_messages(response.wsgi_request))), 1, "success message should be displayed after successfully contact form sent")

    def test_should_contact_data_be_saved_correctly_into_db(self):

        self.client.post(self.baseUrl, data=self.valid_form_data)
        
        saved_obj = Newsletter.objects.get(name=self.valid_form_data['name'])
        self.assertIsNotNone(saved_obj.pk, "object is not created in db")
        self.assertEqual(saved_obj.email, saved_obj.email, "email is not saved correctly")
        self.assertEqual(saved_obj.name, saved_obj.name, "name is not saved correctly")

    def test_elements_are_in_correct_order(self):
        self.addFaqItem("question1", "answer1", 0)
        self.addFaqItem("question2", "answer2", 2)
        self.addFaqItem("question3", "answer3", 1)
        
        response = self.client.get(self.baseUrl)

        SortAssert(response, 'faqs').checkOrderOfElements()

    def test_elements_with_the_same_order_number_are_correct_ordered(self):
        self.addFaqItem("question1", "answer1", 3)
        self.addFaqItem("question2", "answer2", 3)
        self.addFaqItem("question3", "answer3", 2)
        
        response = self.client.get(self.baseUrl)
        
        SortAssert(response, 'faqs').checkOrderOfElements()


class CorrectFormAssert:

    def __init__(self, test, form):
        self.test = test
        self.form = form

    def checkEmailRequired(self):
        self.test.assertIn(field_required, self.form.errors['email'], "email should be required")
        return self

    def checkNameRequired(self):
        self.test.assertIn(field_required, self.form.errors['name'], "name should be required")
        return self

    def checkPermissionRequired(self):
        self.test.assertIn(newsletter_permission_required, self.form.errors['permission'], "permission should be accepted")
        return self

    def isFormValid(self):
        self.test.assertFalse(self.form.is_valid(), "name and email should be required, permision should be accepted")
        return self

    def checkFormRequiredFields(self):
        return self.checkEmailRequired().checkNameRequired().checkPermissionRequired().isFormValid()

    def checkEmailFormat(self):
        self.test.assertIn(incorrect_email_format, self.form.errors['email'])
        self.test.assertFalse(self.form.is_valid(), "email format should be valid")
        return self


class FaqTemplateAssert:

    def __init__(self, test, response):
        self.test = test
        self.response = response

    def checkIfCorrectTemplatesAreUsed(self):
        self.test.assertTemplateUsed(self.response, 'faq.html')
        self.test.assertTemplateUsed(self.response, 'partials/_newsletter.html')
        return self

    def checkIfErrorsAreInDOM(self):
        self.test.assertContains(self.response, field_required, 2)
        self.test.assertContains(self.response, newsletter_permission_required, 1)
        return self

    def checkIfTemplateIsCorrect(self):
        self.checkIfCorrectTemplatesAreUsed().checkIfErrorsAreInDOM()
        return self
