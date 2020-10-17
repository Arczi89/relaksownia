from http import HTTPStatus

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from demosite.constants import email_or_phone_required, field_required, incorrect_email_format, incorrect_phone_format, incorrect_extension
from .forms import ContactForm

import tempfile


class ContactRequestTests(TestCase):
    baseUrl = "/contact/"

    # contact page should be loaded
    def test_contact_page_loaded(self):
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # form should pass when all required fields are filled
    def test_contact_all_required_fields(self):
        # email variant
        form_data1 = {
            "email": "test@test.pl",
            "message": "test message",
            "name": "Jan Kowalski",
            "attachment_img": tempfile.NamedTemporaryFile(suffix=".jpg").name,
            "phone": ""
        }
        form1 = ContactForm(data=form_data1)
        self.assertEqual(len(form1.errors), 0, "form should not have errors")
        self.assertTrue(form1.is_valid(), "form should be valid with correct email, message and name provided")

        # phone variant
        form_data2 = {
            "phone": "500400200",
            "message": "test message",
            "name": "Jan Kowalski",
            "attachment_img": tempfile.NamedTemporaryFile(suffix=".jpg").name,
            "email": ""
        }
        form2 = ContactForm(data=form_data2)
        self.assertEqual(len(form2.errors), 0, "form should not have errors")
        self.assertTrue(form2.is_valid(), "form should be valid with correct phone, message and name provided")

    # form should not pass until required fields - input message textarea and name - are not filled
    def test_contact_form_message_and_name_required_fields(self):
        form_data = {
            "email": "test@test.pl",
            "phone": "",
            "message": "",
            "name": "",
            "attachment_img": tempfile.NamedTemporaryFile(suffix=".jpg").name
        }
        form = ContactForm(data=form_data)

        self.assertIn(field_required, form.errors['name'])
        self.assertIn(field_required, form.errors['message'])
        self.assertFalse(form.is_valid(), "name and massage should be required")

    # form should not pass until required fields - email OR phone - are not filled
    def test_contact_form_email_or_message_required(self):
        form_data = {
            "email": "",
            "phone": "",
            "message": "test",
            "name": "test",
            "attachment_img": tempfile.NamedTemporaryFile(suffix=".jpg").name
        }
        form = ContactForm(data=form_data)
        self.assertIn(email_or_phone_required, form.errors['__all__'])
        self.assertFalse(form.is_valid(), "phone or email should be provided")

    # validation for email should work
    def test_contact_form_email_format(self):
        form_data = {
            "email": "TEST",
            "phone": "123456789",
            "message": "test",
            "name": "test",
            "attachment_img": tempfile.NamedTemporaryFile(suffix=".jpg").name
        }
        form = ContactForm(data=form_data)
        self.assertIn(incorrect_email_format, form.errors['email'])
        self.assertFalse(form.is_valid(), "email format should be valid")

    # validation for phone should work
    def test_contact_form_phone_format(self):
        form_data1 = {
            "email": "TEST@TEST.pl",
            "phone": "x234w5629",
            "message": "test",
            "name": "test",
            "attachment_img": tempfile.NamedTemporaryFile(suffix=".jpg").name
        }
        form1 = ContactForm(data=form_data1)
        self.assertIn(incorrect_phone_format, form1.errors['__all__'])
        self.assertFalse(form1.is_valid(), "phone format should have only digits")

        form_data2 = {
            "email": "TEST@TEST.pl",
            "phone": "x234w5629",
            "message": "test",
            "name": "test",
            "attachment_img": tempfile.NamedTemporaryFile(suffix=".jpg").name
        }
        form2 = ContactForm(data=form_data2)
        self.assertIn(incorrect_phone_format, form2.errors['__all__'])
        self.assertFalse(form2.is_valid(), "phone format should have 9 digits")

    # TODO fix
    # attachment should receive only image or pdf format
    # def test_contact_form_attachment_format(self):
    #     form_data1 = {
    #         "email": "TEST@TEST.pl",
    #         "phone": "500400200",
    #         "message": "test",
    #         "name": "test",
    #         "attachment_img": tempfile.NamedTemporaryFile(suffix=".doc").name
    #     }
    #     form1 = ContactForm(data=form_data1)
    #     self.assertIn(incorrect_extension, form1.errors['attachment_img'])
    #     self.assertFalse(form1.is_valid(), "attachment img should not pass .doc")
    #
    #     form_data2 = {
    #         "email": "TEST@TEST.pl",
    #         "phone": "500400200",
    #         "message": "test",
    #         "name": "test",
    #         "attachment_img": tempfile.NamedTemporaryFile(suffix=".png").name
    #     }
    #
    #     form = ContactForm(data=form_data2)
    #     self.assertEqual(len(form.errors), 0, "form should not have errors")
    #     self.assertTrue(form.is_valid(), "attachment img should pass .png")

    # contact form request should be stored in database

    # contact form should be styled correctly
