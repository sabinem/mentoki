# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models.query import QuerySet


class MaterialQuerySet(QuerySet):

    def materials_for_course(self, course):
        return self.filter(course=course)

    def materials_for_lesson(self, lesson):
        return self.filter(lesson=lesson)