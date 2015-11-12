# coding: utf-8

from __future__ import unicode_literals, absolute_import

from ..models.lesson import Lesson
from ..models.classlesson import ClassLesson

import factory


class LessonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Lesson


class ClassLessonFactory(factory.DjangoModelFactory):
    class Meta:
        model = ClassLesson

