# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.test import TestCase

from ..models import Course, CourseOwner

from django.test import Client


client = Client()


class CourseCreateTest(TestCase):
    """
    Test the creation of a course
    A Course with the title="title" is created
    """
    def setUp(self):
        pass

    def test_create_course(self):
        """
        Asserts that a course exists after the creation
        """
        self.course = Course(title='title1')
        self.course.save()
        # retrieve: only one newsletter, but no published one
        self.assertEqual(Course.objects.all().count(), 1)


