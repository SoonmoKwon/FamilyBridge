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
        We are only testing GET request views
        """

        self.client.get(reverse('calendar_home'))
        self.client.get(reverse('calendar_add'))
        self.client.get(reverse('calendar_activity_add'))
        self.client.get(reverse('calendar_download'))
        self.client.get(reverse('calendar_dayplan', kwargs = {'day': '03102013'}))
        self.client.get(reverse('calendar_weekplan', kwargs = {'day': '03102013'}))