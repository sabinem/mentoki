# coding: utf-8

"""
TO DO: use with chunks template tags
https://github.com/clintecker/django-chunks/blob/master/chunks/templatetags/chunks.py
"""
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.core.urlresolvers import reverse
from apps_data.courseevent.models.courseevent import CourseEvent
from django_markdown.models import MarkdownField
from model_utils.models import TimeStampedModel

from froala_editor.fields import FroalaField


class PublicTextChunks(TimeStampedModel):
    """
    General text chunks like agb, etc.
    """
    pagecode = models.CharField(
        'Code',
        max_length=10,
        primary_key=True)
    text =  FroalaField(
        'text'
    )
    title = models.CharField(
        'Titel',
        max_length=200
    )
    description = models.CharField(
        'description',
        max_length=250
    )

    class meta:
        verbose_name = "Texte für allgemeine Seiten"

    def __unicode__(self):
        return self.pagecode