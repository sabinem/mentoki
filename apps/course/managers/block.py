# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models.query import QuerySet


class CourseBlockQuerySet(QuerySet):

    def courseblocks_for_course(self, course):
        return self.filter(course=course)

