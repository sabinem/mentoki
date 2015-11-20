# coding: utf-8

"""
Seiteninformation für öffentlich zugängliche statische Seiten:
 - Texte
 - Banner
 - HTML Meta Informationen
"""
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from model_utils.models import TimeStampedModel

from froala_editor.fields import FroalaField

from apps_data.courseevent.models.courseevent import CourseEvent

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


class StaticPublicPages(TimeStampedModel):
    """
    Public visible pages: each chunk corresponds to one page. It can be found
    by its unique page code.
    """
    pagecode = models.CharField(
        verbose_name=_('Seitencode'),
        help_text=_('Der Seitencode ordnet die Textchunks eindeutig '
                    'zu html Seiten zu. Die Views greifen die Seiten '
                    'über den Seitencode ab.'),
        max_length=20,
        primary_key=True
    )
    text =  FroalaField(
        verbose_name=_('Textchunk'),
        help_text=_('Dieser Text wird als html chunk auf '
                    'der Seite integriert. Der pagecode ordnet die Seite zu'),
        blank=True
    )
    title = models.CharField(
        verbose_name=_('Seitentitel'),
        help_text=_('Der Seitentitel wird ebenfalls benutzt zum Aufbau der  '
                    'zugeordenten html Seite'),
        max_length=200,
        blank=True
    )
    description = models.CharField(
        verbose_name=_('interne Beschreibung der Seite'),
        help_text=_('wird nicht nach aussen angezeigt.'),
        max_length=250
    )
    banner = models.ImageField(
        verbose_name=_('Banner'),
        help_text=_('Optional kann ein Banner hochgeladen werden, dass nach'
        ' aussen angezeigt werden kann.'),
        upload_to=foto_location,
        blank=True
    )
    meta_keywords = models.CharField(
        verbose_name=_('Meta Keywords'),
        help_text=_('HTML Meta Information zur Seite.'),
        max_length=250
    )
    meta_description = models.CharField(
        verbose_name=_('Meta Description'),
        help_text=_('HTML Meta Information zur Seite.'),
        max_length=250
    )
    meta_title = models.CharField(
        verbose_name=_('Meta Titel'),
        help_text=_('HTML Meta Information zur Seite.'),
        max_length=250
    )
    slug = models.SlugField(blank=True, null=True)
    template_name = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Öffentliche statische Seite'
        verbose_name_plural = 'Öffentliche statische Seiten'

    def __unicode__(self):
        return self.pagecode

    def get_absolute_url(self):
        return reverse_lazy('home:public',
                       kwargs={'slug': self.slug})