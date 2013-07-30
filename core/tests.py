"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from core.views import signup
from django.contrib.sessions.models import Session
from django.contrib.auth.models import AnonymousUser
from django.core import mail


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
        self.factory = RequestFactory()

    def test_login_views(self):

        self.client.get(reverse('home'))
        self.client.get(reverse('signin'))
        self.client.get(reverse('forgot_password'))

    def test_signin_model(self):

        user1 = User(username='email')
        user1.set_password('helloworld')
        user1.is_active = True
        user1.save()

        user2 = User(username='email2')
        user2.set_password('helloworld')
        user2.is_active = False
        user2.save()

        #wrong username case
        response1 = self.client.post(reverse('signin'), {'username': 'email', 'password': 'helloworld'})
        self.assertEquals(response1.status_code, 302)
        response2 = self.client.post(reverse('signin'), {'username': 'mail', 'password': 'helloworld'})
        self.assertContains(response2, 'Invalid username')
        #wrong password case

        # No need to check inactive user since they get automatically activated after authenticate
        #response3 = self.client.post(reverse('signin'), {'username': 'email2', 'password': 'helloworld'})
        #self.assertContains(response3, 'Inactive User')
        response4 = self.client.post(reverse('signin'), {'username': 'email', 'password': 'hwlloworld'})
        self.assertContains(response4, 'Invalid username')


    def test_signup_model(self):

        user1 = User(username='user6')
        user1.set_password('helloworld')
        user1.is_active = True
        user1.save()
        response1 = self.client.post(reverse('signup'), {'username': 'user1', 'password': 'newser','password2':'newser', 'first_name': 'soonmo', 'last_name': 'kwon', 'email': 'email@email.com'})
        self.assertContains(response1, 'User with this Username already exists.')
        response1 = self.client.post(reverse('signup'), {'username': 'user7', 'password': 'newser1','password2':'newser', 'first_name': 'soonmo', 'last_name': 'kwon', 'email': 'email@email.com'})
        self.assertContains(response1, 'Your passwords do not match')
        response1 = self.client.post(reverse('signup'), {'username': 'user7', 'password': 'newser','password2':'newser', 'first_name': 'soonmo', 'last_name': 'kwon', 'email': 'emailemail.com'})
        self.assertContains(response1, 'Enter a valid email address.')
        response1 = self.client.post(reverse('signup'), {'username': 'userss', 'password': 'newser','password2':'newser', 'first_name': 'soonmo', 'last_name': 'kwon', 'email': 'email@email.com'})
        self.assertEquals(response1.status_code, 302)

        """
        request = self.factory.post(reverse('signup'), {'username': 'user7', 'password': 'newser','password2':'newser', 'first_name': 'soonmo', 'last_name': 'kwon', 'email': 'email@email.com'})
        request.session = {}
        request.session['expire_date'] = '2013-07-31'
        request.session['cycle_key'] = 5
        response1 = signup(request)
        self.assertEquals(response1.status_code, 302)
        """


        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ['email@email.com'])

