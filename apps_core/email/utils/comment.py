# coding: utf-8

"""
These are utility functions for mailing comments to studentsworks.
django_mailqueue is used for the actual mailing.
"""

from __future__ import unicode_literals, absolute_import

from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site

from mailqueue.models import MailerMessage

from django.conf import settings

from apps_data.courseevent.models.courseevent import CourseEventParticipation
from apps_data.course.models.course import CourseOwner
from apps_data.courseevent.models.homework import StudentsWork, Comment

import logging
logger = logging.getLogger(__name__)


def send_work_comment_notification(studentswork, comment, courseevent, module):

    commenters_emails = \
        list(Comment.objects.commentors_emails(studentswork=studentswork))
    workers_emails = \
        list(studentswork.workers_emails())
    notification_all_emails = \
        list(CourseEventParticipation.objects.forum_notification_all_emails(courseevent=courseevent))
    notification_none_emails = \
        list(CourseEventParticipation.objects.forum_notification_none_emails(courseevent=courseevent))
    teachers_emails = \
        list(CourseOwner.objects.teachers_emails(course=courseevent.course))
    all_emails = set(commenters_emails + workers_emails + teachers_emails + notification_all_emails)
    notifify_emails = all_emails - set(notification_none_emails)
    send_all = ", ".join(notifify_emails)

    context = {
        'site': Site.objects.get_current(),
        'courseevent': courseevent,
        'studentswork': studentswork,
        'homework': studentswork.homework,
        'comment': comment,
        'betreff':  courseevent.email_greeting
    }

    message = get_template('email/homework/newcomment.html').render(Context(context))

    mail_message = MailerMessage(
       subject = "%s: Aufgaben" % courseevent.title,
       bcc_address = settings.MENTOKI_COURSE_EMAIL,
       to_address = send_all,
       from_address = settings.MENTOKI_COURSE_EMAIL,
       content = "Neuer Kommentar von %s zur Aufgabe %s" \
                           % (comment.author, studentswork.homework),
       html_content = message,
       reply_to = None,
       app = module
    )

    mail_message.save()

    logger.info("[%s] [Arbeit %s %s][Kommentar %s %s][Email %s %s]: gesendet an %s"
            % (courseevent,
               studentswork.id,
               studentswork.title,
               comment.id,
               comment.title,
               mail_message.id,
               mail_message,
               send_all))

    return send_all

