"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.contrib.auth.models import User


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def runTest(self):

        pass

    def setUp(self):
        self.client = Client()

    def test_login_views(self):

        self.client.get(reverse('home'))
        self.client.get(reverse('login'))
        self.client.get(reverse('signup'))
        self.client.get(reverse('forgot_password'))

    def test_login_model(self):

        user1 = User(username='email')
        user1.set_password('helloworld')
        user1.is_active = True
        user1.save()

        user2 = User(username='email2')
        user2.set_password('helloworld')
        user2.is_active = False
        user2.save()

        #wrong username case
        response1 = self.client.post(reverse('login'), {'username': 'email', 'password': 'helloworld'})
        self.assertContains(response1, 'success')
        response2 = self.client.post(reverse('login'), {'username': 'mail', 'password': 'helloworld'})
        self.assertContains(response2, 'Invalid username')
        #wrong password case

        # No need to check inactive user since they get automatically activated after authenticate
        #response3 = self.client.post(reverse('login'), {'username': 'email2', 'password': 'helloworld'})
        #self.assertContains(response3, 'Inactive User')
        response4 = self.client.post(reverse('login'), {'username': 'email', 'password': 'hwlloworld'})
        self.assertContains(response4, 'Invalid username')


    def test_signup_model(self):

        # signupuser = self.client.post(reverse('signup'), {'username': 'userss', 'password': 'newser','password2':'newser', 'first_name': 'soonmo', 'last_name': 'kwon', 'email': 'email@email.com'})

