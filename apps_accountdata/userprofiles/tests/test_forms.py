"""
Tests of Forms for Custom User Model
"""

# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from apps_data.course.models.course import CourseOwner
from apps_data.courseevent.models.courseevent import CourseEventParticipation
from ..models import User
from .factories import UserFactory, CourseFactory, CourseEventFactory
from ..forms import UserCreationForm


from ..forms import CustomUserCreationForm

class CustomUserFormTests(TestCase):
    """
    Test forms for Custom User
    """
    def test_custom_user_creation_form_passwords_do_not_match(self):
        form_data = {'email': 'test1@gmail.com',
                     'username': 'username1',
                     'password1': 'something',
                     'password2': 'something'}
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
