# coding: utf-8

from __future__ import unicode_literals, absolute_import

import datetime

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.core.validators import ValidationError

from model_utils.models import TimeStampedModel
from model_utils.managers import QueryManager
from model_utils.fields import MonitorField
from model_utils import Choices

#from django_prices.models import PriceField

from apps_data.course.models.course import Course


#class CourseEventQuerySet(QuerySet):
class CourseEventManager(models.Manager):

    def courseevents_for_course(self, course):
        return self.filter(course=course)

    def active_courseevents_for_course(self, course):
        return self.filter(course=course, active=True)

    def courseevents_for_course_slug(self, course_slug):
        return self.select_related('course').filter(course__slug=course_slug)

    def get_courseevent_or_404_from_slug(self, slug):
        return get_object_or_404(self, slug=slug)

    def is_teacher(self, user):
        if user in self.teachers:
            return True
        else:
            return False


class CourseEvent(TimeStampedModel):

    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT
    )

    slug = models.SlugField(unique=True)

    title = models.CharField(
        verbose_name=_("Kurstitel"),
        help_text=_("Kurstitel unter dem dieser Kurs ausgeschrieben wird."),
        max_length=100)

    start_date = models.DateField(
        verbose_name=_("Startdatum"),
        help_text=_('im Format Tag.Monat.Jahr angeben'),
        null=True, blank=True)

    nr_weeks = models.IntegerField(
        verbose_name=_("Wochenanzahl"),
        help_text=_("Die Anzahl der Wochen, die der Kurs dauern soll, nur bei geführten Kursen."),
        null=True,
        blank=True)

    max_participants = models.IntegerField(
        verbose_name=_("Teilnehmeranzahl"),
        null=True,
        blank=True)

    EVENT_TYPE = Choices(('guided', 'guidedgroup', _('geführter Gruppenkurs')),
                         ('selflearn', 'selflearn', _('Selbstlernen')),
                         ('coached', 'coached', _('Selbstlernen mit Unterstützung'))
                        )
    event_type  =  models.CharField(
        verbose_name="Kursart",
        max_length=12,
        choices=EVENT_TYPE,
        default=EVENT_TYPE.selflearn)

    STATUS_EXTERNAL = Choices(('0', 'not_public', _('nicht öffentlich')),
                              ('1', 'booking', _('zur Buchung geöffnet')),
                              ('1', 'booking_closed', _('Buchung abgeschlossen')),
                              ('2', 'preview', _('Vorschau'))
                             )
    status_external =  models.CharField(
        verbose_name="externer Status",
        max_length=2,
        choices=STATUS_EXTERNAL,
        default=STATUS_EXTERNAL.not_public)
    published_at = MonitorField(monitor='status_external', when=['booking'])
    booking_closed_at = MonitorField(monitor='status_external', when=['booking_closed'])

    active = models.BooleanField(default=True)

    STATUS_INTERNAL = Choices(('0', 'draft', _('nicht veröffentlicht')),
                              ('1', 'review', _('offen')),
                              ('a', 'accepted', _('Vorschau'))
                             )
    status_internal =  models.CharField(
        verbose_name="interner Status",
        max_length=2,
        choices=STATUS_INTERNAL,
        default=STATUS_INTERNAL.draft)
    accepted_at = MonitorField(
        monitor='status_external',
        when=['accepted'])
    review_ready_at = MonitorField(
        monitor='status_external',
        when=['review'])

    # description of the courseevent
    excerpt = models.TextField(verbose_name="Abstrakt",
                               help_text="Diese Zusammenfassung erscheint auf der Kursliste.",
                               blank=True)
    video_url = models.CharField(max_length=100, blank=True, verbose_name="Kürzel des Videos bei You Tube ")
    text = models.TextField(
        verbose_name=_("freie Kursbeschreibung"),
        blank=True)
    format = models.TextField(
        verbose_name=_("Kursformat"),
        blank=True)
    workload = models.TextField(
        verbose_name=_("Arbeitsbelastung"),
        blank=True)
    project = models.TextField(
        verbose_name=_("Teilnehmernutzen"),
        blank=True)
    structure = models.TextField(
        verbose_name=_("Gliederung"),
        blank=True)
    target_group = models.TextField(
        verbose_name=_("Zielgruppe"),
        help_text=_('Zielgruppe, wie sie in der Kursausschreibung erscheinen soll.'),
        blank=True)
    prerequisites = models.TextField(
        verbose_name=_("Voraussetzungen"),
        blank=True)

    #price = PriceField('Price', currency='ECU', max_digits=12, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    #participants
    participation = models.ManyToManyField(settings.AUTH_USER_MODEL, through="CourseEventParticipation", related_name='participation')

    you_okay = models.BooleanField(
        default=True
    )

    #objects = PassThroughManager.for_queryset_class(CourseEventQuerySet)()
    objects = CourseEventManager()
    public_ready_for_booking = QueryManager(status_external=STATUS_EXTERNAL.booking)
    public_ready_for_preview = QueryManager(status_external=STATUS_EXTERNAL.preview)

    def __unicode__(self):
        return self.title

    @cached_property
    def teachers(self):
        return self.course.teachers

    @cached_property
    def teachers_emails(self):
        return self.course.teachers.email

    @property
    def email(self):
        return self.course.email

    @cached_property
    def teachersrecord(self):
        return self.course.teachersrecord

    @cached_property
    def course_slug(self):
        return self.course.slug

    def end_date(self):
        """
        calculate the end date form the startdate and the number of weeks if a startdate is given.
        """
        if self.start_date and self.nr_weeks:
           end_date = self.start_date + datetime.timedelta(days=7*self.nr_weeks)
           return end_date

    @property
    def days_to_start(self):
        today = datetime.date.today()
        try:
            if today < self.start_date:
               # the course has not started yet
               return (self.start_date - today).days
        except:
            return None

    def students(self):
        """
        Returns all the accounts of users who are students in the courseevent
        """
        return self.participation.all().prefetch_related('participation').order_by('username')


    def get_absolute_url(self):
        return reverse('coursebackend:courseevent:detail',
                       kwargs={'course_slug':self.course_slug,
                               'slug':self.slug})

    def clean(self):
        if self.start_date:
            if not self.start_date > datetime.date.today():
                raise ValidationError('Startdatum muss in der Zukunft liegen!')


class ParticipationManager(models.Manager):

    def learning(self, user):
        return self.filter(user=user)

    def learners(self, courseevent):
        return self.filter(courseevent=courseevent).select_related('user')

    def active_learners(self, courseevent):
        return self.filter(courseevent=courseevent, hidden=False).select_related('user')

    def learners_emails(self, courseevent):
        return self.filter(courseevent=courseevent).select_related('user').\
            values_list('user__email', flat=True)

    def active(self,courseevent):
        return self.filter(courseevent=courseevent, hidden=False).select_related('user')


class CourseEventParticipation(TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    hidden = models.BooleanField(
        verbose_name=_('versteckt'),
        default=False)
    hidden_status_changed = MonitorField(monitor='hidden')

    objects = ParticipationManager()

    def __unicode__(self):
        return u'%s / %s' % (self.courseevent, self.user)

    def hide(self):
        self.hidden = True
        self.save()

    def unhide(self):
        self.hidden = False
        self.save()









