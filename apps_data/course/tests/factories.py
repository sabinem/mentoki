# coding: utf-8

from __future__ import unicode_literals, absolute_import

from ..models.course import Course


import factory

class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course


