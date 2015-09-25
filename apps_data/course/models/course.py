# coding: utf-8

"""
Courses are the timeindependent representation of Lessons.
In this file there are two classes: the database representation of Courses
and the many-to-many relationship of Courses to Owners: these are the teachers
teaching the courses, that are the only persons eligible to change their data.
"""
from __future__ import unicode_literals, absolute_import

from django.db import models

from django.conf import settings
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError

from model_utils.models import TimeStampedModel

from autoslug import AutoSlugField


class Course(TimeStampedModel):
    """
    Courses are the central model of the Application. They gather all the
    material for teaching the subject. Courseevents draw from here for the
    actual teaching.
    """

    title = models.CharField(
        verbose_name=_('Kurstitel'),
        help_text=_('''Arbeitstitel für Deinen Kurs. Er ist nicht öffentlich
                    sichtbar.'''),
        max_length=100
    )
    slug = AutoSlugField(
        populate_from='title',
        unique=True,
        editable=False
    )

    owners = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='CourseOwner'
    )

    excerpt = models.TextField(
        verbose_name=_('Kurze Zusammenfassung / Abstrakt'),
        help_text=_('''Diese Kurzbeschreibung dient später als Vorlage
                    bei der Ausschreibung Deiner Kurse'''),
        blank=True,
    )
    target_group = models.TextField(
        verbose_name=_('Zielgruppe'),
        help_text=_('Die Zielgruppe für Deinen Kurs.'),
        blank=True
    )
    prerequisites = models.TextField(
        verbose_name=_("Voraussetzungen"),
        help_text=_('''Welches Vorwissen wird in Deinem
                    Kurses Voraussetzung?'''),
        blank=True
    )
    project = models.TextField(
        verbose_name=_("Teilnehmerprojekt"),
        help_text=_('Was nehmen Teilnehmer aus Deinem Kurs für sich mit?'),
        blank=True
    )
    structure = models.TextField(
        verbose_name=_("Gliederung"),
        help_text=_('Gib eine Gliederung Deines Kurses an'),
        blank=True
    )
    text = models.TextField(
        verbose_name=_('Kursbeschreibung'),
        help_text=_('Hier kannst Du Deinen Kurs ausführlich beschreiben.'),
        blank=True
    )

    class Meta:
        verbose_name = _("Kursvorlage")
        verbose_name_plural = _("Kursvorlagen")

    def __unicode__(self):
        return u'%s' % (self.title)

    @cached_property
    def teachers(self):
        """
        Returns all the accounts of users, who are involved with teaching that
        course sorted by the order in which they should be displayed;
        RETURN: queryset of Users
        """
        return self.owners.all().order_by('courseowner__display_nr')

    @property
    def teachersrecord(self):
        """
        Returns the teachers of the course as a string ready for display.
        RETURN: string of teachers names
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
        IN: user
        RETURN: Bool whether user is owner
        """
        if user in self.teachers:
            return True
        else:
            return False

    def get_absolute_url(self):
        """
        absolute url of the course
        """
        return reverse('coursebackend:course:detail',
                       kwargs={'course_slug': self.slug})


class CourseOwnerManager(models.Manager):
    """
    Querysets on the Teachers/Owners of a course
    """
    def teachers_courseinfo_display(self, course):
        """
        gets all the teachers ownershiprecords, of teachers, whoes profiles
        should be displayed on the public page of the course; includes
        user-data
        IN: Course
        RETURN: CourseOwner-queryset; with user data
        """
        return self\
            .filter(course=course, display=True).select_related('user')\
            .order_by('display_nr')

    def teachers_courseinfo_all(self, course):
        """
        gets all teachers ownershiprecords for a course including their user
        data
        IN: Course
        RETURN: CourseOwner-queryset; with user data
        """
        return self\
            .filter(course=course).select_related('user')\
            .order_by('display_nr')

    def other_teachers_for_display(self, course, user):
        """
        checks whether there are teachers records other from the given users
        for this course.
        IN: Course, User
        RETURN: CourseOwner-queryset
        """
        return self \
            .filter(course=course, display=True) \
            .exclude(user=user)

    def teachers_emails(self, course):
        """
        get all teachers emails; includes user-data
        IN: Course
        RETURN: queryset-list of emails
        """
        return self.filter(course=course)\
            .select_related('user')\
            .values_list('user__email', flat=True)


def foto_location(instance, filename):
        """
        location where the teachers foto is stored
        IN: CourseOwner, filename
        RETURN: path <course-slug>/<filename>
        """
        return '/'.join([instance.course.slug, filename])


class CourseOwner(TimeStampedModel):
    """
    Relationship of Courses to Users through the Relationship of teaching
    / owning the course.
    """
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Kursleiter"),
        on_delete=models.PROTECT
    )

    text = models.TextField(
        verbose_name=_('Kursleiterbeschreibung'),
        help_text=_('''Personenbeschreibung: was qualifiziert Dich für das
                  Halten dieses Kurses?'''),
        blank=True
    )
    foto = models.ImageField(
        verbose_name=_('Kursleiter-Foto'),
        help_text=_('''Hier kannst Du ein Foto von Dir hochladen, das auf der
                    Kursauschreibung erscheinen soll.'''),
        upload_to=foto_location, blank=True
    )

    display = models.BooleanField(
        verbose_name=_('Anzeigen auf der Auschreibungsseite?'),
        help_text=_('''Soll dieses Profil auf der Kursausschreibungsseite
                    angezeigt werden?.'''),
        default=True
    )
    display_nr = models.IntegerField(
        verbose_name=_('Anzeigereihenfolge'),
        help_text=_('''Dieses Feld steuert die Anzeigereihenfolge bei mehreren
                    Kursleitern.'''),
        default=1
    )

    objects = CourseOwnerManager()

    class Meta:
        verbose_name = _("Kursleitung")
        verbose_name_plural = _("Kursleitungen")
        ordering = ['course', 'display_nr']

    def __unicode__(self):
        """
        The courseownership is shown as <course> <user>
        RETURN: ownership record representation
        """
        return u'%s %s' % (self.course, self.user)

    def get_absolute_url(self):
        """
        absolute url for courseownership relation
        RETURN: relative url
        """
        return reverse('coursebackend:course:detail',
                       kwargs={'course_slug': self.course.slug, 'pk': self.pk})

    def clean(self):
        """
        at least on user profile must have display=True, so that there is a
        user profile available for the public page of the course
        """
        if not self.display:
            if not CourseOwner.objects.other_teachers_for_display(
                    course=self.course,
                    user=self.user):
                raise ValidationError(_('''Wenigstens ein Lehrerprofil pro
                    Kurs muss in der Kurs-Ausschreibung angezeigt werden.'''))
