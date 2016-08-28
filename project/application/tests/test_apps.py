import datetime
from django.utils import timezone
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from application.apps import ApplicationConfig


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()

	def tearDown(self):
		pass

	def test_application_config(self):
		self.assertEqual(ApplicationConfig.name, 'application')
