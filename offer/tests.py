import tempfile
from http import HTTPStatus
from django.test import TestCase
from demosite.tests import SortAssert
from offer.models import OfferItem


class OfferTests(TestCase):

    def addOfferItem(self, order=0):
        offer_item = OfferItem(
            title="Title",
            text="text",
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            image_alt="main_image_alt",
            element_order=order
        )
        offer_item.save()

    def setUp(self):
        self.baseUrl = "/offer/"

    def test_offer_page_loaded(self):
        response = self.client.get(self.baseUrl, secure=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_offer_elements_are_in_correct_order(self):
        # Arrange
        self.addOfferItem(0)
        self.addOfferItem(2)
        self.addOfferItem(1)
        # Act
        response = self.client.get(self.baseUrl, secure=True)
        # Assert
        SortAssert(response, 'offers').checkOrderOfElements()

    def test_offer_elements_with_the_same_order_number_are_correct_ordered(self):
        # Arrange
        self.addOfferItem(6)
        self.addOfferItem(6)
        self.addOfferItem(1)
        # Act
        response = self.client.get(self.baseUrl, secure=True)
        # Assert
        SortAssert(response, 'offers').checkOrderOfElements()
