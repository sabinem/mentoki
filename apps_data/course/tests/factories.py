# coding: utf-8

from __future__ import unicode_literals, absolute_import

from ..models import Course, CourseOwner, Lesson, Material
from authentication.factories import AccountFactory

import factory

class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course


class CourseOwnerFactory(factory.DjangoModelFactory):
    class Meta:
        model = CourseOwner
    account = factory.SubFactory(AccountFactory)
    course = factory.SubFactory(CourseFactory)
    rank = 1

class UserWith2GroupsFactory(AccountFactory):
    ownership1 = factory.RelatedFactory(CourseOwner, 'account', course__title='title1')
    ownership2 = factory.RelatedFactory(CourseOwner, 'account', course__title='title2')


class LessonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Lesson


class MaterialFactory(factory.DjangoModelFactory):
    class Meta:
        model = Material

