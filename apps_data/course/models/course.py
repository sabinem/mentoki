# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models

from django.conf import settings
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from autoslug import AutoSlugField

from mentoki.settings import DEFAULT_COURSE_FROM_EMAIL


class CourseManager(models.Manager):

    use_for_related_fields = True

    #def get_course_or_404_from_slug(self, slug):
        # gets course from slug
        #return get_object_or_404(self, slug=slug)

    #def teachers_courseinfo(self, slug):
        # gets course from slug
        #return get_object_or_404(self, slug=slug)

    # <obj>.owners.all() gives all the owners for this course


class Course(TimeStampedModel):
    """
    Courses are the central model of the Application. They gather all the material for teaching the subject
    without any regards to the actual event of teaching that material to students.
    """

    title = models.CharField(verbose_name=_('title'),
                             help_text=_('Working title for your course. You may change this later on'),
                             max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    # course owners are the teachers
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, through='CourseOwner')

    # Information about the course
    excerpt = models.TextField(verbose_name=_('abstract'),
                               help_text=_('Abstracts serve to describe courses on course list page'),
                               blank=True,)
    target_group = models.TextField(verbose_name=_('targetgroup'),
                               help_text = _('The target group for your course.'),
                               blank=True)
    prerequisites = models.TextField(verbose_name="Voraussetzungen",
                               help_text = _('The prequisites for your course. What prior knowledge must be there?'),
                               blank=True)
    project = models.TextField(verbose_name="Teilnehmerprojekt",
                               help_text = _('What do the participants take away from your course?'),
                               blank=True)
    structure = models.TextField(verbose_name="Gliederung",
                               help_text = _('Provide the structure of your course.'),
                               blank=True)
    text = models.TextField(verbose_name='Kursbeschreibung',
                               help_text = _('Here you can give a detailed description of your course.'),
                               blank=True)
    # Email Account for the course
    email = models.EmailField(default=DEFAULT_COURSE_FROM_EMAIL)

    objects = CourseManager()

    class Meta:
        verbose_name = "Kursvorlage"
        verbose_name_plural = "Kursvorlagen"

    def __unicode__(self):
        return u'%s' % (self.title)

    @cached_property
    def teachers(self):
        """
        Returns all the accounts of users who are involved with teaching that course sorted by the order in which
        they should be displayed
        """
        return self.owners.all().order_by('courseowner__display_nr')

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

    def is_owner(self, user):
        """
        Is this person a teacher in this course? (Then he may work on it.)
        """
        if user in self.teachers:
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse('coursebackend:course:detail', kwargs={'course_slug':self.slug})


class CourseOwnerManager(models.Manager):

    #def teachingcourses(self, user):
    #    return self.filter(user=user).select_related('course')

    #def courseteachers(self, course):
    #    return self.filter(course=course).order_by('display_nr').select_related('user')

    def teachers_courseinfo_display(self, course):
        return self.filter(course=course, display=True).select_related('user').order_by('display_nr')

    def teachers_courseinfo_all(self, course):
        return self.filter(course=course).select_related('user').order_by('display_nr')


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

    objects = CourseOwnerManager()

    class Meta:
        verbose_name = "Kursleitung"
        verbose_name_plural = "Kursleitungen"
        ordering = [ 'course', 'display_nr' ]

    def __unicode__(self):
        return u'%s %s' % (self.course, self.user)

