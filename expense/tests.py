"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client


class SimpleTest(TestCase):

    def runTest(self):

        pass

    def setUp(self):
        self.client = Client()


    def test_loading_views(self):
        """
            We are only testing GET request to views
        """

        self.client.get(reverse('expense_home'))
        self.client.get(reverse('expense_add'))
        self.client.get(reverse('expense_item_add'))
        self.client.get(reverse('expense_download'))
        self.client.get(reverse('expense_category_name_sort', kwargs= {'category_name': 'food'}))
        self.client.get(reverse('expense_category_id_sort', kwargs= {'category_id': '123'}))
        self.client.get(reverse('expense_teammate_name_sort', kwargs={'teammate_name': 'food'}))
        self.client.get(reverse('expense_teammate_id_sort', kwargs={'teammate_id': '123'}))
        self.client.get(reverse('expense_category_name_filter', kwargs={'category_name': 'food'}))
        self.client.get(reverse('expense_category_id_filter', kwargs={'category_id': '123'}))
        self.client.get(reverse('expense_teammate_name_filter', kwargs={'teammate_name': 'food'}))
        self.client.get(reverse('expense_teammate_id_filter', kwargs={'teammate_id': '123'}))