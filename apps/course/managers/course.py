# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models.query import QuerySet
from django.contrib.auth.models import User



class CourseOwnerQuerySet(QuerySet):

    def teaching(self, user):
        return self.filter(user=user)

    def teachers(self, course):
        return self.filter(course=course).select_related('user')


