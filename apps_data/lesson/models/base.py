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
from django.db.models.loading import get_model

from mptt.models import MPTTModel, TreeForeignKey, TreeManager

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField
from model_utils.choices import Choices

from apps_data.course.models.course import Course
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.material.models.material import Material

from model_utils.managers import QueryManager
from django.db.models import Q


class BaseLessonManager(TreeManager):

    def complete_tree_for_course(self, course):
        return self.filter(course=course, level=0).\
            get_descendants(include_self=True).prefetch_related('materials')

    def lessons_for_course(self, course):
        return self.filter(course=course,
                           level=1,
                           )

    def blocks_for_course(self, course):
        return self.filter(course=course,
                           level=0,
                           )


def lesson_material_name(instance, filename):
        path = '/'.join([instance.course.slug, slugify(instance.title), filename])
        return path

def lesson_nr_block():
    return ""

def lesson_nr_lesson(nr):
    return u'%s' % str(nr)

def lesson_nr_step(nr, parent_nr):
    return u'%s.%s' % (str(parent_nr), str(nr))


class BaseLesson(MPTTModel, TimeStampedModel):

    parent = TreeForeignKey('self',
        verbose_name="einhängen unter",
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        )

    course = models.ForeignKey(Course)

    nr = models.IntegerField(
        verbose_name=_('Nr.'),
        default=1)
    lesson_nr = models.CharField(
        verbose_name=_('Lektionsnr.'),
        help_text='abgeleitetes Feld: keine manuelle Eingabe',
        blank=True,
        max_length=10)

    title = models.CharField(
        verbose_name="Überschrift",
        help_text="Lektions-Titel",
        max_length=100)
    text = models.TextField(
        verbose_name="Lektionstext",
        help_text="Text der Lektion",
        blank=True)
    description = models.CharField(
        verbose_name='kurze Beschreibung',
        help_text="diese Beschreibung erscheint nur in den Übersichten",
        max_length=200,
        blank=True)

    materials = models.ManyToManyField(Material,
        verbose_name="Kursmaterial",
        help_text="Material der Lektion",
        blank=True)

    objects = BaseLessonManager()

    LESSON_TYPE = Choices(
                     ('block', _('Block')),
                     ('lesson', _('Lesson')),
                     ('step', _('Step')),)

    class Meta:
        verbose_name = "Lektion"
        verbose_name_plural = "Lektionen"
        abstract = True

    class MPTTMeta:
        order_insertion_by = ['course', 'nr']

    def __unicode__(self):
        if self.level == 0:
            return u'Block: %s' % (self.title)
        elif self.level == 1:
            return u'%s: %s. %s' % (self.parent.title, self.lesson_nr, self.title)
        elif self.is_step:
            return u'%s %s' % (self.lesson_nr, self.title)

    def save(self, *args, **kwargs):
        # lesson_nr is calculated and stored in the database for performance
        if self.level:
            if self.level == 0:
                self.lesson_nr = lesson_nr_block()
            elif self.level == 1 :
                self.lesson_nr = lesson_nr_lesson(nr=self.nr)
            elif self.level == 2 :
                self.lesson_nr = lesson_nr_step(nr=self.nr, parent_nr=self.parent.nr)
        super(BaseLesson, self).save(*args, **kwargs)

    @property
    def lesson_type(self):
        if self.level == 0 :
            return self.LESSON_TYPE.block
        elif self.level == 1 :
            return self.LESSON_TYPE.lesson
        elif self.level == 2 :
            return self.LESSON_TYPE.step
        else:
            raise ValueError('unexpected lesson level')

    def breadcrumb(self):
        if self.level == 0:
            return u'%s' % (self.title)
        elif self.level == 1:
            return u'%s. %s' % (self.lesson_nr, self.title)
        elif self.is_step:
            return u'%s %s' % (self.lesson_nr, self.title)

    def get_next_sibling(self):
        next = super(BaseLesson, self).get_next_sibling()
        try:
            if next.course_id == self.course_id:
                return next
            else:
                return None
        except:
            return None

    def get_previous_sibling(self):
        previous = super(BaseLesson, self).get_previous_sibling()
        try:
            if previous.course_id == self.course_id:
                return previous
            else:
                return None
        except:
            return None

    def get_tree_with_material(self):
        return self.get_descendants(include_self=False).prefetch_related('materials')

    def get_tree_without_material(self):
        return self.get_descendants(include_self=False)

    def is_block(self):
        if self.get_level() == 0:
            return True
        else:
            return False

    def is_lesson(self):
        if self.get_level() == 1:
            return True
        else:
            return False

    def is_step(self):
        if self.get_level() == 2:
            return True
        else:
            return False

    def is_owner(self, user):
        """
        Is this person a teacher in this course? (Then he may work on it.)
        """
        if self.course.is_owner(user):
            return True
        else:
            return False

