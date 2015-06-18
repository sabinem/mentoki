# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from model_utils.models import TimeStampedModel
from django.utils.functional import cached_property

from autoslug import AutoSlugField
from model_utils.fields import StatusField
from model_utils import Choices
from model_utils.managers import PassThroughManager

from .course import Course
from .oldcoursepart import CourseMaterialUnit
from ..managers import MaterialQuerySet


def lesson_material_name(instance, filename):
        path = '/'.join([instance.course.slug, slugify(instance.title), filename])
        return path

class Material(TimeStampedModel):

    course = models.ForeignKey(Course, blank=True, null=True)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, verbose_name='kurze Beschreibung')

    DOCTYPE = Choices('text', 'pdf')
    document_type  = StatusField(choices_name='DOCTYPE')

    pdf_download_link = models.BooleanField(default=False)
    pdf_viewer = models.BooleanField(default=False)
    pdf_link = models.BooleanField(default=False)

    file = models.FileField(upload_to=lesson_material_name, blank=True, verbose_name="Datei")
    slug = AutoSlugField(populate_from='get_file_slug', blank=True)

    #just for the data_migration: refers to old data-structure (oldcourseparts),
    # will be deleted after data-transfer
    unitmaterial = models.ForeignKey(CourseMaterialUnit, null=True, blank=True)

    objects = PassThroughManager.for_queryset_class(MaterialQuerySet)()

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materialien"

    def __unicode__(self):
        return u'%s/%s' % (self.course, self.title)

    def get_file_slug(instance):
        pathparts = instance.file.name.split('/')
        return '-'.join(pathparts)

    @cached_property
    def course_slug(self):
        return self.course.slug

    def get_absolute_url(self):
        return reverse('coursebackend:material:detail', kwargs={'course_slug':self.course_slug, 'pk':self.pk })

