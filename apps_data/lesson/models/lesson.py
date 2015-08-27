# coding: utf-8

from __future__ import unicode_literals, absolute_import

from model_utils.fields import MonitorField

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import BaseLesson, BaseLessonManager
from .base import lesson_nr_block, lesson_nr_lesson, lesson_nr_step

# for datatransefer
from apps_data.course.models.oldcoursepart import CourseBlock, CourseMaterialUnit, CourseUnit


class LessonManager(BaseLessonManager):

    def create_block(self, nr, title, text, description, course):
        """
        creates a block
        :param nr:
        :param title:
        :param text:
        :param description:
        :param course:
        :return: created block
        """
        block = Lesson(course=course,
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
        """
        creates a lesson
        :param nr:
        :param title:
        :param text:
        :param description:
        :param course:
        :param parent:
        :return: created lesson
        """
        lesson = Lesson(course=course,
                       title=title,
                       description=description,
                       text=text,
                       nr=nr,
                       lesson_nr=lesson_nr_lesson(nr=nr)
                       )
        lesson.insert_at(parent)
        lesson.save()
        return lesson

    def create_step(self, nr, title, text, description, course, parent, material):
        """
        creates a step
        :param nr:
        :param title:
        :param text:
        :param description:
        :param course:
        :param parent:
        :param materials:
        :return: cretaed lesson step
        """
        step = Lesson(course=course,
                       title=title,
                       description=description,
                       text=text,
                       nr=nr,
                       lesson_nr=lesson_nr_step(nr=nr, parent_nr=parent.nr),
                       material=material,
                       )
        step.insert_at(parent)
        step.save()
        return step

    def blocks_for_delete(self, courseevent):
        return self.objects.all()


class Lesson(BaseLesson):
    #just for the data_migration: refers to old data-structure (oldcourseparts),
    # will be deleted after data-transfer
    courseblock = models.ForeignKey(CourseBlock, null=True, blank=True, related_name="lessonblock")
    unit = models.ForeignKey(CourseUnit, null=True, blank=True, related_name="lessonunit")
    unitmaterial = models.ForeignKey(CourseMaterialUnit, null=True, blank=True, related_name="lessonmaterial")

    objects = LessonManager()

    class Meta:
        verbose_name = "Lektion (Vorlage)"
        verbose_name_plural = "Lektionen (Vorlage)"

    def cb_id(self):
        if self.courseblock:
            return self.courseblock.id

    def u_id(self):
        if self.unit:
            return self.unit.id

    def um_id(self):
        if self.unitmaterial:
            return self.unitmaterial.id


