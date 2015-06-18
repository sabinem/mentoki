# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models.query import QuerySet


class LessonQuerySet(QuerySet):

    def lessons_for_course(self, course):
        return self.filter(course=course)

    def get_next_sibling_within_course(self, course, lesson):
        next = lesson.get_next_sibling()
        try:
            if next.course_id == course.id:
                return next
            else:
                next = None
        except:
            pass

        return next

    def get_previous_sibling_within_course(self, course, lesson):
        previous = lesson.get_previous_sibling()
        try:
            if previous.course_id == course.id:
                return previous
            else:
                next = None
        except:
            pass

        return previous