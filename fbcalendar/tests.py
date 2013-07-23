"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.contrib.auth.models import User
from fbcalendar.models import Activity
from core.models import Category
from datetime import date, datetime


class SimpleTest(TestCase):
    def runTest(self):
        pass

    def setUp(self):
        self.client = Client()

    def test_loading_views(self):
        """
        We are only testing GET request views
        """

        self.client.get(reverse('calendar_home')) # 주어진 url에서 제대로 동작하는지.
        self.client.get(reverse('calendar_add'))
        self.client.get(reverse('calendar_activity_add'))
        self.client.get(reverse('calendar_download'))
        self.client.get(reverse('calendar_dayplan', kwargs = {'day': '03102013'}))
        self.client.get(reverse('calendar_weekplan', kwargs = {'day': '03102013'}))

    def test_calendar_model(self):
        c1 = Category(name = "food")
        c2 = Category(name = "doctor")
        c3 = Category(name = "entertainment")
        c1.save()
        c2.save()
        c3.save()
        u1 = User(username = "member1", email = "member1@gmail.com", first_name = "Member", last_name = "One")
        u1.save()
        d1 = datetime(year = 2013, month = 7, day = 22, hour = 5, minute = 50)
        d2 = datetime(year = 2013, month = 7, day = 22, hour = 7, minute = 50)
        d3 = datetime(year = 2013, month = 7, day = 22, hour = 9, minute = 50)
        a1 = Activity(team_member = u1, description = "grocery shopping", category = c1, start_time = d1, end_time = d2)
        a2 = Activity(team_member = u1, description = "hospital", category = c2, start_time = d2, end_time = d3)
        a3 = Activity(team_member = u1, description = "niagara falls", category = c3, start_time = d1, end_time = d3)
        a1.save()
        a2.save()
        a3.save()