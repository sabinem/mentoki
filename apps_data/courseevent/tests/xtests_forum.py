# coding: utf-8

from __future__ import unicode_literals, absolute_import

import random
import string

from django.contrib.auth import get_user_model

from django.test import TestCase

from ..models import Course, CourseOwner

import factory

from django.test import Client

from django.core.urlresolvers import reverse

client = Client()


def random_string(length=10):
    return u''.join(random.choice(string.ascii_letters) for x in range(length))

NAME2 = random_string()
NAME2 = random_string()


class CourseOwnerCreateTest(TestCase):
    """
    Test the creation of a courseowner
    For a User: testuser1
    and a Course: with title="title" and slug="slug" a courseowner is created
    """
    def setUp(self):
        self.slug = "slug"
        self.user = get_user_model().objects.create(username='testuser')
        Course.objects.create(title="title", slug=self.slug)
        self.course = Course.objects.get(slug=self.slug)

    def test_create_courseowner(self):
        """
        asserts that one courseowner records exists
        """
        courseowner = CourseOwner(course=self.course, user=self.user)
        courseowner.save()
        self.assertEqual(CourseOwner.objects.all().count(), 1)


class CourseOwnerQuerySetTest(TestCase):
    """
    Tests querysets on the CourseOwner model
    Users: testuser1, testuser2, testuser3
    Courses: course1, course2
    course1 is taught by testuser1, course2 is taught by testuser1 and testuser3
    """
    def setUp(self):
        self.slug1 = "slug1"
        self.slug2 = "slug2"
        self.user1 = get_user_model().objects.create(username='testuser1')
        self.user2 = get_user_model().objects.create(username='testuser2')
        self.user3 = get_user_model().objects.create(username='testuser3')
        self.course1 = Course.objects.create(title="title1", slug=self.slug1)
        self.course2 = Course.objects.create(title="title2", slug=self.slug2)
        CourseOwner.objects.create(course=self.course1, user=self.user1, display_nr=1)
        CourseOwner.objects.create(course=self.course2, user=self.user1, display_nr=2)
        CourseOwner.objects.create(course=self.course2, user=self.user3, display_nr=1)

    def test_queryset_teaching(self):
        """
        expected: user2 is teaching None, user 1 is teaching course1 and course2, and user3 is teaching course2
        """
        self.assertEqual(CourseOwner.objects.teaching(user=self.user1), [self.course1, self.course2])
        self.assertEqual(CourseOwner.objects.teaching(user=self.user2), None)
        self.assertEqual(CourseOwner.objects.teaching(user=self.user3), [self.course2])

    def test_queryset_teachers(self):
        """
        expected: course2 has teachers user3 and user1 in that order
                  course1 has teacher user1
        """
        self.assertEqual(CourseOwner.objects.teachers(course=self.course1), [self.user1])
        self.assertEqual(CourseOwner.objects.teachers(course=self.course2), [self.user3, self.user1])
