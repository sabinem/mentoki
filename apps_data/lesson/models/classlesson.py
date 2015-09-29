# coding: utf-8

from __future__ import unicode_literals, absolute_import

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError
from django.utils.functional import cached_property

from model_utils.fields import MonitorField

from apps_data.courseevent.models.courseevent import CourseEvent

from .base import BaseLesson, lesson_nr_lesson, lesson_nr_step, lesson_nr_block
from .lesson import Lesson, LessonManager


class ClassLessonManager(LessonManager):
    """
    ClassLessons are derived from Base Lessons. They come into being by being
    copied from Lessons, as copies that should serve in one courseevent.
    The Owner decides himself where the master should recide. He can chose
    to make the Classlesson Master, then the relation to the original lesson
    is resolved and later on he can copy it back to the course as a new lesson
    or block. But he can also leave the master at the course and continue to
    changes over to the courseevent.
    """
    def create_classlessonblock(self, nr, title, text, description, courseevent):
        """
        this creates a classlesson
        """
        classlessonroot = ClassLesson.objects.get(
            level=0,
            courseevent=courseevent)
        classlesson = ClassLesson(course=courseevent.course,
                       courseevent=courseevent,
                       title=title,
                       description=description,
                       text=text,
                       nr=nr,
                       lesson_nr=lesson_nr_block(nr=nr)
                       )
        classlesson.insert_at(classlessonroot)
        classlesson.save()
        ClassLesson.objects.rebuild()
        return classlesson

    def create_classlesson(self, nr, title, text, description, courseevent, parent):
        """
        this creates a classlesson
        """
        classlesson = ClassLesson(course=courseevent.course,
                       courseevent=courseevent,
                       title=title,
                       description=description,
                       text=text,
                       nr=nr,
                       lesson_nr=lesson_nr_lesson(nr=nr)
                       )
        classlesson.insert_at(parent)
        classlesson.save()
        ClassLesson.objects.rebuild()
        return classlesson

    def create_classstep(self, nr, title, text, description, courseevent,
                         parent, material, is_homework):
        """
        this creates a classlessonstep
        """
        classstep = ClassLesson(course=courseevent.course,
                       courseevent=courseevent,
                       title=title,
                       description=description,
                       text=text,
                       nr=nr,
                       lesson_nr=lesson_nr_step(nr=nr, parent_nr=parent.nr),
                       material=material,
                       is_homework=is_homework,
                       )
        classstep.insert_at(parent)
        classstep.save()
        ClassLesson.objects.rebuild()
        return classstep


    def copied_lesson_ids(self,courseevent):
        """
        this fetches the ids of all lessons for a courseevent, that
        are related to lessons in the course
        """
        return self.filter(courseevent=courseevent, original_lesson__isnull=False).\
            values_list('original_lesson_id', flat=True)

    def copied_block_ids(self,courseevent):
        """
        this fetches the ids of all lessons for a courseevent, that
        are related to lessons in the course
        """
        return self.filter(courseevent=courseevent,
                           original_lesson__isnull=False,
                           level=1).\
            values_list('original_lesson_id', flat=True)

    def copied_blocks(self,courseevent):
        """
        this fetches the ids of all lessons for a courseevent, that
        are related to lessons in the course
        """
        return self.filter(courseevent=courseevent,
                           original_lesson__isnull=False, level=1)

    def independent_blocks(self,courseevent):
        """
        this fetches the ids of all lessons for a courseevent, that
        are related to lessons in the course
        """
        return self.filter(courseevent=courseevent, level=1,
                           original_lesson=None)

    def complete_tree_for_courseevent(self, courseevent):
        """
        gets complete tree for courseevent including materials
        """
        return self.filter(courseevent=courseevent, level=0).\
            get_descendants(include_self=True).order_by('nr').select_related('material')

    def blocks_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent,
                           level=1,
                           )

    def lessons_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent,
                           level=2,
                           )

    def lessons_for_menu(self, courseevent):
        return self.filter(courseevent=courseevent,
                           level__gt=1,
                           )

    def lessonsteps_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent,
                           level=3,
                           )

    def homeworks(self, courseevent):
        return self.filter(courseevent=courseevent,
                           is_homework=True,
                           ).order_by('created')

    def published_homeworks(self, courseevent):
        from apps_data.courseevent.models.menu import ClassroomMenuItem
        ids = ClassroomMenuItem.objects.lesson_ids_published_in_class()

        return self.filter(courseevent=courseevent,
                           is_homework=True,

                           ).order_by('created')


