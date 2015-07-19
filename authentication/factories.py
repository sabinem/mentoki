# coding: utf-8

from __future__ import unicode_literals, absolute_import

from ..models import Course, CourseOwner, Lesson, Material

import factory

class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course


class CourseOwnerFactory(factory.DjangoModelFactory):
    class Meta:
        model = CourseOwner


class LessonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Lesson


class MaterialFactory(factory.DjangoModelFactory):
    class Meta:
        model = Material


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'Account'
        django_get_or_create = ('username',)

    username = 'john'