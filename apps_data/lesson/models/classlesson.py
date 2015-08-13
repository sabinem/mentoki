# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.functional import cached_property
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError
from django.db.models import Q

from mptt.models import MPTTModel, TreeForeignKey, TreeManager

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField
from model_utils.choices import Choices

from apps_data.course.models.course import Course
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.material.models.material import Material

from model_utils.managers import QueryManager
from django.db.models import Q

from .base import BaseLesson
from .lesson import Lesson, LessonManager

class ClassLessonManager(LessonManager):

    def copied_lesson_ids(self,courseevent):
        return self.filter(courseevent=courseevent).\
            values_list('original_lesson_id', flat=True)

    def complete_tree_for_courseevent(self, courseevent):
        return self.filter(course=courseevent.course, courseevent=courseevent, level=0).\
            get_descendants(include_self=True).prefetch_related('materials')

    def complete_tree_uncopied(self, courseevent):
        course_blocks = self.filter(course=courseevent.course, level=0).\
            exclude(course=courseevent.course,
                    courseevent=courseevent,
                    level=0)

    def complete_tree_for_course(self, course):
        return self.filter(course=course, level=0).\
            get_descendants(include_self=True).prefetch_related('materials')


    def blocks_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent,
                           level=0).\
                           get_descendants(include_self=True)


    def lessons_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent,
                           level=1,
                           )

    def blocks_for_course(self, course):
        return self.filter(course=course,
                           level=0,
                           )


class ClassLesson(BaseLesson):
    courseevent = models.ForeignKey(CourseEvent)
    original_lesson = models.ForeignKey(Lesson)

    objects = ClassLessonManager()

    class Meta:
        verbose_name = "Kurs-Lektion"
        verbose_name_plural = "Kurs-Lektionen"

    @cached_property
    def courseevent_slug(self):
        return self.courseevent.slug
