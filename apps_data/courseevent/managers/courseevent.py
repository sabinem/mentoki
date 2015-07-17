# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models.query import QuerySet







class CourseeventUnitPublishQuerySet(QuerySet):

    def published_unit_ids_for_course(self, course):
        return self.select_related('courseevent', 'course').filter(courseevent__course=course).values_list('unit_id', flat=True)
