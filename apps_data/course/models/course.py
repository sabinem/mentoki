# coding: utf-8

"""
Courses are the timeindependent representation of Courses.
In this file there are two classes: the database representation of Courses
and the many-to-many relationship of Courses to Owners: these are the teachers
teaching the courses, that are the only persons eligible to change their data.

TODO:
1. is the email account for the course still needed?
2. Course Attribute "teachers_emails" seems to deliver the same result as
   CourseOwner queryset "teachers_emails"?
3. CourseOwner queryset "other_teachers_for_display" should be replaced by a
   count.

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

from mentoki.settings import MENTOKI_INFO_EMAIL


class Course(TimeStampedModel):
    """
    Courses are the central model of the Application. They gather all the
    material for teaching the subject without any regards to the actual event
    of teaching that material to students.
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
    email = models.EmailField(
        verbose_name=_("email Addresse für den Kurs"),
        help_text=_("""Die email-Adresse des Kursleiters oder eine
                    Mentoki-Adresse. Bitte stimme diese Adresse mit
                    Mentoki ab."""),
        default=MENTOKI_INFO_EMAIL
    )

    class Meta:
        verbose_name = _("Kursvorlage")
        verbose_name_plural = _("Kursvorlagen")

    def __unicode__(self):
        return u'%s' % (self.title)

    @cached_property
    def teachers(self):
        """
        Returns all the accounts of users who are involved with teaching that
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
        gets all teachers that are selected for showing their profiles
        on the public page of the course; includes user-data
        IN: Course
        RETURN: CourseOwner-queryset
        """
        return self\
            .filter(course=course, display=True).select_related('user')\
            .order_by('display_nr')

    def teachers_courseinfo_all(self, course):
        """
        get all teachers ownershiprecords of a course including their user data
        IN: Course
        RETURN: CourseOwner-queryset
        """
        return self\
            .filter(course=course).select_related('user')\
            .order_by('display_nr')

    def other_teachers_for_display(self, course, user):
        """
        check whether there are teachers records from other users then the
        given user for the course.
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
        RETURN: string
        """
        return u'%s %s' % (self.course, self.user)

    def get_absolute_url(self):
        """
        absolute url for courseownership relation
        RETURN: string
        """
        return reverse('coursebackend:course:detail',
                       kwargs={'course_slug': self.course_slug, 'pk': self.pk})

    def clean(self):
        """
        at least on user profile must have display=True, so that it is
        displayed on the public page of the course
        """
        if not self.display:
            if not CourseOwner.objects.other_teachers_for_display(
                    course=self.course,
                    user=self.user):
                raise ValidationError(_('''Wenigstens ein Lehrerprofil pro
                    Kurs muss in der Kurs-Ausschreibung angezeigt werden.'''))