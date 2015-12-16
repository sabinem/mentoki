"""
Tests of Forms for Custom User Model
"""

# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.test.client import RequestFactory
from django.db import IntegrityError
from django.conf import settings

from apps_data.course.models.course import CourseOwner
from apps_data.courseevent.models.courseevent import CourseEventParticipation
from ..models import User
from .factories import UserFactory, CourseFactory, CourseEventFactory
from ..forms import CustomUserCreationForm, SignupForm

class CustomUserFormTests(TestCase):
    """
    Test forms for Custom User
    """
    def setUp(self):
        """
        1 User is created
        """
        self.user1 = UserFactory(email='test1@gmail.com',
                                 username='username1',
                                 first_name='vorname1',
                                 last_name='nachname1')
        # A request is needed by some tests
        self.request = RequestFactory()

    def test_custom_user_creation_form_valid(self):
        """
        It should be possible to enter valid data into the form: that
        is email, username and two matching passwords.
        """
        form_data = {'email': 'test2@gmail.com',
                     'username': 'username2',
                     'password1': 'something',
                     'password2': 'something'}
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_passwords_do_not_match(self):
        """
        The form should raise an error, if the user enters
        two passwords that do not match.
        """
        form_data = {'email': 'test2@gmail.com',
                     'username': 'username2',
                     'password1': 'something',
                     'password2': 'somethingelse'}
        form = CustomUserCreationForm(data=form_data)
        self.assertRaises(ValidationError)

    def test_custom_user_creation_no_duplicate_username(self):
        """
        A duplicate username should raise an error
        """
        form_data = {'email': 'test2@gmail.com',
                     'username': 'username1',
                     'password1': 'something',
                     'password2': 'something'}
        form = CustomUserCreationForm(data=form_data)
        self.assertRaises(ValidationError)

    #TODO test does not go through!
    def test_signup_form_signup(self):
        """
        A duplicate username should raise an error
        """
        form_data = {'first_name': 'first_name1',
                     'last_name': 'last_name1'}
        form = SignupForm(data=form_data)
        SignupForm.signup(form, request=self.request,
                          user= self.user1)
        user1 = User.objects.get(user= self.user1)
        self.assertEquals(user1.first_name, 'first_name1')
        self.assertEquals(user1.last_name, 'last_name1')