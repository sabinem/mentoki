# coding: utf-8

"""
Announcements are the communication between teachers and the class.
Announcements have a lifecycle:
- they may start as drafts: in that stage they are private to the teachers.
they may delete or change them.
- once they are published, they will be visible in the classroom. Also
an email is send to all teachers and the all participants.
- later they may be archived, that means they will no longer be visible in
the classroom.

TODO: what about hidden participants? Is the announcement also sent to them?
should not be. -> check
"""

from __future__ import unicode_literals, absolute_import

from django.db import models, IntegrityError
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField

from froala_editor.fields import FroalaField

from mailqueue.models import MailerMessage

from django.conf import settings

from apps_data.courseevent.models.courseevent import CourseEvent, CourseEventParticipation
from apps_data.course.models.course import CourseOwner

import logging
logger = logging.getLogger(__name__)


class AnnouncementManager(models.Manager):
    """
    Querysets for Announcements
    """
    def archived_announcements(self, courseevent):
        """
        gets all archived announcements, newest announcement first
        RETURN: queryset of Announcements
        """
        return self.filter(courseevent=courseevent,
                           is_archived=True
                           ).order_by('-published_at')

    def published_in_class(self, courseevent):
        """
        get all announcements that are displayed in the class
        (published, but not archived announcements)
        RETURN: queryset of Announcements
        """
        return self.filter(courseevent=courseevent,
                           published=True,
                           is_archived=False
                           ).order_by('-published_at')

    def drafts_in_backend(self, courseevent):
        """
        get all announcements that are only drafts yet
        RETURN: queryset of Announcements
        """
        return self.filter(courseevent=courseevent, published=False).\
            order_by('-created')

    def create(self, courseevent, text, title, mail_distributor="", published=False):
        """
        an anncouncement is created.
        """
        announcement = Announcement(courseevent=courseevent,
                                    text=text,
                                    title=title,
                                    mail_distributor=[],
                                    published=False)
        announcement.save()
        logger.info("[%s] [Ankündigung %s %s]: neu angelegt"
                    % (courseevent, announcement.id, announcement))
        return announcement

def send_announcement(announcement, courseevent, module):
    """
    Send an announcement: it is send to the teachers and the particpants.
    Mentoki is set on CC. Sending uses django-mailqueue, so that send out
    emails are als stored in the database.
    """
    participants_emails = \
        list(CourseEventParticipation.objects.learners_emails(courseevent=courseevent))
    teachers_emails = \
        list(CourseOwner.objects.teachers_emails(course=courseevent.course))
    all_emails = participants_emails + teachers_emails
    send_all = ", ".join(all_emails)

    context = {
        'site': Site.objects.get_current(),
        'courseevent': courseevent,
        'announcement': announcement,
        'owners': courseevent.teachers,
        'betreff':  "Neue Nachricht von Mentoki %s" % courseevent.title
    }
    message = get_template('email/announcement/announcement.html').render(Context(context))

    mail_message = MailerMessage()

    mail_message.subject = "Neue Nachricht von %s" % courseevent.title
    mail_message.bcc_address = settings.MENTOKI_COURSE_EMAIL
    mail_message.to_address = send_all
    mail_message.from_address = settings.MENTOKI_COURSE_EMAIL
    mail_message.content = "Neue Nachricht von %s and die Teilnehmer" % courseevent.title
    mail_message.html_content = message
    mail_message.reply_to = send_all
    mail_message.app = module

    mail_distributer = send_all
    logger.info("[%s] [Ankündigung %s %s]: als email verschickt an %s"
                        % (courseevent,
                           announcement.id,
                           announcement,
                           mail_distributer))
    mail_message.save()
    return mail_distributer


class Announcement(TimeStampedModel):
    """
    Announcements are send out as emails to the class, therefore they can not
    be deleted or changed once they have been sent, but they can be archived.
    They may start as drafts. They are the one to many communication from the
    teachers to the class.
    """
    courseevent = models.ForeignKey(CourseEvent, related_name="courseeventnews")

    title = models.CharField(
        verbose_name=_("Betreff"),
        max_length=100)
    text = FroalaField(
        verbose_name=_("Text"))

    published = models.BooleanField(
        verbose_name=_("veröffentlichen?"),
        help_text=_("""Beim Veröffentlichen wird die Ankündigung an
                    alle Kursteilnehmer und Mentoren verschickt:"""),
        default=False)
    published_at = MonitorField(
        verbose_name=_("veröffentlicht am"),
        monitor='published',
        when=[True])

    is_archived=models.BooleanField(
        verbose_name=_("archivieren"),
        help_text=_("""Archivierte Veröffentlichungen sind im Klassenzimmer
                    nicht mehr zu sehen."""),
        default=False)

    mail_distributor = models.TextField(
        verbose_name=_("Mail-Verteiler"),
        help_text=_("email-Adressen, an die die Ankündigung geschickt wurde"),
        null=True,
        blank=True)

    objects = AnnouncementManager()

    class Meta:
        verbose_name = _("Ankündigung")
        verbose_name_plural = _("Ankündigungen")

    def __unicode__(self):
        """
        Ankündigungen werden durch ihren Titel repräsentiert.
        """
        return self.title


    def get_absolute_url(self):
        """
        absolute urls for an announcement in the coursebackend
        """
        return reverse('coursebackend:announcement:detail',
                       kwargs={'course_slug':self.course_slug,
                               'slug':self.slug,
                               'pk':self.pk})

    def archive_announcement(self):
        """
        archive an announcement, so that is no longer visible
        in the classroom
        """
        logger.info("[%s] [Ankündigung %s %s]: archiviert"
                    % (self.courseevent, self.id, self))
        if not self.published:
            raise IntegrityError('''only published announcements
                                 can get archived''')
        self.is_archived = True
        self.save()

    def unarchive_announcement(self):
        """
        revive an announcement, so that is again visible
        in the classroom
        """
        logger.info("[%s] [Ankündigung %s %s]: unarchiviert"
                    % (self.courseevent, self.id, self))
        self.is_archived = False
        self.save()

    def publish_announcement(self, mail_distributor):
        """
        publish an announcement: publication means 2 things:
        1. an email is send out to the students
        2. the announcement is visible in the classroom
        """
        logger.info("[%s] [Ankündigung %s %s]: veröffentlicht"
                    % (self.courseevent, self.id, self))
        self.mail_distributor = mail_distributor
        self.published = True
        self.save()