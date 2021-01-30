import tempfile
from http import HTTPStatus
from django.test import TestCase
from demosite.tests import SortAssert
from promo.models import PromoItem


class PromoTests(TestCase):

    def addPromoItem(self, order=0):
        promo_item = PromoItem(
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

    def test_promo_elements_are_in_correct_order(self):
        # Arrange
        self.addPromoItem(0)
        self.addPromoItem(2)
        self.addPromoItem(1)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        SortAssert(response, 'promoItems').checkOrderOfElements()

    def test_promo_elements_with_the_same_order_number_are_correct_ordered(self):
        # Arrange
        self.addPromoItem(6)
        self.addPromoItem(6)
        self.addPromoItem(1)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        SortAssert(response, 'promoItems').checkOrderOfElements()
