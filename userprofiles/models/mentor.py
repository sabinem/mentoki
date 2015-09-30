# coding: utf-8

"""
Courses are the timeindependent representation of Lessons.
In this file there are two classes: the database representation of Courses
and the many-to-many relationship of Courses to Owners: these are the teachers
teaching the courses, that are the only persons eligible to change their data.
"""
from __future__ import unicode_literals, absolute_import

from django.db import models

from django.conf import settings
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError

from model_utils.models import TimeStampedModel

from autoslug import AutoSlugField

import logging
logger = logging.getLogger(__name__)


def foto_location(instance, filename):
        """
        location where the teachers foto is stored
        IN: CourseOwner, filename
        RETURN: path <course-slug>/<filename>
        """
        path = '/'.join([instance.user.username, filename])
        logger.info("""[%s] [filename %s]:
                    Foto gespeichert unter %s"""
                    % (instance.user,  filename, path))
        return path


class MentorsProfile(TimeStampedModel):
    """
    Relationship of Courses to Users through the Relationship of teaching
    / owning the course.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Mentor"),
        on_delete=models.PROTECT
    )
    at_mentoki = models.CharField(
        verbose_name=_('Rolle bei Mentoki'),
        blank=True,
        max_length=200,
    )
    special_power = models.CharField(
        verbose_name=_('Spezielle Eigenschaft'),
        blank=True,
        max_length=200,
    )
    text = models.TextField(
        verbose_name=_('ausführliche Beschreibung'),
        blank=True
    )
    foto = models.ImageField(
        verbose_name=_('Foto'),
        help_text=_('''Hier kannst Du ein Foto von Dir hochladen.'''),
        upload_to=foto_location, blank=True
    )
    display_nr = models.IntegerField(
        verbose_name=_('Anzeigereihenfolge'),
    )

    class Meta:
        verbose_name = _("Mentor")
        verbose_name_plural = _("Mentoren")

    def __unicode__(self):
        """
        The courseownership is shown as <course> <user>
        RETURN: ownership record representation
        """
        return u'%s' % (self.user)
