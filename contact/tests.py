from http import HTTPStatus

from django.test import TestCase

from demosite.constants import email_or_phone_required, field_required
from .forms import ContactForm


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
            "attachment_img": "test.jpg",
            "phone": ""
        }
        form1 = ContactForm(data=form_data1)
        self.assertTrue(form1.is_valid(), "form should be valid with correct email, message and name provided")

        # phone variant
        form_data2 = {
            "phone": "500400200",
            "message": "test message",
            "name": "Jan Kowalski",
            "attachment_img": "test.jpg",
            "email": ""
        }
        form2 = ContactForm(data=form_data2)
        self.assertTrue(form2.is_valid(), "form should be valid with correct phone, message and name provided")

    # form should not pass until required fields - input message textarea and name - are not filled
    def test_contact_form_message_and_name_required_fields(self):
        form_data = {
            "email": "test@test.pl",
            "phone": "",
            "message": "",
            "name": "",
            "attachment_img": "test.jpg"
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid(), "name and massage should be required")
        self.assertEqual(form.errors['name'][0], field_required)
        self.assertEqual(form.errors['message'][0], field_required)

    # form should not pass until required fields - email OR phone - are not filled
    def test_contact_form_email_or_message_required(self):
        form_data = {
            "email": "",
            "phone": "",
            "message": "test",
            "name": "test",
            "attachment_img": "test.jpg"
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid(), "phone or email should be provided")
        self.assertEqual(form.errors[0], email_or_phone_required)

    # validation for email should work
    def test_contact_form_email_or_message_required(self):
        form_data = {
            "email": "TEST",
            "phone": "123456789",
            "message": "test",
            "name": "test",
            "attachment_img": "test.jpg"
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid(), "email format should be valid")

    # validation for phone should work
    def test_contact_form_email_or_message_required(self):
        form_data = {
            "email": "TEST",
            "phone": "x234569",
            "message": "test",
            "name": "test",
            "attachment_img": "test.jpg"
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid(), "email format should be valid")

    # attachment should receive only image or pdf format

    # contact form request should be stored in database

    # contact form should be styled correctly
