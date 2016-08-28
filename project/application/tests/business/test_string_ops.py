import datetime
from django.utils import timezone
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from application.business.string_ops import *

class TestViews(TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_reverse_string(self):
		string = 'TEST'
		reverse_str = 'TSET'
		self.assertEqual(reverse_string(string), reverse_str)
		self.assertEqual(reverse_string(''), '')
		self.assertEqual(reverse_string(), '')

		with self.assertRaises(ValueError):
			reverse_string([])


