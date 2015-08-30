# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import get_object_or_404

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField

from mailqueue.models import MailerMessage


from apps_data.courseevent.models.courseevent import CourseEvent, CourseEventParticipation


class AnnouncementManager(models.Manager):

    def published(self, courseevent):
        return self.filter(courseevent=courseevent,
                           published=True,
                           archive=False
                           ).order_by('-published_at')

    def unpublished(self, courseevent):
        return self.filter(courseevent=courseevent, published=False).\
            order_by('-created')

    def create(self, courseevent, text, title, published=False):
        announcement = Announcement(courseevent=courseevent,
                                    text=text,
                                    title=title,
                                    published=published)
        announcement.save()
        return announcement

def send_announcement(announcement, courseevent, module):
    participants_emails = \
        CourseEventParticipation.objects.learners_emails(courseevent=courseevent)
    send_to_class = ", ".join(participants_emails)
    courseemail = courseevent.email
    context = {
        'courseevent': courseevent,
        'title': announcement.title,
        'text': announcement.text,
        'owners': courseevent.teachers,
        'betreff':  "Neue Nachricht von Mentoki %s" % courseevent.title
    }
    message = get_template('email/announcement/announcement.html').render(Context(context))

    mail_message = MailerMessage()

    mail_message.subject = "Neue Nachricht von %s" % courseevent.title
    mail_message.bcc_address = courseemail
    mail_message.to_address = send_to_class
    mail_message.from_address = courseemail
    mail_message.content = "Neue Nachricht von %s and die Teilnehmer" % courseevent.title
    mail_message.html_content = message
    mail_message.reply_to = courseemail
    mail_message.app = module
    mail_message = mail_message.save()
    announcement = get_object_or_404(Announcement, pk=announcement.pk)
    announcement.mailer_message = mail_message
    announcement.save()

    message = u"""Die Ank\u00fcndigung wurde an die Teilnehmer: %s verschickt. Ausserdem ging
    eine Kopie an die Kursleitung: %s verschickt.""" % (send_to_class, courseemail)
    return message


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
        default=False)
    published_at = MonitorField(
        verbose_name=_("veröffentlicht am"),
        monitor='published',
        when=[True])

    mailer_message = models.ForeignKey(MailerMessage, null=True, blank=True)

    archive=models.BooleanField(
        verbose_name=_("archivieren"),
        default=False)

    objects = AnnouncementManager()

    def __unicode__(self):
        return self.title

    def was_send_to(self):
        MailerMessage.objects


    def get_absolute_url(self):
        return reverse('coursebackend:announcement:detail',
                       kwargs={'course_slug':self.course_slug,
                               'slug':self.slug,
                               'pk':self.pk})


