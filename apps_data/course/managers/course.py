# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class CourseQuerySet(QuerySet):

    def get_course_or_404_from_slug(self, slug):
        return get_object_or_404(self, slug=slug)


class CourseOwnerQuerySet(QuerySet):

    def teaching(self, user):
        return self.filter(user=user)

    def teachers(self, course):
        teachers_ids = self.filter(course=course).select_related('user').values_list('id', flat=True)
        return User.objects.filter(id__in=teachers_ids)




