# coding: utf-8

"""
Notification Profile:
Der Benutzer kann einstellen über was er benachrichtigt werden will
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from apps_data.courseevent.models.courseevent import CourseEvent


import logging
logger = logging.getLogger('data.userprofile')


class NotificationProfileManager(models.Manager):
    def per_user_and_courseevent(self, user, courseevent):
        """
        Benachrichtigung per Benutzer und Kursereignis
        """
        return self.filter(user=user, courseevent=courseevent)\
            .select_related('user').\
            order_by('display_nr')


class NotificationProfile(TimeStampedModel):
    """
    Benachrichtigungsprofil
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Benachrichtigungsprofil"),
        on_delete=models.PROTECT
    )
    courseevent = models.ForeignKey(CourseEvent, blank=True, null=True)
    classroom_all = models.BooleanField(default=False)
    announcements = models.BooleanField(default=True)
    forum_all = models.BooleanField(default=False)
    forum_involved = models.BooleanField(default=False)
    studentswork_all = models.BooleanField(default=False)
    studentswork_involved = models.BooleanField(default=True)


    objects = NotificationProfileManager()

    class Meta:
        verbose_name = _("Benachrichtigungsprofil")
        verbose_name_plural = _("Benachrichtigungsprofile")

    def __unicode__(self):
        """
        Benachrichtigung für Kursereignis
        """
        return u'%s' % (self.user)

