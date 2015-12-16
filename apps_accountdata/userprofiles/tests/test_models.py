"""
Tests of Custom User Model
"""

# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.test import TestCase
from django.db import IntegrityError

from apps_data.course.models.course import CourseOwner
from apps_data.courseevent.models.courseevent import CourseEventParticipation
from ..models import User
from .factories import UserFactory, CourseFactory, CourseEventFactory


class MentorsProfileTest(TestCase):
    """
    Test the Custom User Model
    """
    def setUp(self):
        """
        3 Users and 3 Courses are created
        """
        self.user1 = UserFactory(email='test1@gmail.com',
                                 username='username1',
                                 first_name='vorname1',
                                 last_name='nachname1')
        self.user2 = UserFactory(email='test2@gmail.com',
                                 username='username2',
                                 first_name='vorname2',
                                 last_name='nachname2')
        self.user3 = UserFactory(email='test3@gmail.com',
                                 username='username3',
                                 first_name='vorname3',
                                 last_name='nachname3')
        self.course1 = CourseFactory(slug='slug1')
        self.course2 = CourseFactory(slug='slug2')
        self.course3 = CourseFactory(slug='slug3')
        self.courseevent1 = CourseEventFactory(slug='slug1',course=self.course1)
        self.courseevent2 = CourseEventFactory(slug='slug2',course=self.course2)
        self.courseevent3 = CourseEventFactory(slug='slug3',course=self.course1)
        self.ownership1 = CourseOwner(course=self.course1, user=self.user1)
        self.ownership1.save()
        self.ownership2 = CourseOwner(course=self.course1, user=self.user2)
        self.ownership2.save()
        self.ownership3 = CourseOwner(course=self.course2, user=self.user2)
        self.ownership3.save()
        self.participation1 = CourseEventParticipation(
            courseevent=self.courseevent1, user=self.user1)
        self.participation1.save()
        self.participation2 = CourseEventParticipation(
            courseevent=self.courseevent3, user=self.user1)
        self.participation2.save()
        self.participation3 = CourseEventParticipation(
            courseevent=self.courseevent2, user=self.user3)
        self.participation3.save()
        self.participation4 = CourseEventParticipation(
            courseevent=self.courseevent3, user=self.user3)
        self.participation4.save()


    def test_get_short_name(self):
        """
        The shortname of a User is his first name: user1 has shortname vorname1
        """
        self.assertEquals(self.user1.get_short_name(), 'vorname1')

    def test_get_full_name(self):
        """
        The fullname of a User is his firstname and his lastname seperated by a
        blank
        """
        self.assertEquals(self.user1.get_full_name(), 'vorname1 nachname1')

    def test_teaching(self):
        """
        What Courses does a user teach?
        user1 teaches course1
        user2 teaches course1 and course2
        user3 teaches nothing
        """
        self.assertQuerysetEqual(self.user1.teaching(),
                                 [repr(self.course1)],
                                 ordered=False)
        self.assertQuerysetEqual(self.user2.teaching(),
                                 [repr(self.course1),
                                  repr(self.course2)],
                                 ordered=False)
        self.assertQuerysetEqual(self.user3.teaching(),
                                 [],
                                 ordered=False)
    def test_studying(self):
        """
        What Courses does a user study?
        user1 studies courseevent1 and courseevent3
        user2 studies nothing
        user3 studies courseevent2 and courseevent3
        """
        self.assertQuerysetEqual(self.user1.studying(),
                                 [repr(self.courseevent1),
                                  repr(self.courseevent3)],
                                 ordered=False)
        self.assertQuerysetEqual(self.user2.studying(),
                                 [],
                                 ordered=False)
        self.assertQuerysetEqual(self.user3.studying(),
                                 [repr(self.courseevent2),
                                  repr(self.courseevent3)],
                                 ordered=False)

    def test_create_user(self):
        """
        create a regular user with username, email, first and lastname.
        Check whether the databasecount of users is raised one afterwards.
        :return:
        """
        usercount = User.objects.all().count()
        User.objects.create_user(
            username='username4',
            email='test4@gmail.com',
            first_name='vorname4',
            last_name='nachname4',
            password=None)
        usercount_after = usercount + 1
        self.assertEquals(User.objects.all().count(), usercount_after)

    def test_create_user_username_required(self):
        """
        creating user without username should not be allowed
        """
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email='test5@gmail.com',
                username='',
                first_name='vorname5',
                last_name='nachname5',
                password=None)

    def test_create_user_email_required(self):
        """
        creating user without email is not allowed
        """
        with self.assertRaises(ValueError):
            User.objects.create_user(
                username='username5',
                email='',
                first_name='vorname5',
                last_name='nachname5',
                password=None)

    def test_no_double_user_email(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username='username5',
                email='test1@gmail.com',
                first_name='vorname5',
                last_name='nachname5',
                password=None)

    def test_no_double_username(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username='username1',
                email='test5@gmail.com',
                first_name='vorname5',
                last_name='nachname5',
                password=None)
