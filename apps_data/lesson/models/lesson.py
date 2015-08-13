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

from .base import BaseLesson, BaseLessonManager
from .base import lesson_nr_block, lesson_nr_lesson, lesson_nr_step

class LessonManager(BaseLessonManager):


    def create_block(self, nr, title, text, description, course):
        block = BaseLesson(course=course,
                       title=title,
                       description=description,
                       text=text,
                       nr=nr,
                       lesson_nr=lesson_nr_block()
                       )
        block.insert_at(None)
        block.save()
        return block

    def create_lesson(self, nr, title, text, description, course, parent):
        lesson = BaseLesson(course=course,
                       title=title,
                       description=description,
                       text=text,
                       nr=nr,
                       lesson_nr=lesson_nr_lesson(nr=nr)
                       )
        lesson.insert_at(parent)
        lesson.save()
        return lesson

    def create_step(self, nr, title, text, description, course, parent, materials):
        print "here"
        step = Lesson()
        step.course = course
        step.title = title
        step.description = description
        #step.nr = lesson_nr_step(nr=nr, parent_nr=parent.nr)
        step.nr =str(nr)
        step.insert_at(parent)
        step.save()
        for item in materials:
            step.materials.add(item)
        return step


class Lesson(BaseLesson):
    old_pk = models.IntegerField(null=True)

    objects = LessonManager()

    class Meta:
        verbose_name = "Vorlage-Lektion"
        verbose_name_plural = "Vorlage-Lektionen"

    @cached_property
    def course_slug(self):
        return self.course.slug


