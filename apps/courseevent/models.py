# coding: utf-8
from __future__ import unicode_literals, absolute_import
# import from python
import datetime
# import from django
from django.db import models
from django.contrib.auth.models import User
# import from thrid party
from model_utils.models import TimeStampedModel
# import from other apps
from apps.course.models import Course, CourseUnit, CourseOwner


class CourseEvent(TimeStampedModel):
    """
    The courseevent is the unit that can be booked by stundents
    """
    # every courseevent builds upon a course
    course = models.ForeignKey(Course)
    # the slug is used as url for the course
    slug = models.SlugField(unique=True)
    # the title of the course
    title = models.CharField(max_length=100)
    # several describing attributes
    excerpt = models.TextField(blank=True)
    text = models.TextField(blank=True)
    format = models.TextField(blank=True, verbose_name="Kursformat")
    workload = models.TextField(blank=True, verbose_name="Arbeitsbelastung")
    structure = models.TextField(blank=True, verbose_name="Gliederung")
    project = models.TextField(default="x",blank=True)
    # startdate and nr of weeks if this applies
    start_date = models.DateField(null=True, blank=True)
    nr_weeks = models.IntegerField(null=True, blank=True)
    # maximal nr of participants if this applies
    max_participants = models.IntegerField(null=True, blank=True)
    # type of the courseevent
    EVENTTYPE_TIMED_COURSE ='0'
    EVENTTYPE_FORUM = '1'
    EVENTTYPE_SELFLEARN_ATTENDED = '2'
    EVENTTYPE_SELFLEARN_UNATTENDED = '3'
    EVENTTYPE_CHOICES = (
        (EVENTTYPE_TIMED_COURSE, 'geführter Gruppenkurs'),
        (EVENTTYPE_FORUM, 'internes Diskussionsforum / ohne Termin / nicht gelistet '),
        (EVENTTYPE_SELFLEARN_ATTENDED, 'unbegleitetes Selbstlernen / ohne Termin'),
        (EVENTTYPE_SELFLEARN_UNATTENDED, 'begleitetes Selbstlernen / ohne Termin'),
    )
    event_type = models.CharField(choices=EVENTTYPE_CHOICES, default=EVENTTYPE_TIMED_COURSE, max_length=2)
    # external status of the event
    EXTEVENT_UNPUBLISHED ='0'
    EXTEVENT_PREVIEW = '1'
    EXTEVENT_OPEN_FOR_BOOKING = '2'
    EXTEVENT_BOOKING_CLOSED = '3'
    EXTEVENT_FINISHED = '4'
    EXTEVENT_CHOICES = (
        (EXTEVENT_UNPUBLISHED, u'noch unveröffentlicht'),
        (EXTEVENT_PREVIEW, u'Vorankündigung'),
        (EXTEVENT_OPEN_FOR_BOOKING, 'zur Buchung geöffnet'),
        (EXTEVENT_BOOKING_CLOSED, 'Buchung abgeschlossen'),
        (EXTEVENT_FINISHED, 'Kursereignis abgeschlossen'),
    )
    status_external = models.CharField(choices=EXTEVENT_CHOICES, default=EXTEVENT_UNPUBLISHED, max_length=2)
    # this status is not needed any more
    INTEVENT_OPEN = '0'
    INTEVENT_DRAFT  = '1'
    INTEVENT_CLOSED = '2'
    INTEVENT_CHOICES = (
        (INTEVENT_DRAFT, 'im Aufbau'),
        (INTEVENT_OPEN, 'zur internen Buchung geoeffnet'),
        (INTEVENT_CLOSED, 'keine interne Buchung mehr moeglich'),
    )
    status_internal = models.CharField(choices=INTEVENT_CHOICES, default=INTEVENT_DRAFT, max_length=2)

    def __unicode__(self):
        return self.title

    @property
    def end_date(self):
        """
        calculate the end date form the startdate and the number of weeks if a startdate is given.
        :return:
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



class CourseeventUnitPublish(models.Model):
    """
    Units are published one by one in a class. Publication is decided on the level of the
    course unit. See app course for details.
    """
    courseevent = models.ForeignKey(CourseEvent)
    unit = models.ForeignKey(CourseUnit)
    published_at_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s / %s' % (self.courseevent, self.unit)


class CourseEventParticipation(TimeStampedModel):
    """
    Participation in courseevent means students study there.
    """
    courseevent = models.ForeignKey(CourseEvent)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s / %s' % (self.courseevent, self.user)


class CourseEventPubicInformation(TimeStampedModel):
    """
    Participation in courseevent means students study there.
    """
    courseevent = models.ForeignKey(CourseEvent)
    excerpt = models.TextField(blank=True)
    text = models.TextField(blank=True, verbose_name="freie Kursbeschreibung, überschreibt die allgemeine "
                                                     "Kursbeschreibung, wenn ausgefüllt")
    format = models.TextField(blank=True, verbose_name="Kursformat")
    workload = models.TextField(blank=True, verbose_name="Arbeitsbelastung")
    project = models.TextField(blank=True,  verbose_name="Teilnehmernutzen, überschreibt die allgemeine "
                                                     "Kursbeschreibung, wenn ausgefüllt")
    structure = models.TextField(blank=True,  verbose_name="Gliederung")
    target_group = models.TextField(blank=True, verbose_name="Zielgruppe, , überschreibt die allgemeine "
                                                     "Kursbeschreibung, wenn ausgefüllt")
    prerequisites = models.TextField(blank=True, verbose_name="Voraussetzungen, , überschreibt die allgemeine "
                                                     "Kursbeschreibung, wenn ausgefüllt")

    def __unicode__(self):
        return u'%s' % (self.courseevent)