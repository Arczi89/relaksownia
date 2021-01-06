import tempfile
from http import HTTPStatus

from django.test import TestCase

from demosite.tests import SortAssert
from opinions.models import OpinionItem, OpinionTreeItem


class OpinionTests(TestCase):

    def addOpinionItem(self, order=0):
        opinion_item = OpinionItem(
            opinion_text="opinion_text",
            customer_name="customer_name",
            element_order=order
        )
        opinion_item.save()

    def addOpinionTreeItem(self, order=0):
        opinion_tree_item = OpinionTreeItem(
            text="text",
            img=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            element_order=order
        )
        opinion_tree_item.save()

    def setUp(self):
        self.baseUrl = "/opinions/"

    def test_opinion_page_loaded(self):
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_opinion_elements_are_in_correct_order(self):
        # Arrange
        self.addOpinionItem(0)
        self.addOpinionItem(3)
        self.addOpinionItem(1)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        SortAssert(response, 'opinions').checkOrderOfElements()

    def test_opinion_elements_with_the_same_order_number_are_correct_ordered(self):
        # Arrange
        self.addOpinionItem(1)
        self.addOpinionItem(1)
        self.addOpinionItem(0)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        SortAssert(response, 'opinions').checkOrderOfElements()

    def test_opinion_tree_elements_are_in_correct_order(self):
        # Arrange
        self.addOpinionTreeItem(0)
        self.addOpinionTreeItem(2)
        self.addOpinionTreeItem(1)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        SortAssert(response, 'opinion_tree').checkOrderOfElements()

    def test_opinion_tree_elements_with_the_same_order_number_are_correct_ordered(self):
        # Arrange
        self.addOpinionTreeItem(7)
        self.addOpinionTreeItem(7)
        self.addOpinionTreeItem(2)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        SortAssert(response, 'opinion_tree').checkOrderOfElements()
