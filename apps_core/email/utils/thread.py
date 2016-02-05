# coding: utf-8

"""
These are utility functions for mailing notifications about
forum threads.

django_mailqueue is used for the actual mailing.
"""

from __future__ import unicode_literals, absolute_import

from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site
from django.conf import settings

from mailqueue.models import MailerMessage

from apps_data.course.models.course import CourseOwner
from apps_data.courseevent.models.courseevent import CourseEventParticipation

import logging
logger = logging.getLogger(__name__)


def send_thread_notification(author, thread, forum, courseevent, module):

    course = courseevent.course
    notification_all_emails = \
        list(CourseEventParticipation.objects.forum_notification_all_emails(courseevent=courseevent))
    teachers_emails = \
        list(CourseOwner.objects.teachers_emails(course=course))
    all_emails = set(notification_all_emails + teachers_emails)
    send_all = (", ".join(all_emails))

    context = {
        'site': Site.objects.get_current(),
        'courseevent': courseevent,
        'author': author,
        'thread': thread,
        'betreff': courseevent.email_greeting
    }

    message = get_template('email/forum/newthread.html').render(Context(context))

    mail_message = MailerMessage(
       subject = "%s: Forum" % courseevent.title,
       bcc_address = settings.MENTOKI_COURSE_EMAIL,
       to_address = send_all,
       from_address = settings.MENTOKI_COURSE_EMAIL,
       content = "Neuer Beitrag im Forum %s" % forum.title,
       html_content = message,
       reply_to = None,
       app = module
    )
    mail_message.save()

    logger.info("[%s] [Forum %s %s][Beitrag %s %s][Email %s %s]: gesendet an %s"
            % (courseevent,
               forum.id,
               forum.title,
               thread.id,
               thread.title,
               mail_message.id,
               mail_message,
               send_all))

    return send_all


def send_thread_delete_notification(author, thread, forum, courseevent, module):

    course = courseevent.course
    teachers_emails = \
        list(CourseOwner.objects.teachers_emails(course=course))
    all_emails = set(teachers_emails + [author.email])
    send_all = ", ".join(all_emails)

    context = {
        'site': Site.objects.get_current(),
        'courseevent': courseevent,
        'author': author,
        'thread': thread,
        'betreff': courseevent.email_greeting
    }

    message = get_template('email/forum/deletedthread.html').render(Context(context))

    mail_message = MailerMessage(
       subject = "%s: Forum" % courseevent.title,
       bcc_address = settings.MENTOKI_COURSE_EMAIL,
       to_address = send_all,
       from_address = settings.MENTOKI_COURSE_EMAIL,
       content = "%s hat seinen Beitrag %s gelöscht" % (author.username, thread.title),
       html_content = message,
       reply_to = None,
       app = module
    )

    mail_message.save()

    logger.info("[%s] [Forum %s %s][Beitrag gelöscht %s %s][Email %s %s]: gesendet an %s"
            % (courseevent,
               forum.id,
               forum.title,
               thread.id,
               thread.title,
               mail_message.id,
               mail_message,
               send_all))

    return send_all