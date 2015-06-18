# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models.query import QuerySet


class CourseEventQuerySet(QuerySet):

    def courseevents_for_course(self, course):
        return self.filter(course=course)

    def courseevents_for_course_slug(self, course_slug):
        return self.select_related('course').filter(course__slug=course_slug)


class CourseEventPubicInformationQuerySet(QuerySet):

    def courseeventinfo_for_slug(self, slug):
        return self.select_related('courseevent').get(courseevent__slug=slug)


class CourseeventUnitPublishQuerySet(QuerySet):

    def published_unit_ids_for_course(self, course):
        return self.select_related('courseevent', 'course').filter(courseevent__course=course).values_list('unit_id', flat=True)
