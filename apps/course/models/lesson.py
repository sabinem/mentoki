# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.functional import cached_property
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
from model_utils.fields import StatusField
from model_utils import Choices
from model_utils.models import TimeStampedModel

from model_utils.managers import PassThroughManager
from model_utils.managers import QueryManager

from django.core.urlresolvers import reverse

from .course import Course
from .material import Material
from .oldcoursepart import CourseBlock, CourseMaterialUnit, CourseUnit
from ..managers import LessonQuerySet


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
    material = models.ManyToManyField(Material, null=True, blank=True)

    #just for the data_migration:
    block = models.ForeignKey(CourseBlock, null=True, blank=True)
    unit = models.ForeignKey(CourseUnit, null=True, blank=True)
    unitmaterial = models.ForeignKey(CourseMaterialUnit, null=True, blank=True)


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
    def has_material(self):
        if self.material:
           return True

    @cached_property
    def attached_materials(self):
        return Material.objects.materials_for_lesson(lesson=self.id)

    @cached_property
    def is_block(self):
        if self.is_root_node():
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
    def is_lesson_part(self):
        if self.get_level() == 2:
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse('coursebackend:lesson:detail', kwargs={'course_slug':self.course_slug, 'pk':self.pk })



