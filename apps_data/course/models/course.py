# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel
from model_utils.managers import PassThroughManager
from autoslug import AutoSlugField

class CourseManager(models.Manager):

    def get_course_or_404_from_slug(self, slug):
        return get_object_or_404(self, slug=slug)

    def create_course_for_user(self, user, title, slug):
        return get_object_or_404(self, slug=slug)

    def teaching(self, user):
        course_ids = CourseOwner.objects.teachingcourses(user=user).values_list('course_id', flat=True)
        print course_ids
        return self.filter(pk__in=course_ids)


class Course(TimeStampedModel):

    title = models.CharField(max_length=100, verbose_name='Überschrift')
    slug = AutoSlugField(populate_from='title', blank=True, unique=True)

    excerpt = models.TextField(blank=True,verbose_name="Abstrakt")
    target_group = models.TextField(blank=True, verbose_name="Zielgruppe")
    prerequisites = models.TextField(blank=True, verbose_name="Voraussetzungen")
    project = models.TextField(blank=True, verbose_name="Teilnehmerprojekt")
    structure = models.TextField(blank=True, verbose_name="Gliederung")
    text = models.TextField(blank=True, verbose_name='Kursbeschreibung')

    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, through='CourseOwner')

    email = models.EmailField(default="info@mentoki.com")

    #objects = PassThroughManager.for_queryset_class(CourseQuerySet)()
    objects = CourseManager()

    class Meta:
        verbose_name = "Kursvorlage"
        verbose_name_plural = "Kursvorlagen"

    def __unicode__(self):
        return u'%s' % (self.title)

    def is_owner(self, user):
        try:
            CourseOwner.objects.get(course=self, user=user)
            return True
        except:
            return False

    @cached_property
    def teachers(self):
        user_ids = CourseOwner.objects.courseteachers(course=self).values_list('user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

    @cached_property
    def teachersrecord(self):
        teachers = self.teachers
        namesstring = ""
        for teacher in teachers:
            if namesstring != "":
                namesstring += " und "
            namesstring += u"%s %s" % (teacher.first_name, teacher.last_name)
        return namesstring

    def get_absolute_url(self):
        return reverse('coursebackend:course:detail', kwargs={'course_slug':self.slug})


class CourseOwnerManager(models.Manager):

    def teachingcourses(self, user):
        return self.filter(user=user).select_related('course')

    def courseteachers(self, course):
        return self.filter(course=course).order_by('display_nr').select_related('user')

    def teachers_courseinfo(self, course):
        return self.filter(course=course, display=True).select_related('user')


def foto_location(instance, filename):
        return '/'.join([instance.course.slug, filename])

class CourseOwner(TimeStampedModel):

    course = models.ForeignKey(Course)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    text = models.TextField(blank=True, verbose_name='Text')

    foto = models.ImageField(upload_to=foto_location, blank=True)

    display = models.BooleanField(default=True, verbose_name='Anzeigen bei der Kursausschreibung?')

    display_nr = models.IntegerField(default=1, verbose_name='Anzeigereihenfolge bei mehreren Kursleitern')

    objects = CourseOwnerManager()

    class Meta:
        verbose_name = "Kursleitung"
        verbose_name_plural = "Kursleitungen"
        ordering = [ 'course', 'display_nr' ]

    def __unicode__(self):
        return u'%s %s' % (self.course, self.user)

    @cached_property
    def owner_name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)