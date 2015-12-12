# coding: utf-8

from __future__ import unicode_literals, absolute_import

import factory

from apps_data.course.models.course import Course
from apps_data.courseevent.models.courseevent import CourseEvent
from ..models import User


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course

class CourseEventFactory(factory.DjangoModelFactory):
    class Meta:
        model = CourseEvent