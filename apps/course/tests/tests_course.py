# coding: utf-8

from __future__ import unicode_literals, absolute_import

import random
import string

from django.contrib.auth import get_user_model

from django.test import TestCase

from ..models import Course


def random_string(length=10):
    return u''.join(random.choice(string.ascii_letters) for x in range(length))


class CourseCreateTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')

    def test_create_course(self):
        # create unpublished newsletter
        course = Course(title='Title Me', slug='titleme')
        course.save()
        # retrieve: only one newsletter, but no published one
        self.assertEqual(Course.objects.all().count(), 1)