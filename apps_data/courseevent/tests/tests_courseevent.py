# coding: utf-8

from __future__ import unicode_literals, absolute_import

import random
import string

from django.contrib.auth import get_user_model

from django.test import TestCase

from ..models.courseevent import CourseEvent
from .factories import CourseEventFactory
from apps_data.course.tests.factories import CourseFactory, CourseOwnerFactory


from django.test import Client

from django.core.urlresolvers import reverse

client = Client()


class CourseEventCreateTest(TestCase):
    """
    Test the creation of a course
    A Course with the title="title" is created
    """
    def setUp(self):
        pass

    def test_create_courseevent(self):
        """
        Asserts that a course exists after the creation
        """
        self.course = CourseEvent(title='title1')
        self.course.save()
        # retrieve: only one newsletter, but no published one
        self.assertEqual(CourseEvent.objects.all().count(), 1)


class CourseEventAttributesTest(TestCase):
    """
    Test the methods and attributes of courseevent
    """
    def setUp(self):
        """
        A Course is created: title = "title", slug = "slug"
        Users are created: testuser1: "firstname1 lastname1"
                           testuser2: "firstname2 lastname2"
        The Users are both declared to teachers of the course: testuser1 being the main teacher is displayed
        first and full. Whereas teacher2 is the assistant teacher appearing second.
        """
        self.slug = "slug"
        self.course = CourseFactory.create(title="title", slug=self.slug)
        self.user1 = get_user_model().objects.create(username='testuser1', first_name="firstname1", last_name="lastname1")
        self.user2 = get_user_model().objects.create(username='testuser2', first_name="firstname2", last_name="lastname2")
        CourseOwnerFactory.create(course=self.course,user=self.user1, display_nr=1, display=True)
        CourseOwnerFactory.create(course=self.course,user=self.user2, display_nr=2, display=False)

    def test_courseevent_property_course_slug(self):
        """
        Test course_slug, expected: self.slug
        """
        self.assertEqual(self.course_slug, self.slug)

    def test_courseevent_property_course_title(self):
        """
        Test course_slug, expected: "title"
        """
        self.assertEqual(self.course_title, "title")

    def test_course_property_teachersrecord(self):
        """
        Teachers should be showed as a record with main teacher appearing first
        """
        self.assertEqual(self.course.teachersrecord, "firstname1 lastname1 und firstname2 lastname2")

    def test_course_property_teachers(self):
        """
        Teachers should be the user records in the appropriate order
        """
        self.assertEqual(self.course.teachers, [self.user1, self.user2])