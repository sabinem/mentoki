# coding: utf-8

from __future__ import unicode_literals, absolute_import

import random
import string

from django.contrib.auth import get_user_model

from django.test import TestCase

from ..models import CourseEvent

import factory

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
        Course.objects.create(title="title", slug=self.slug)
        self.course = Course.objects.get(slug=self.slug)
        self.user1 = get_user_model().objects.create(username='testuser1', first_name="firstname1", last_name="lastname1")
        self.user2 = get_user_model().objects.create(username='testuser2', first_name="firstname2", last_name="lastname2")
        CourseOwner.objects.create(course=self.course,user=self.user1, display_nr=1, display=True)
        CourseOwner.objects.create(course=self.course,user=self.user2, display_nr=2, display=False)

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

    def test_get_course_or_404_from_slug(self):
        """
        The course should be fetched from the slug
        """
        course = Course.objects.get_course_or_404_from_slug(slug=self.slug)
        self.assertEqual(course, self.course)


    def course_slug(self):
        return self.course.slug

    @cached_property
    def course_title(self):
        return self.course.title

    @cached_property
    def teachers(self):
        return self.course.teachers

    @cached_property
    def teachersrecord(self):
        return self.course.teachersrecord

    @cached_property
    def end_date(self):
        """
        calculate the end date form the startdate and the number of weeks if a startdate is given.
        """
        if self.start_date:
           end_date = self.start_date + datetime.timedelta(days=7*self.nr_weeks)
           return end_date


    @property
    def days_to_start(self):
        today = datetime.date.today()
        try:
            if today < self.start_date:
               # the course has not started yet
               return (self.start_date - today).days
        except:
            return None

