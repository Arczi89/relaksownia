import tempfile
from http import HTTPStatus

from django.test import TestCase
from main.models import MainConfiguration, MainSliderConfiguration, MainSliderItem, MainBoxItem


class MainPageTests(TestCase):

    def addBasicConfigurations(self):
        main_configuration = MainConfiguration(
            newsletter_info="Newsletter info",
            main_text="Main text"
        )
        main_configuration.save()

        slider_configuration = MainSliderConfiguration(
            change_image_time_ms="300"
        )
        slider_configuration.save()

        return main_configuration.pk

    def addSliderItem(self, order=0):
        slider_item = MainSliderItem(
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            image_alt="main_image_alt",
            visible=True,
            element_order=order
        )
        slider_item.save()

    def addMainBoxItem(self, order=0):
        main_box_item = MainBoxItem(
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            image_alt="main_image_alt",
            header_text="header_text",
            description="description",
            visible=True,
            element_order=order
        )
        main_box_item.save()

    def removeMainConfiguration(self):
        obj = MainConfiguration.objects.get(pk=self.mainConfigurationPk)
        obj.delete()

    def setUp(self):
        self.baseUrl = "/"
        self.mainConfigurationPk = self.addBasicConfigurations()

    def test_main_page_with_configuration_loaded(self):
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_mains_page_without_configuration_loaded(self):
        self.removeMainConfiguration()
        response = self.client.get(self.baseUrl)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_slider_elements_are_in_correct_order(self):
        # Arrange
        self.addSliderItem(0)
        self.addSliderItem(2)
        self.addSliderItem(1)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        self.assertLessEqual(response.context['slider_items'][0].element_order, response.context['slider_items'][1].element_order, "There is wrong order of elements")
        self.assertLessEqual(response.context['slider_items'][1].element_order, response.context['slider_items'][2].element_order, "There is wrong order of elements")

    def test_slider_elements_with_the_same_order_number_are_correct_ordered(self):
        # Arrange
        self.addSliderItem(6)
        self.addSliderItem(6)
        self.addSliderItem(1)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        self.assertLessEqual(response.context['slider_items'][0].element_order, response.context['slider_items'][1].element_order, "There is wrong order of elements")
        self.assertLessEqual(response.context['slider_items'][1].element_order, response.context['slider_items'][2].element_order, "There is wrong order of elements")

    def test_main_box_elements_are_in_correct_order(self):
        # Arrange
        self.addMainBoxItem(3)
        self.addMainBoxItem(9)
        self.addMainBoxItem(2)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        self.assertLessEqual(response.context['containers'][0].element_order, response.context['containers'][1].element_order, "There is wrong order of elements")
        self.assertLessEqual(response.context['containers'][1].element_order, response.context['containers'][2].element_order, "There is wrong order of elements")

    def test_main_box_elements_with_the_same_order_number_are_correct_ordered(self):
        # Arrange
        self.addMainBoxItem(1)
        self.addMainBoxItem(1)
        self.addMainBoxItem(0)
        # Act
        response = self.client.get(self.baseUrl)
        # Assert
        self.assertLessEqual(response.context['containers'][0].element_order, response.context['containers'][1].element_order, "There is wrong order of elements")
        self.assertLessEqual(response.context['containers'][1].element_order, response.context['containers'][2].element_order, "There is wrong order of elements")