class ClassLesson(BaseLesson):
    """
    ClassLesson is a copy of the course lesson that adapted
    for a courseevent.

    Class Lessons are never created but just copied. They can be updated
    and thereby refined for the class.
    """
    courseevent = models.ForeignKey(CourseEvent)

    # original lesson cannot be deleted aslong as it is employed in some classroom
    original_lesson = models.ForeignKey(
        Lesson,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    is_original_lesson = models.BooleanField(default=True)
    is_master = models.BooleanField(default=True)

    due_date = models.DateField(
        verbose_name='Abgabedatum',
        blank=True,
        null=True)

    extra_text = models.TextField(
        verbose_name="Anhang Aufgabe",
        help_text="Anhang zu Aufgaben",
        blank=True)

    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)

    objects = ClassLessonManager()

    class Meta:
        verbose_name = "Lektion (Kurs)"
        verbose_name_plural = "Lektionen (Kurs)"

    class MPTTMeta:
        order_insertion_by = ['course', 'courseevent', 'nr']

    def get_breadcrumbs_with_self_published(self):
        return self.get_ancestors(include_self=True).filter(published=True)

    def outdated(self):
        if self.modified < self.original_lesson.modified:
            print self.modified
            print self.original_lesson.modified
            return True
        else:
            return False

    @cached_property
    def is_published_in_class(self):
        """
        decides wether there is a menuitem for the lesson
        """
        if self.is_block():
            return False
        # fetched here in order to avoid circular import
        from apps_data.courseevent.models.menu import ClassroomMenuItem
        menuitems = \
            ClassroomMenuItem.objects.lesson_ids_published_in_class(courseevent=self.courseevent)
        if self.id in menuitems:
            return True
        return False

    @property
    def is_visible_in_classroom(self):
        """
        decides wether a lesson is visible in the classroom. This is the case
        for a lessonstep if it is menuitem by itself or wether the parent lesson
        is a menu item.
        """
        if self.is_block():
            return False
        elif self.is_lesson():
            if self.is_published_in_class:
                return True
        elif self.is_step():
            if self.is_published_in_class or self.parent.is_published_in_class:
                return True
        return False

    def original_modified(self):
        """
        checks versions between the copied and the original lesson
        """
        if self.modified > self.created:
            return True
        else:
            return False

    @property
    def get_previous_sibling_published(self):
        # fetched here in order to avoid circular import
        from apps_data.courseevent.models.menu import ClassroomMenuItem
        previous = self
        while previous:
            previous = previous.get_previous_sibling()
            if previous:
                if previous.is_published_in_class:
                    return previous
        return None

    def get_next_sibling_published(self):
        next = self
        while next:
            next = next.get_next_sibling()
            if next:
                if next.is_published_in_class == True:
                   return next
        return None

    @property
    def get_previous_sibling_in_courseevent(self):
        previous = self.get_previous_sibling()
        if previous:
            if previous.courseevent == self.courseevent:
                return previous
        return None

    @property
    def get_next_sibling_in_courseevent(self):
        next = self.get_next_sibling()
        if next:
            if next.courseevent == self.courseevent:
                return next
        return None

    def get_published_breadcrumbs_with_self(self):
        if self.is_lesson():
            return self.get_ancestors(include_self=True).filter(level=2)
        elif self.is_step():
            return self.get_ancestors(include_self=True).filter(level__gt=1)

    def save(self, copy=False):
        if not copy:
            self.is_original_lesson = False
            self.modified = datetime.datetime.now()
        super(ClassLesson, self).save()

    def cut_block_connection(self):
        nodes = self.get_delete_tree()
        for node in nodes:
            node.original_lesson = None
            node.save()

    @property
    def studentswork_count(self):
        if self.is_homework:
            from apps_data.courseevent.models.homework import StudentsWork
            return StudentsWork.objects.filter(homework=self).count()