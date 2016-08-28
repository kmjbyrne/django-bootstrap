import datetime
from django.utils import timezone
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()

	def tearDown(self):
		pass

	def test_index(self):
		url = reverse('index')
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, 200)

	def test_404(self):
		url = '/random_test_url'
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, 404)

	def test_add_new_message(self):
		resp = self.client.get(reverse('add_new_message', args=['hello']))
		self.assertEqual(resp.status_code, 200)
