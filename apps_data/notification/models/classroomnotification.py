# coding: utf-8

"""
Mentors are users that teach courses.
Here are their profile data stored. These data are
displayed on public pages.
"""

from __future__ import unicode_literals, absolute_import

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.conf import settings


from model_utils.models import TimeStampedModel

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.courseevent.models.forum import Thread
from ..constants import NotificationType
from django_enumfield import enum

import logging
logger = logging.getLogger('data.userprofile')


class ClassroomNotificationManager(models.Manager):
    def notification_by_user(self, user):
        """
        Notification Manager
        """
        return self.filter(user=user)\
            .select_related('thread').\
            order_by('created')


class ClassroomNotification(TimeStampedModel):
    """
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    courseevent = models.ForeignKey(CourseEvent, blank=True, null=True)
    notification_type = enum.EnumField(
        NotificationType,
        default=NotificationType.POST_CREATED,
    )
    thread = models.ForeignKey(
        Thread,
        blank=True,
        null=True)
    description = models.TextField(
        verbose_name="Beschreibung",
    )

    objects = ClassroomNotificationManager()

    class Meta:
        verbose_name = _("Benachrichtigung")
        verbose_name_plural = _("Benachrichtigungen")

    def __unicode__(self):
        """
        The courseownership is shown as <course> <user>
        RETURN: ownership record representation
        """
        return u'%s' % (self.user)
