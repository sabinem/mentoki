# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# import from 3rd party apps
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from apps.courseevent.models import CourseEvent
# import from other apps
from apps.core.helpers import timesince


class Contact(TimeStampedModel):
    """
    Contacts are stored together with their data
    """
    # each course has a slug
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField()
    # these field sum up to the description of the course
    message = models.TextField(blank=True, verbose_name="Deine Nachricht")
    projecttitle = models.CharField(max_length=100, verbose_name='Titel für Dein Kursprojekt', blank=True)
    projectdescription = models.TextField(verbose_name='Beschreibe Dein Kursprojekt', blank=True)
    qualification = models.TextField(verbose_name='Was qualifiziert Dich dafür?', blank=True)
    courseevent = models.ForeignKey(CourseEvent, blank=True, null=True, verbose_name='Welcher Kurs interessiert Dich?')
    contactinfo = models.TextField(verbose_name='Wie können wir Dich erreichen?', blank=True)
    motivation = models.TextField(verbose_name='Warum brennst Du für dieses Thema?', blank=True)
    priorexperience = models.TextField(verbose_name='Hast Du schon Unterrichtserfahrungen online oder im Präsenzunterricht?', blank=True)

    CONTACT_GENERAL ='0'
    CONTACT_TEACHER = '1'
    CONTACT_STUDENT = '2'
    CONTACTTYPE = (
        (CONTACT_GENERAL, 'Allgemein'),
        (CONTACT_TEACHER, 'Starterkurs'),
        (CONTACT_STUDENT, 'Kursvorbuchung'),
    )
    contacttype = models.CharField(choices=CONTACTTYPE, default=CONTACT_GENERAL, max_length=2)

    def __unicode__(self):
        # the course is represented by its title
        return u'%s' % (self.name)
