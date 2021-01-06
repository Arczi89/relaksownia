import tempfile
from http import HTTPStatus

from django.template.loader import render_to_string
from django.test import TestCase



from demosite.tests import SortAssert
from .models import Info, CertItem


class InfoTests(TestCase):

    def addBasicConfigurations(self):
        info_configuration = Info(
            photo=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_alt="main_image_alt",
            description="Lorem ipsum description, test test test"
        )
        info_configuration.save()
        return info_configuration.pk

    def addCertItem(self, image_alt, order=0):
        cert_item = CertItem(
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            image_alt=image_alt,
            element_order=order
        )
        cert_item.save()

    def removeMainConfiguration(self):
        obj = Info.objects.get(pk=self.info_configuration_pk)
        obj.delete()

    def setUp(self):
        self.baseUrl = "/info/"
        self.info_configuration_pk = self.addBasicConfigurations()

    def test_info_page_with_configuration_loaded(self):
        self.addCertItem("certificate 1", 1)
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_info_page_without_configuration_loaded(self):
        self.removeMainConfiguration()
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_elements_are_in_correct_order(self):
        # Arrange
        self.addCertItem("certificate 1", 0)
        self.addCertItem("certificate 2", 2)
        self.addCertItem("certificate 3", 1)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        SortAssert(response, 'certs').checkOrderOfElements()

    def test_elements_with_the_same_order_number_are_correct_ordered(self):
        # Arrange
        self.addCertItem("certificate 1", 7)
        self.addCertItem("certificate 2", 7)
        self.addCertItem("certificate 3", 4)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        SortAssert(response, 'certs').checkOrderOfElements()

    def test_should_all_section_be_visible_in_page(self):
        # Arrange
        template_name = "info.html"
        context = {
            "about_me": "not empty",
            "certs": "not empty"
        }
        # Act
        result = render_to_string(template_name, context)
        # Assert
        self.assertTrue("about-me-container" in result, "there is no 'about me' container on page")
        self.assertTrue("certs-container" in result, "there is no certification container on page")
