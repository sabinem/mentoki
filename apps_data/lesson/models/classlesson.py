# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError

from model_utils.fields import MonitorField

from apps_data.courseevent.models.courseevent import CourseEvent

from .base import BaseLesson
from .lesson import Lesson, LessonManager


class ClassLessonManager(LessonManager):
    """
    ClassLessons need their own query methods since they are searched by courseevent,
    rather then just course as the Base Lessons
    """
    def copied_lesson_ids(self,courseevent):
        """
        get all ids of original lessons that have already been copied for the courseevent
        :param courseevent
        :return: list of lesson ids of lessons that have been already copied for the courseevent
        """
        return self.filter(courseevent=courseevent).\
            values_list('original_lesson_id', flat=True)

    def complete_tree_for_courseevent(self, courseevent):
        """
        get complete tree for courseevent including materials
        :param courseevent
        :return: complete tree for courseevent
        """
        return self.filter(course=courseevent.course, courseevent=courseevent, level=0).\
            get_descendants(include_self=True).order_by('nr').prefetch_related('materials')

    def complete_tree_uncopied(self, courseevent):
        course_blocks = self.filter(course=courseevent.course, level=0).\
            exclude(course=courseevent.course,
                    courseevent=courseevent,
                    level=0)

    def lessons_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent,
                           level=1,
                           )

    def lessonsteps_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent,
                           level=2,
                           )



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

    published = models.BooleanField(
        verbose_name=_('veröffentlicht'),
        default=False,
        editable=False
    )
    publish_status_changed = MonitorField(monitor='published')

    objects = ClassLessonManager()

    class Meta:
        verbose_name = "Lektion (Kurs)"
        verbose_name_plural = "Lektionen (Kurs)"

    class MPTTMeta:
        order_insertion_by = ['course', 'courseevent', 'nr']

    def org_lesson_id(self):
        return self.original_lesson.id

    def can_be_pulled_from_classroom(self):
        homeworks = self.homework_set.values_list('published', flat=True)
        if homeworks:
            return False
        else:
            return True

    def get_breadcrumbs_with_self_published(self):
        return self.get_ancestors(include_self=True).filter(published=True)

    @property
    def get_previous_sibling_published(self):
        previous = self.get_previous_sibling()
        if previous:
            if previous.published == True:
                return previous
        return None

    @property
    def get_next_sibling_published(self):
        next = self.get_next_sibling()
        if next:
            if next.published == True:
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

    @property
    def published_homework(self):
        steps = self.get_children()
        for step in steps:
            if step.homework_set.filter(published=True):
                return True
        return False

    def publish(self):
        if not self.is_lesson():
            raise ValidationError('Nur Lektionen können veröffentlicht werden.')
        descendants = self.get_descendants(include_self=True)
        for descendant in descendants:
            descendant.published = True
            descendant.save()

    def unpublish(self):
        if not self.classlesson.published:
            raise ValidationError('Es gibt schon veröffentlichte Aufgaben dazu!')
        descendants = self.get_descendants(include_self=True)
        for descendant in descendants:
            descendant.published = False
            descendant.save()

    def delete(self):
        if self.published:
            raise ValidationError('Lektion wurde bereits veröffentlicht!')
        super(ClassLesson, self).delete()