# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManager
from django.utils.functional import cached_property
from django.template.defaultfilters import slugify
from django.conf import settings

from model_utils.models import TimeStampedModel

from django.core.urlresolvers import reverse

from .course import Course
from .material import Material
from .oldcoursepart import CourseBlock, CourseMaterialUnit, CourseUnit

from model_utils.managers import QueryManager
from django.db.models import Q

class LessonManager(TreeManager):

    def lessons_for_course(self,course_id):
        return self.filter(course_id=course_id, level=0).\
            get_descendants(include_self=True)


def lesson_material_name(instance, filename):
        path = '/'.join([instance.course.slug, slugify(instance.title), filename])
        return path

class Lesson(MPTTModel, TimeStampedModel):

    course = models.ForeignKey(Course)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name="einhängen unter")

    nr = models.IntegerField(default=1)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    description = models.CharField(max_length=200, blank=True, verbose_name='kurze Beschreibung')
    material = models.ManyToManyField(Material, blank=True)

    #just for the data_migration: refers to old data-structure (oldcourseparts),
    # will be deleted after data-transfer
    courseblock = models.ForeignKey(CourseBlock, null=True, blank=True)
    unit = models.ForeignKey(CourseUnit, null=True, blank=True)
    unitmaterial = models.ForeignKey(CourseMaterialUnit, null=True, blank=True)

    objects = LessonManager()
    block = QueryManager(level=0)
    lesson = QueryManager(level=1)
    lesson_step = QueryManager(level=2)
    parent_choice_new = QueryManager(level__lte=1).order_by('tree_id', 'level', 'nr')

    class Meta:
        verbose_name = "Lektion"
        verbose_name_plural = "Lektionen"

    class MPTTMeta:
        order_insertion_by = ['course', 'nr']

    def __unicode__(self):
        return u'%s %s' % (str(self.lesson_nr), self.title)

    @cached_property
    def course_slug(self):
        return self.course.slug

    def get_next_sibling(self):
        next = super(Lesson, self).get_next_sibling()
        try:
            if next.course_id == self.course_id:
                return next
            else:
                return None
        except:
            return None

    def get_previous_sibling(self):
        previous = super(Lesson, self).get_previous_sibling()
        try:
            if previous.course_id == self.course_id:
                return previous
            else:
                return None
        except:
            return None

    @cached_property
    def lesson_nr(self):
        if self.is_root_node():
            return ""
        elif self.parent.is_root_node():
            return u'%s' % str(self.nr)
        else:
            return u'%s.%s' % (str(self.parent.lesson_nr), str(self.nr))

    @cached_property
    def is_block(self):
        if self.get_level() == 0:
            return True
        else:
            return False

    @cached_property
    def is_lesson(self):
        if self.get_level() == 1:
            return True
        else:
            return False

    @cached_property
    def is_lesson_step(self):
        if self.get_level() == 2:
            return True
        else:
            return False


    def get_absolute_url(self):
        return reverse('coursebackend:lesson:detail', kwargs={'course_slug':self.course_slug, 'pk':self.pk })


    def possible_parents(self):
        qs = Lesson.objects.none()
        if self.is_block:
            pass
        elif self.is_leaf_node():
           qs = Lesson.objects.filter(level__lte=1, course=self.course)
        else:
           qs = Lesson.objects.filter(level=0, course=self.course)
        return qs.exclude(pk=self.pk).order_by('tree_id', 'level', 'nr')

