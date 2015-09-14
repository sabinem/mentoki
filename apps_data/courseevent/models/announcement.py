# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import get_object_or_404
from django.contrib.sites.models import Site

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField

from mailqueue.models import MailerMessage

from mentoki.settings import MENTOKI_COURSE_EMAIL

from apps_data.courseevent.models.courseevent import CourseEvent, CourseEventParticipation
from apps_data.course.models.course import CourseOwner


class AnnouncementManager(models.Manager):

    def archived(self, courseevent):
        return self.filter(courseevent=courseevent,
                           is_archived=True
                           ).order_by('-published_at')

    def published(self, courseevent):
        return self.filter(courseevent=courseevent,
                           published=True,
                           is_archived=False
                           ).order_by('-published_at')

    def classroom(self, courseevent):
        return self.filter(courseevent=courseevent,
                           published=True,
                           is_archived=False
                           ).order_by('-published_at')

    def unpublished(self, courseevent):
        return self.filter(courseevent=courseevent, published=False).\
            order_by('-created')

    def create(self, courseevent, text, title, mail_distributor="", published=False):
        announcement = Announcement(courseevent=courseevent,
                                    text=text,
                                    title=title,
                                    published=published,
                                    mail_distributor=mail_distributor)
        announcement.save()
        return announcement

def send_announcement(announcement, courseevent, module):
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
    mail_message.bcc_address = MENTOKI_COURSE_EMAIL
    mail_message.to_address = send_all
    mail_message.from_address = MENTOKI_COURSE_EMAIL
    mail_message.content = "Neue Nachricht von %s and die Teilnehmer" % courseevent.title
    mail_message.html_content = message
    mail_message.reply_to = send_all
    mail_message.app = module

    mail_distributer = send_all
    print mail_distributer
    mail_message = mail_message.save()
    return mail_distributer


class Announcement(TimeStampedModel):
    """
    Announcements are send out as emails to the class, therefor they can not be deleted or changed
    once send
    """
    courseevent = models.ForeignKey(CourseEvent, related_name="courseeventnews")

    title = models.CharField(
        verbose_name=_("Betreff"),
        max_length=100)
    text = models.TextField(
        verbose_name=_("Text"))

    published = models.BooleanField(
        verbose_name=_("veröffentlichen?"),
        help_text=_("""Beim Veröffentlichen wird die Ankündigung an alle Kursteilnehmer
        und Mentoren verschickt:
        """),
        default=False)
    published_at = MonitorField(
        verbose_name=_("veröffentlicht am"),
        monitor='published',
        when=[True])

    is_archived=models.BooleanField(
        verbose_name=_("archivieren"),
        help_text=_("""Archivierte Veröffentlichungen sind im Klassenzimmer nicht mehr zu sehen.
        """),
        default=False)

    mail_distributor = models.TextField(MailerMessage, null=True, blank=True)

    objects = AnnouncementManager()

    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('coursebackend:announcement:detail',
                       kwargs={'course_slug':self.course_slug,
                               'slug':self.slug,
                               'pk':self.pk})

    def archive(self):
        self.is_archived = True
        self.save()

    def unarchive(self):
        self.is_archived = False
        self.save()

    def publish(self, mail_distributor):
        self.mail_distributor = mail_distributor
        self.published = True
        self.save()