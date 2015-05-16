# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.db import models
from model_utils.models import TimeStampedModel
from django.core.urlresolvers import reverse
from apps.courseevent.models import CourseEvent


class Newsletter(TimeStampedModel):
    """
    Newsletters are appear once a month
    """
    title = models.CharField(max_length=100, verbose_name="Thema")
    # abstract that appears on the list page for newsletters
    excerpt = models.TextField(verbose_name="Abstract", default="x")
    # left newsletter column
    text_left = models.TextField(verbose_name="Linke Spalte", default="x")
    # right newsletter column
    text_right = models.TextField(verbose_name="Rechte Spalte", default="x")
    # indicator whether it is a draft or already published
    published = models.BooleanField(default=False, verbose_name="jetzt veröffentlichen?")
    # if published: this contains the date of publication
    published_at_date = models.DateTimeField(null=True, blank=True,
                                             verbose_name="veröffentlicht am")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newsletters:single', args=[str(self.id)])
