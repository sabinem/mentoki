# coding: utf-8

"""
These are utility functions for mailing announcements.
django_mailqueue is used for the actual mailing.
"""

from __future__ import unicode_literals, absolute_import

from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site
from django.conf import settings

from mailqueue.models import MailerMessage

from apps_data.courseevent.models.courseevent import CourseEventParticipation
from apps_data.course.models.course import CourseOwner

import logging
logger = logging.getLogger(__name__)

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
        'betreff':  courseevent.email_greeting
    }

    message = get_template('email/announcement/announcement.html').render(Context(context))

    mail_message = MailerMessage(
       subject = courseevent.email_greeting,
       bcc_address = settings.MENTOKI_COURSE_EMAIL,
       to_address = send_all,
       from_address = settings.MENTOKI_COURSE_EMAIL,
       content = "Neue Nachricht von %s and die Teilnehmer" % courseevent.title,
       html_content = message,
       reply_to = send_all,
       app = module
    )
    mail_message.save()

    logger.info("[%s] [Ankündigung %s %s][Email %s %s]: gesendet an %s"
            % (courseevent,
               announcement.id,
               announcement.title,
               mail_message.id,
               mail_message,
               send_all))

    announcement.publish_announcement(mail_distributor=send_all)

    return send_all

