# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models

from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField
from model_utils import Choices
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property
from autoslug import AutoSlugField

from .course import Course


class CoursePartModel(TimeStampedModel):

    course  = models.ForeignKey(Course, verbose_name='XKurs')

    title = models.CharField(max_length=100, verbose_name='Ueberschrift')
    description = models.CharField(max_length=200, blank=True, verbose_name='kurze Beschreibung')
    text = models.TextField(blank=True, verbose_name='Text')

    display_nr = models.IntegerField(
        verbose_name='interne Nummer, steuert die Anzeigereihenfolge',
    )

    STATUS = Choices('Entwurf', 'Veröffentlicht')
    status = StatusField()

    class Meta:
        abstract=True


class CourseBlock(CoursePartModel):

    is_numbered = models.BooleanField(default=True)
    show_full = models.BooleanField(default=True)

    class Meta:
        verbose_name = "XUnterrichtsblock"
        verbose_name_plural = "XUnterrichtsblöcke"
        ordering = ['display_nr']

    def __unicode__(self):
        return u'%s/%s' % (self.course, self.title)

    @cached_property
    def urlprefix(self):
        return self.course.urlprefix



class CourseUnit(CoursePartModel):
    block = models.ForeignKey(CourseBlock)

    def __unicode__(self):
        return u'%s / %s' % (self.block, self.title)

    class Meta:
        verbose_name = "xLektion"


def lesson_material_name(instance, filename):
        print instance.course_id
        print instance.course.slug
        path = '/'.join([instance.course.slug, slugify(instance.unit.title), filename])
        print path
        return path

class CourseMaterialUnit(CoursePartModel):
    """
    material like pdf files, etc can only be defined on this sublevel to units.
    """
    unit = models.ForeignKey(CourseUnit)

    DOCTYPE = Choices('Text', 'PDF Viewer', 'PDF download und Text')
    document_type  = StatusField(choices_name='DOCTYPE')

    file = models.FileField(upload_to=lesson_material_name, blank=True, verbose_name="Datei")
    slug = AutoSlugField(populate_from='get_file_slug', blank=True)

    class Meta:
        verbose_name = "xMaterial"

    def __unicode__(self):
        return u'%s/%s' % (self.unit, self.title)

    def get_file_slug(instance):
        pathparts = instance.file.name.split('/')
        return '-'.join(pathparts)

def lesson_material_name(instance, filename):
        print instance.course_id
        print instance.course.slug
        path = '/'.join([instance.course.slug, slugify(instance.unit.title), filename])
        print path
        return path

