# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.db.models.query import QuerySet
from django.utils.functional import cached_property

from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField
from model_utils import Choices
from model_utils.managers import PassThroughManager

from autoslug import AutoSlugField

from .course import Course
# still a Foreignkey on a old table: this will be deleted after the data-transfer
from .oldcoursepart import CourseMaterialUnit


class ContentTypeRestrictedFileField(FileField):
    """
    I have copied this from this source:
    http://nemesisdesign.net/blog/coding/django-filefield-content-type-size-validation/

    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, content_types=None, max_upload_size=None, **kwargs):
        # these are defined in the field
        self.content_types = content_types
        self.max_upload_size = max_upload_size
        super(ContentTypeRestrictedFileField, self).__init__(**kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)

        file = data.file
        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file._size > self.max_upload_size:
                    raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
            else:
                raise forms.ValidationError(_('Filetype not supported.'))
        except AttributeError:
            pass

        return data


class MaterialQuerySet(QuerySet):

    def materials_for_course(self, course):
        return self.filter(course=course)

    def materials_for_lesson(self, lesson):
        return self.filter(lesson=lesson)

def lesson_material_name(instance, filename):
        path = '/'.join([instance.course.slug, slugify(instance.title), filename])
        return path


class Material(TimeStampedModel):

    course = models.ForeignKey(Course, blank=True, null=True)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, verbose_name='kurze Beschreibung')

    DOCTYPE = Choices('zip', 'pdf')
    document_type  = StatusField(choices_name='DOCTYPE', default='pdf')

    pdf_download_link = models.BooleanField(default=False)
    pdf_viewer = models.BooleanField(default=False)
    pdf_link = models.BooleanField(default=False)

    file = ContentTypeRestrictedFileField(
        upload_to=lesson_material_name, blank=True, verbose_name="Datei",
        content_types=['application/pdf', 'application/zip'],
        max_upload_size=5242880
    )
    slug = AutoSlugField(populate_from='get_file_slug', blank=True)

    #just for the data_migration: refers to old data-structure (oldcourseparts),
    # will be deleted after data-transfer
    unitmaterial = models.ForeignKey(CourseMaterialUnit, null=True, blank=True)

    objects = PassThroughManager.for_queryset_class(MaterialQuerySet)()

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materialien"

    def __unicode__(self):
        return u'%s/%s' % (str(self.course_id), self.title)

    def get_file_slug(instance):
        pathparts = instance.file.name.split('/')
        return '-'.join(pathparts)

    @cached_property
    def course_slug(self):
        return self.course.slug

    def get_absolute_url(self):
        return reverse('coursebackend:material:detail', kwargs={'course_slug':self.course_slug, 'pk':self.pk })

    def clean(self):
        if self.document_type == self.DOCTYPE.zip:
            if (self.pdf_viewer or self.pdf_link):
                forms.ValidationError(_('zip file kann nicht angezeigt werden.'))
