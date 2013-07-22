"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client
from expense.models import Item
from django.contrib.auth.models import User
from core.models import Category
from datetime import date


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

    def test_expense_model(self):

        c1 = Category(name='food')
        c2 = Category(name='doctor')
        c3 = Category(name='entertainment')
        c4 = Category(name='ride')
        c1.save()
        c2.save()
        c3.save()
        c4.save()

        u1 = User(username='soonmo kwon', email='kwon@soon.mo', first_name='soonmo', last_name='kwon')
        u1.save()
        u2 = User(username='soonuck kwon', email='kwon@soon.uck', first_name='soonuck', last_name='kwon')
        u2.save()

        item1 = Item(dollar_amount=100.00, team_member=u1, category=c2, activity_date=(date(year=2013, month=7, day=23)))
        item1.save()
        item2 = Item(dollar_amount=52.25, team_member=u2, category=c3, activity_date=(date(year=2013, month=7, day=22)))
        item2.save()