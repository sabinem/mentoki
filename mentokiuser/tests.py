# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model

from django.test import TestCase

from apps_data.course.tests import CourseFactory
from apps_data.course.models import CourseOwner

from .factories import AccountFactory

from django.test import Client


client = Client()


class AccountAttributesTest(TestCase):
    """
    Tests custom methods and attributes of Account
    """
    def setUp(self):
        """
        Courses are created: course1
                             course2

        Users are created: testuser1
                           testuser2
                           testuser3
        testuser1 and testuser2 are both declared teachers of course1:
        testuser1 is teacher of Course2
        """
        self.course1 = CourseFactory.create(title="title1")
        self.course2 = CourseFactory.create(title="title2")
        self.user1 = get_user_model().objects.create(username='testuser1', first_name="firstname1", last_name="lastname1", email="u1@gmail.com")
        self.user2 = get_user_model().objects.create(username='testuser2', first_name="firstname2", last_name="lastname2", email="u2@gmail.com")
        self.user3 = get_user_model().objects.create(username='testuser3', first_name="firstname3", last_name="lastname3", email="u3@gmail.com")
        ownership1 = CourseOwner(course=self.course1, user=self.user1)
        ownership1.save()
        ownership2 = CourseOwner(course=self.course1, user=self.user2)
        ownership2.save()
        ownership3 = CourseOwner(course=self.course2, user=self.user1)
        ownership3.save()

    def test_account_property_teaching(self):
        """
        Course1 and Course2 are taught by User3, Course1 is also taught by User1, User2 is not teaching so far
        """
        self.assertQuerysetEqual(self.user1.teaching().order_by('title'), [repr(self.course1), repr(self.course2)])
        self.assertQuerysetEqual(self.user2.teaching(), [repr(self.course1)])
        self.assertQuerysetEqual(self.user3.teaching(), [])

    def test_course_property_has_ownership(self):
        """
        Teachers should be the user records in the appropriate order
        """
        self.assertEqual(self.user1.has_ownership(self.course1), True)
        self.assertEqual(self.user1.has_ownership(self.course2), True)
        self.assertEqual(self.user2.has_ownership(self.course1), True)
        self.assertEqual(self.user2.has_ownership(self.course2), False)
        self.assertEqual(self.user3.has_ownership(self.course1), False)
        self.assertEqual(self.user3.has_ownership(self.course2), False)

