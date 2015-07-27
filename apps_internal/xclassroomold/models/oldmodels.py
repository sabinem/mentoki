# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.db import models
from model_utils.models import TimeStampedModel
from apps_data.courseevent.models import CourseEvent


class Announcement(TimeStampedModel):
    """
    Announcements are stored here.
    """
    courseevent = models.ForeignKey(CourseEvent, related_name="kurs")
    title = models.CharField(max_length=100, verbose_name="Thema")
    text = models.TextField(verbose_name="Text der Ankündigung: Vorsicht Bilder werden noch nicht mitgeschickt")
    published = models.BooleanField(default=False, verbose_name="jetzt veröffentlichen?")
    published_at_date = models.DateTimeField(null=True, blank=True,
                                             verbose_name="veröffentlicht am")

    def __unicode__(self):
        return self.title


class ClassRules(TimeStampedModel):
    """
    Rules are stored here.
    """
    courseevent = models.ForeignKey(CourseEvent, related_name="regel")
    title = models.CharField(max_length=100)
    excerpt = models.TextField(default="x")
    text = models.TextField()
    DOC_STATUS_DRAFT ='0'
    DOC_STATUS_PUBLISHED = '1'
    DOC_STATUS = (
        (DOC_STATUS_DRAFT, 'Entwurf'),
        (DOC_STATUS_PUBLISHED, 'oeffentlich'),
    )
    status = models.CharField(choices=DOC_STATUS, default=DOC_STATUS_DRAFT, max_length=2)

    def __unicode__(self):
        return self.title

    def valid_since(self):
        return self.published_at_date
