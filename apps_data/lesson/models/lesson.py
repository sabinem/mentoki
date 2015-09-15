# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404

from model_utils.fields import MonitorField
from model_utils.models import TimeStampedModel

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import BaseLesson, BaseLessonManager
from .base import lesson_nr_block, lesson_nr_lesson, lesson_nr_step


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
        lessonroot= get_object_or_404(Lesson, course=course, level=0)
        block = Lesson(course=course,
                       title=title,
                       description=description,
                       text=text,
                       nr=nr,
                       lesson_nr=lesson_nr_block(nr=nr)
                       )
        block.insert_at(lessonroot)
        block.save()
        Lesson.objects.rebuild()
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
        Lesson.objects.rebuild()
        return lesson

    def create_step(self, nr, title, text, description, course, parent, material, is_homework):
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
                       is_homework=is_homework,
                       )
        step.insert_at(parent)
        step.save()
        Lesson.objects.rebuild()
        return step

    def blocks_for_delete(self, courseevent):
        return self.objects.all()


class Lesson(BaseLesson, TimeStampedModel):

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

    def has_published_classlesson(self):
        if self.classlesson_set.filter(published=True):
            return True
        else:
            return False


