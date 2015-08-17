# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from django.forms import forms

from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property

from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField
from model_utils import Choices

from autoslug import AutoSlugField

from apps_core.core.fields import ContentTypeRestrictedFileField
from apps_data.course.models.course import Course

# still a Foreignkey on a old table: this will be deleted after the data-transfer
from apps_data.course.models.oldcoursepart import CourseMaterialUnit


class MaterialManager(models.Manager):

    def materials_for_course(self, course):
        """
        gets all materials for a course
        :param course:
        :return: all material for a course
        """
        return self.filter(course=course)

    def create(self, course, title, file, document_type, description="",
               pdf_download_link=True,
               pdf_link=True, pdf_viewer=True):
        """
        creates a new material for course
        :param course:
        :param title:
        :param file:
        :param document_type:
        :param description:
        :param pdf_download_link:
        :param pdf_link:
        :param pdf_viewer:
        :return: created material
        """
        material = Material(course=course,
                            title=title,
                            file=file,
                            description=description,
                            document_type=document_type,
                            pdf_link=pdf_link,
                            pdf_download_link=pdf_download_link,
                            pdf_viewer=pdf_viewer)
        material.save()
        return material

def lesson_material_name(instance, filename):
    """
    constructs the path where the file ist stored: <course-slug>/slugify<title>
    since course and title are unique together this should be unique
    :param instance: material instance
    :param filename: filename
    :return: path were the uploaded file is stored
    """
    path = '/'.join([instance.course.slug, slugify(instance.title), filename])
    return path


class Material(TimeStampedModel):
    """
    Materials are uploaded files. So far only pdfs can be uploaded.
    """
    course = models.ForeignKey(Course, related_name="coursematerial")

    title = models.CharField(
        verbose_name="Material-Titel",
        help_text='''Titel, unter dem das Material angezeigt wird.
        ''',
        max_length=100
    )
    description = models.CharField(
        verbose_name=_('kurze Beschreibung des Materials'),
        help_text=_("""Diese Beschreibung wird in Listen oder Übersichtsseiten
        angezeigt."""),
        max_length=200,
        blank=True
    )
    DOCTYPE = Choices(('zip', 'zip-Datei'),
                      ('pdf', 'pdf-Datei'))
    document_type  = StatusField(
        verbose_name='Dateityp',
        help_text="""Derzeit sind nur pdf und zip erlaubt.""",
        choices_name='DOCTYPE',
        default='pdf'
    )
    pdf_download_link = models.BooleanField(
        verbose_name=_('Download-Link anbieten?'),
        help_text=_("""Es wird ein Download-Link angeboten."""),
        default=False
    )
    pdf_viewer = models.BooleanField(
        verbose_name='Pdf-Viewer anbieten?',
        help_text=_("""Bei Dateityp pdf: Das pdf-Datei ist durch einen Pdf-
        Viewer ind die Webseite integriert, falls das möglich ist (auf dem PC
        zum Beispiel)."""),
        default=False
    )
    pdf_link = models.BooleanField(
        verbose_name=_('Link anbieten?'),
        help_text=_("""Bei Dateityp pdf: das pdf-file ist über einen Link
        erreichbar."""),
        default=False
    )
    file = ContentTypeRestrictedFileField(
        upload_to=lesson_material_name, verbose_name="Datei",
        content_types=['application/pdf'],
        max_upload_size=5242880,
    )
    slug = AutoSlugField(populate_from='get_file_slug', unique=True, always_update=True)

    #just for the data_migration: refers to old data-structure (oldcourseparts),
    # will be deleted after data-transfer
    unitmaterial = models.ForeignKey(CourseMaterialUnit, null=True, blank=True, related_name="unitmaterial")

    unique_together=('course', 'title')

    objects = MaterialManager()

    class Meta:
        verbose_name=_("Material")
        verbose_name_plural=_("Materialien")

    def __unicode__(self):
        return u'%s' % (self.file)

    def um_id(self):
        if self.unitmaterial:
            return self.unitmaterial.id

    def get_file_slug(instance):
        """
        creates a unique slug for a file from the material-title and the course-slug
        the slug will be used for downloading the file, it is unique because
        course and title are unique together.
        :param instance: of the material
        :return: slug for download
        """
        sequence=(instance.course.title, instance.title)
        return '-'.join(sequence)

    def get_absolute_url(self):
        return reverse('coursebackend:material:detail', kwargs={'course_slug':self.course_slug, 'pk':self.pk })

    def clean(self):
        """
        so far only pdf files will be accepted
        Errors:
        no_zip: zip files are not accepted so far
        no_file: Material cannot be stored without a file to upload
        """
        if self.document_type == self.DOCTYPE.zip:
            if (self.pdf_viewer or self.pdf_link):
                forms.ValidationError(_('zip file kann nicht angezeigt werden.'), code='no_zip')
