# coding: utf-8

from __future__ import unicode_literals, absolute_import

import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from model_utils.models import TimeStampedModel
from model_utils.managers import QueryManager
from model_utils.managers import PassThroughManager
from model_utils.fields import StatusField, MonitorField
from model_utils import Choices

from apps_data.course.models import Course, CourseOwner


class CourseEventQuerySet(QuerySet):

    def courseevents_for_course(self, course):
        return self.filter(course=course)

    def courseevents_for_course_slug(self, course_slug):
        return self.select_related('course').filter(course__slug=course_slug)

    def get_courseevent_or_404_from_slug(self, slug):
        return get_object_or_404(self, slug=slug)

    def studying(self, user):
        study_courseevent_ids = \
            ParticipationQuerySet.learning(user=self.request.user).\
                values_list('courseevent_id', flat=True)
        return self.select_related('course').\
                filter(id__in=study_courseevent_ids).order_by('start_date')

    def is_teacher(self, user):
        if user in self.teachers:
            return True
        else:
            return False

class CourseEvent(TimeStampedModel):

    course = models.ForeignKey(Course)

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)

    start_date = models.DateField(null=True, blank=True, verbose_name="Startdatum")
    nr_weeks = models.IntegerField(null=True, blank=True, verbose_name="Wochenanzahl")

    max_participants = models.IntegerField(null=True, blank=True, verbose_name="Teilnehmeranzahl")

    EVENT_TYPE = Choices(('gg', 'guidedgroup', _('geführter Gruppenkurs')),
                         ('sl', 'selflearn', _('Selbstlernen'))
                        )
    event_type  =  models.CharField(max_length=2, choices=EVENT_TYPE, default=EVENT_TYPE.selflearn)

    STATUS_EXTERNAL = Choices(('0', 'not_public', _('not public')),
                              ('1', 'booking', _('open for booking')),
                              ('2', 'preview', _('open for preview'))
                             )
    status_external =  models.CharField(max_length=2, choices=STATUS_EXTERNAL, default=STATUS_EXTERNAL.not_public)
    published_at = MonitorField(monitor='status_external', when=['public'])
    opened_at = MonitorField(monitor='status_external', when=['booking'])

    STATUS_INTERNAL = Choices(('0', 'draft', _('not public')),
                              ('1', 'review', _('open for booking')),
                              ('a', 'accepted', _('open for preview'))
                             )
    status_internal =  models.CharField(max_length=2, choices=STATUS_INTERNAL, default=STATUS_INTERNAL.draft)
    accepted_at = MonitorField(monitor='status_external', when=['accepted'])
    review_ready_at = MonitorField(monitor='status_external', when=['review'])

    excerpt = models.TextField(blank=True, verbose_name="Abstrakt")
    video_url = models.CharField(max_length=100, blank=True, verbose_name="Kürzel des Videos bei You Tube ")
    text = models.TextField(blank=True, verbose_name="freie Kursbeschreibung")
    format = models.TextField(blank=True, verbose_name="Kursformat")
    workload = models.TextField(blank=True, verbose_name="Arbeitsbelastung")
    project = models.TextField(blank=True,  verbose_name="Teilnehmernutzen")
    structure = models.TextField(blank=True,  verbose_name="Gliederung")
    target_group = models.TextField(blank=True, verbose_name="Zielgruppe")
    prerequisites = models.TextField(blank=True, verbose_name="Voraussetzungen")

    objects = PassThroughManager.for_queryset_class(CourseEventQuerySet)()
    public_ready_for_booking = QueryManager(status_external=STATUS_EXTERNAL.booking)
    public_ready_for_preview = QueryManager(status_external=STATUS_EXTERNAL.preview)

    participation = models.ManyToManyField(settings.AUTH_USER_MODEL, through="CourseEventParticipation", related_name='participation')

    #participants = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.title

    @cached_property
    def course_slug(self):
        return self.course.slug

    @cached_property
    def course_title(self):
        return self.course.title

    @cached_property
    def teachers(self):
        return self.course.teachers

    @cached_property
    def teachersrecord(self):
        return self.course.teachersrecord

    @cached_property
    def end_date(self):
        """
        calculate the end date form the startdate and the number of weeks if a startdate is given.
        """
        if self.start_date:
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

    #def get_absolute_url(self):
    #    return reverse('coursebackend:courseevent:detail', kwargs={'course_slug':self.course_slug, 'slug':self.slug})


class ParticipationQuerySet(QuerySet):

    def learning(self, user):
        return self.filter(user=user)

    def learners(self, course):
        return self.filter(course=course).select_related('user')


class CourseEventParticipation(TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    objects = PassThroughManager.for_queryset_class(ParticipationQuerySet)()

    def __unicode__(self):
        return u'%s / %s' % (self.courseevent, self.user)











