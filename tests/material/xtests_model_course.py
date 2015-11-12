# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model

from django.test import TestCase

from ..models.course import Course, CourseOwner
from .factories import CourseFactory


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


class CourseAttributesTest(TestCase):
    """
    Test the methods and attributes of course
    """
    def setUp(self):
        """
        A Course is created: title = "title", slug = "slug"
        Users are created: testuser1: "firstname1 lastname1"
                           testuser2: "firstname2 lastname2"
                           testuser3: "firstname3 lastname3"
        The testuser1 and testuser2 are both declared to teachers of the course: testuser1 being the main teacher is displayed
        first and full. Whereas teacher2 is the assistant teacher appearing second. testuser3 stays unassigned.
        """
        self.slug = "slug"
        self.course = CourseFactory.create(title="title", slug=self.slug)
        self.user1 = get_user_model().objects.create(username='testuser1', first_name="firstname1", last_name="lastname1", email="u1@gmail.com")
        self.user2 = get_user_model().objects.create(username='testuser2', first_name="firstname2", last_name="lastname2", email="u2@gmail.com")
        self.user3 = get_user_model().objects.create(username='testuser3', first_name="firstname3", last_name="lastname3", email="u3@gmail.com")
        ownership1 = CourseOwner(course=self.course, user=self.user1, display_nr=1, display=True)
        ownership1.save()
        ownership2 = CourseOwner(course=self.course, user=self.user2, display_nr=2, display=False)
        ownership2.save()

    def test_course_property_teachersrecord(self):
        """
        Teachers should be showed as a record with main teacher appearing first
        """
        self.assertEqual(self.course.teachersrecord, "firstname1 lastname1 und firstname2 lastname2")

    def test_course_property_teachers(self):
        """
        Teachers should be the user records in the appropriate order
        """
        self.assertQuerysetEqual(self.course.teachers, [repr(self.user1), repr(self.user2)])

    def test_course_property_is_owner(self):
        """
        Teachers should be the user records in the appropriate order
        """
        self.assertEqual(self.course.is_owner(self.user1), True)
        self.assertEqual(self.course.is_owner(self.user2), True)
        self.assertEqual(self.course.is_owner(self.user3), False)

    def test_get_course_or_404_from_slug(self):
        """
        The course should be fetched from the slug
        """
        course = Course.objects.get_course_or_404_from_slug(slug=self.slug)
        self.assertEqual(course, self.course)

