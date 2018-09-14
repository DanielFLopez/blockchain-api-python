from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from api.models import Block


class SetZeroAccountUpdateViewSetTest(TestCase):
    fixtures = ['initial_data']

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('api:initialize-detail', kwargs={'pk': 1})

    def tearDown(self):
        del self.client
        del self.url

    def test_put_status_400(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, 400)

    def test_put_status_200(self):
        Block.block_manager.create_initial_block()
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, 200)


class TransactionAccountUpdateViewSetTest(TestCase):
    fixtures = ['initial_data']

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('api:transaction-detail', kwargs={'pk': 1})
        self.data = {'value': 10}

    def tearDown(self):
        del self.client
        del self.url
        del self.data

    def test_put_status_400(self):
        response = self.client.put(self.url, data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_put_status_200(self):
        Block.block_manager.create_initial_block()
        response = self.client.put(self.url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_put_status_400_not_funds(self):
        self.data = {'value': -1000}
        Block.block_manager.create_initial_block()
        response = self.client.put(self.url, data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_put_status_400_value_error(self):
        self.data = {'value': "menos uno"}
        response = self.client.put(self.url, data=self.data)
        self.assertEqual(response.status_code, 400)


class BlockTransactionsListViewTest(TestCase):
    fixtures = ['initial_data']

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('api:block-list')

    def tearDown(self):
        del self.client
        del self.url

    def test_put_status_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
