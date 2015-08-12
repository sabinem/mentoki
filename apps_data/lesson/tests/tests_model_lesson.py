# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.test import TestCase

from ..models.course import Course, CourseOwner
from ..models.lesson import Lesson
from .factories import CourseFactory

from django.contrib.auth import get_user_model


class LessonAttributesTest(TestCase):
    """
    Test the methods and attributes of lessons
    """
    def setUp(self):
        """
        two courses are set up with lessons:

        the first course has a tree of: lesson 1
                                   and: lesson 2 - lesson 3 - lesson 4
        the second course has a tree of : lesson 5 - lesson 6 - lesson 7
        """
        slug1 = "slug1"
        self.course1 = CourseFactory.create(title="title1", slug=slug1)
        slug2 = "slug2"
        self.course2 = CourseFactory.create(title="title2", slug=slug2)
        self.user1 = get_user_model().objects.create(username='testuser1', first_name="firstname1", last_name="lastname1", email="u1@gmail.com")
        self.user2 = get_user_model().objects.create(username='testuser2', first_name="firstname2", last_name="lastname2", email="u2@gmail.com")
        self.user3 = get_user_model().objects.create(username='testuser3', first_name="firstname3", last_name="lastname3", email="u3@gmail.com")
        ownership1 = CourseOwner(course=self.course1, user=self.user1)
        ownership1.save()
        ownership2 = CourseOwner(course=self.course2, user=self.user3)
        ownership2.save()

        lesson1 = Lesson(course=self.course1,nr=1, title="title1")
        lesson1.insert_at(None)
        lesson1.save()
        self.lesson1 = Lesson.objects.get(title="title1")

        lesson2 = Lesson(course=self.course1,nr=2, title="title2")
        lesson2.insert_at(None)
        lesson2.save()
        self.lesson2 = Lesson.objects.get(title="title2")

        lesson3 = Lesson(course=self.course1,nr=1, title="title3")
        lesson3.insert_at(self.lesson2)
        lesson3.save()
        self.lesson3 = Lesson.objects.get(title="title3")

        lesson4 = Lesson(course=self.course1,nr=1, title="title4")
        lesson4.insert_at(self.lesson3)
        lesson4.save()
        self.lesson4 = Lesson.objects.get(title="title4")

        lesson5 = Lesson(course=self.course2,nr=1, title="title5")
        lesson5.insert_at(None)
        lesson5.save()
        self.lesson5 = Lesson.objects.get(title="title5")

        lesson6 = Lesson(course=self.course2,nr=2, title="title6")
        lesson6.insert_at(self.lesson5)
        lesson6.save()
        self.lesson6 = Lesson.objects.get(title="title6")

        lesson7 = Lesson(course=self.course2,nr=1, title="title7")
        lesson7.insert_at(self.lesson6)
        lesson7.save()
        self.lesson7 = Lesson.objects.get(title="title7")

        Lesson.objects.rebuild()

    def test_method_get_next_sibling(self):
        """
        test that siblings are only fetched within the same course
        """
        self.assertEqual(self.lesson5.get_next_sibling(), None)
        self.assertEqual(self.lesson1.get_next_sibling(), self.lesson2)

    def test_method_get_previous_sibling(self):
        """
        test that siblings are only fetched within the same course
        """
        self.assertEqual(self.lesson5.get_previous_sibling(), None)
        self.assertEqual(self.lesson2.get_previous_sibling(), self.lesson1)

    def test_property_is_block(self):
        """
        test that siblings are only fetched within the same course
        """
        self.assertEqual(self.lesson5.is_block, True)
        self.assertEqual(self.lesson6.is_block, False)
        self.assertEqual(self.lesson7.is_block, False)

    def test_property_is_lesson(self):
        """
        test that siblings are only fetched within the same course
        """
        self.assertEqual(self.lesson5.is_lesson, False)
        self.assertEqual(self.lesson6.is_lesson, True)
        self.assertEqual(self.lesson7.is_lesson, False)

    def test_property_is_lesson_step(self):
        """
        test that siblings are only fetched within the same course
        """
        self.assertEqual(self.lesson5.is_step, False)
        self.assertEqual(self.lesson6.is_step, False)
        self.assertEqual(self.lesson7.is_step, True)

    def test_lesson_property_is_owner(self):
        """
        User should be teacher of the course
        """
        self.assertEqual(self.lesson1.is_owner(self.user1), True)
        self.assertEqual(self.lesson6.is_owner(self.user3), True)
        self.assertEqual(self.lesson2.is_owner(self.user3), False)