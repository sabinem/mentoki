# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.db import models
from model_utils.models import TimeStampedModel
from apps.courseevent.models import CourseEvent
from django.core.urlresolvers import reverse



class Newsletter(TimeStampedModel):
    """
    Newsletters are stored here.
    """
    title = models.CharField(max_length=100, verbose_name="Thema")
    excerpt = models.TextField(verbose_name="Abstract", default="x")
    text_left = models.TextField(verbose_name="Linke Spalte", default="x")
    text_right = models.TextField(verbose_name="Rechte Spalte", default="x")
    published = models.BooleanField(default=False, verbose_name="jetzt veröffentlichen?")
    published_at_date = models.DateTimeField(null=True, blank=True,
                                             verbose_name="veröffentlicht am")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newsletters:single', args=[str(self.id)])
