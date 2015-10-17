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
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from froala_editor.fields import FroalaField

import logging
logger = logging.getLogger(__name__)


def foto_location(instance, filename):
        """
        location where the banner is stored
        IN: filename
        RETURN: path mentoki-pubic/<filename>
        """
        title = 'mentoki-public'
        path = '/'.join([title, filename])
        logger.info("""[%s] [filename %s]:
                    Foto gespeichert unter %s"""
                    % (title,  filename, path))
        return path

class PublicTextChunks(TimeStampedModel):
    """
    General text chunks like agb, etc.
    """
    pagecode = models.CharField(
        'Code',
        max_length=20,
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
    banner = models.ImageField(
        verbose_name=_('Banner'),
        help_text=_('''Hier kannst Du ein Foto für Deinen Kurs hochladen.'''),
        upload_to=foto_location, blank=True
    )

    class Meta:
        verbose_name = 'Text für Webseite'
        verbose_name_plural = 'Texte für Webseite'

    def __unicode__(self):
        return self.pagecode