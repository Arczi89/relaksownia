from http import HTTPStatus

from django.test import TestCase

from policy.models import PolicyConfiguration


class PolicyTests(TestCase):

    def addBasicConfigurations(self):
        policy_configuration = PolicyConfiguration(
            privacy_text="Lorem ipsum description, test test test",
            order_rules="Lorem ipsum description, test test test"
        )
        policy_configuration.save()
        return policy_configuration.pk

    def removeMainConfiguration(self):
        obj = PolicyConfiguration.objects.get(pk=self.policy_configuration_pk)
        obj.delete()

    def setUp(self):
        self.baseUrl = "/policy/"
        self.policy_configuration_pk = self.addBasicConfigurations()

    def test_policy_page_with_configuration_loaded(self):
        response = self.client.get(self.baseUrl, secure=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_policy_page_without_configuration_loaded(self):
        self.removeMainConfiguration()
        response = self.client.get(self.baseUrl, secure=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

