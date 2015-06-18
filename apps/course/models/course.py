# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.conf import settings
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel
from model_utils.managers import PassThroughManager
from autoslug import AutoSlugField

from ..managers import CourseOwnerQuerySet


class Course(TimeStampedModel):

    title = models.CharField(max_length=100, verbose_name='Überschrift')
    slug = AutoSlugField(populate_from='title', blank=True, unique=True)

    excerpt = models.TextField(blank=True,verbose_name="Abstrakt")
    target_group = models.TextField(blank=True, verbose_name="Zielgruppe")
    prerequisites = models.TextField(blank=True, verbose_name="Voraussetzungen")
    project = models.TextField(blank=True, verbose_name="Teilnehmerprojekt")
    structure = models.TextField(blank=True, verbose_name="Gliederung")
    text = models.TextField(blank=True, verbose_name='Kursbeschreibung')

    email = models.EmailField(default="info@mentoki.com")

    class Meta:
        verbose_name = "Kursvorlage"
        verbose_name_plural = "Kursvorlagen"

    def __unicode__(self):
        return u'%s' % (self.title)

    @cached_property
    def teachers(self):
        course_owners = CourseOwner.objects.filter(course=self.id)
        teacher_list = []
        for teacher in course_owners:
            teacher_list.append(teacher.user)
        return teacher_list

    @cached_property
    def teachersrecord(self):
        teachers = self.teachers
        namesstring = ""
        for teacher in teachers:
            if namesstring != "":
                namesstring += " und "
            namesstring += u"%s %s " % (teacher.first_name, teacher.last_name)
        return namesstring

    def get_absolute_url(self):
        return reverse('coursebackend:course', kwargs={'slug':self.slug})


def foto_location(instance, filename):
        return '/'.join([instance.course.slug, filename])

class CourseOwner(TimeStampedModel):

    course = models.ForeignKey(Course)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    text = models.TextField(blank=True, verbose_name='Text')

    foto = models.ImageField(upload_to=foto_location, blank=True)

    display = models.BooleanField(default=True, verbose_name='Anzeigen bei der Kursausschreibung?')

    display_nr = models.IntegerField(default=1, verbose_name='Anzeigereihenfolge bei mehreren Kursleitern')

    objects = PassThroughManager.for_queryset_class(CourseOwnerQuerySet)()

    class Meta:
        verbose_name = "Kursleitung"
        verbose_name_plural = "Kursleitungen"
        ordering = [ 'course', 'display_nr' ]

    def __unicode__(self):
        return u'%s %s' % (self.course, self.user)

    @cached_property
    def name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)