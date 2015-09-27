# coding: utf-8

"""
These are utility functions for mailing turnedin homeworks.

django_mailqueue is used for the actual mailing.
"""

from __future__ import unicode_literals, absolute_import

from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site

from mailqueue.models import MailerMessage

from mentoki.settings import MENTOKI_COURSE_EMAIL

from apps_data.course.models.course import CourseOwner

import logging
logger = logging.getLogger(__name__)


def send_work_published_notification(studentswork, courseevent, module):

    workers_emails = \
        list(studentswork.workers_emails())
    teachers_emails = \
        list(CourseOwner.objects.teachers_emails(course=courseevent.course))
    all_emails = set(workers_emails + teachers_emails)
    send_all = ", ".join(all_emails)

    context = {
        'site': Site.objects.get_current(),
        'courseevent': courseevent,
        'studentswork': studentswork,
        'homework': studentswork.homework,
        'betreff':  courseevent.email_greeting
    }

    message = get_template('email/homework/newhomework.html').render(Context(context))

    mail_message = MailerMessage(
       subject = courseevent.email_greeting,
       bcc_address = MENTOKI_COURSE_EMAIL,
       to_address = send_all,
       from_address = MENTOKI_COURSE_EMAIL,
       content = "Arbeit abgegeben %s zur Aufgabe %s" \
                           % (studentswork.title, studentswork.homework),
       html_content = message,
       reply_to = None,
       app = module
    )
    mail_message.save()

    logger.info("[%s] [Arbeit %s %s][Email %s %s]: gesendet an %s"
            % (courseevent,
               studentswork.id,
               studentswork.title,
               mail_message.id,
               mail_message,
               send_all))

    return send_all

