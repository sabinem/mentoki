# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel
from model_utils.managers import PassThroughManager
from autoslug import AutoSlugField


class CourseManager(models.Manager):

    def get_course_or_404_from_slug(self, slug):
        # gets course from slug
        return get_object_or_404(self, slug=slug)

    # <obj>.owners.all() gives all the owners for this course



class Course(TimeStampedModel):
    """
    Courses are the central model of the Application. They gather all the material for teaching the subject
    without any regards to the actual event of teaching that material to students.
    """

    title = models.CharField(max_length=100, verbose_name='Überschrift')
    slug = AutoSlugField(populate_from='title', unique=True)

    # course owners are the teachers
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, through='CourseOwner')

    # Information about the course
    excerpt = models.TextField(blank=True,verbose_name="Abstrakt")
    target_group = models.TextField(blank=True, verbose_name="Zielgruppe")
    prerequisites = models.TextField(blank=True, verbose_name="Voraussetzungen")
    project = models.TextField(blank=True, verbose_name="Teilnehmerprojekt")
    structure = models.TextField(blank=True, verbose_name="Gliederung")
    text = models.TextField(blank=True, verbose_name='Kursbeschreibung')

    # Email Account for the course
    email = models.EmailField(default="info@mentoki.com")

    objects = CourseManager()

    class Meta:
        verbose_name = "Kursvorlage"
        verbose_name_plural = "Kursvorlagen"

    def __unicode__(self):
        return u'%s' % (self.title)

    def is_owner(self, user):
        """
        Is this person a teacher in this course? (Then he may work on it.)
        """
        try:
            CourseOwner.objects.get(course=self, user=user)
            return True
        except:
            return False

    @cached_property
    def teachers(self):
        """
        Returns all the accounts of users who are involved with teaching that course sorted by the order in which
        they should be displayed
        """
        return self.owners.all().order_by('courseowner__display_nr')

    @cached_property
    def teachersrecord(self):
        """
        Returns the teachers of the course as a string ready for display.
        """
        teachers = self.teachers
        namesstring = ""
        for teacher in teachers:
            if namesstring != "":
                namesstring += " und "
            namesstring += teacher.get_full_name()
        return namesstring

    def get_absolute_url(self):
        return reverse('coursebackend:course:detail', kwargs={'course_slug':self.slug})


def foto_location(instance, filename):
        return '/'.join([instance.course.slug, filename])

class CourseOwner(TimeStampedModel):
    """
    Relationship of Courses to Accounts through the Relationship of teaching.
    """
    course = models.ForeignKey(Course)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    # special text and foto for this course
    text = models.TextField(blank=True, verbose_name='Text')
    foto = models.ImageField(upload_to=foto_location, blank=True)

    # this information is about the display of the teachers in the course-profile:
    # Should the whole profile be displayed or just the name
    display = models.BooleanField(default=True, verbose_name='Anzeigen bei der Kursausschreibung?')
    # Whose name goes first?
    display_nr = models.IntegerField(default=1, verbose_name='Anzeigereihenfolge bei mehreren Kursleitern')

    class Meta:
        verbose_name = "Kursleitung"
        verbose_name_plural = "Kursleitungen"
        ordering = [ 'course', 'display_nr' ]

    def __unicode__(self):
        return u'%s %s' % (self.course, self.user)

