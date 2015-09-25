# coding: utf-8

from __future__ import unicode_literals, absolute_import

import random
import string

from django.contrib.auth import get_user_model

from django.test import TestCase

from ..models.courseevent import CourseEvent
from ..models.menu import ClassroomMenuItem
from .factories import CourseEventFactory
from apps_data.course.tests.factories import CourseFactory


from django.test import Client

from django.core.urlresolvers import reverse

client = Client()


class MenuItemCleanTest(TestCase):
    """
    Test the creation of a menuitem
    A Menuitem with the display_title="title1" and the display_nr 1 and
    item-type "header" is created
    """
    def setUp(self):
        self.courseevent1_slug = 'ceslug1'
        self.course = CourseEventFactory.create(title="cetitle1",
                                                slug=self.courseevent1_slug)
        self.courseevent2_slug = 'ceslug2'
        self.course = CourseEventFactory.create(title="cetitle2",
                                                slug=self.courseevent2_slug)

    def test_create_classroommenuitem(self):
        """
        Asserts that a menuitem can be created with just title, nr and item_type given
        """
        self.classroommenuitem = ClassroomMenuItem(display_title='menu1',
                                                   display_nr=1,
                                                   item_type='header')
        self.classroommenuitem.save()
        # retrieve: only one menu item
        self.assertEqual(ClassroomMenuItem.objects.all().count(), 1)


class MenuItemAttributesTest(TestCase):
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
        self.course_slug = 'cslug'
        self.course = CourseFactory.create(title="ctitle",
                                           slug=self.course_slug)
        self.courseevent_slug = 'ceslug1'
        self.courseevent_slug = 'ceslug2'
        self.course = CourseEventFactory.create(title="cetitle",
                                                slug=self.courseevent_slug)
        self.courseevent = CourseEventFactory.create(title="title", slug=self.slug)
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