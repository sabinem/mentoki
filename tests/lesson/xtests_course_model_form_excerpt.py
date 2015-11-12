# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model

from django.test import TestCase
from django.core.validators import ValidationError

from django.test import Client

from ..forms.course import CourseTeachersChangeForm
from .factories import CourseFactory
from ..models.course import CourseOwner


client = Client()


class TestCourseForm(TestCase):

    def setUp(self):
        self.user1 = get_user_model().objects.create(username='testuser1', first_name="firstname1",
                                                     last_name="lastname1", email="u1@gmail.com")
        self.user2 = get_user_model().objects.create(username='testuser2', first_name="firstname2",
                                                     last_name="lastname2", email="u2@gmail.com")
        self.course1 = CourseFactory.create(title="title", slug="slug")
        ownership1 = CourseOwner(course=self.course1, user=self.user1, display_nr=1, display=True)
        ownership1.save()
        self.excerpt = u'excerpt'
        self.title = u'title'

    def test_course_update_only(self):
        """
        test calling of the form
        """
        with self.assertRaises(ValidationError):
            form = CourseTeachersChangeForm(data={'title': u'title1', 'excerpt': u'excerpt1'}, user=self.user1)

    def test_course_valid_update(self):
        """
        valid update
        """
        form = CourseTeachersChangeForm(instance=self.course1, data={'title': u'title1', 'excerpt': u'excerpt1'}, user=self.user1)
        self.assertTrue(form.is_valid())

    def test_course_update_without_permission(self):
        """
        test calling of the form
        """
        with self.assertRaises(ValidationError):
            form = CourseTeachersChangeForm(instance=self.course1, data={'title': u'title1', 'excerpt': u'excerpt1'}, user=self.user2)

    def test_course_update_no_user_provided(self):
        """
        test calling of the form
        """
        with self.assertRaises(ValidationError):
            form = CourseTeachersChangeForm(instance=self.course1, data={'title': u'title1', 'excerpt': u'excerpt1'})
