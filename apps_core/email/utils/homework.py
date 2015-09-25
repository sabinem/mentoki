# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site

from mailqueue.models import MailerMessage

from mentoki.settings import MENTOKI_COURSE_EMAIL

from apps_data.course.models.course import CourseOwner


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

    mail_message = MailerMessage()

    mail_message.subject = courseevent.email_greeting
    mail_message.bcc_address = MENTOKI_COURSE_EMAIL
    mail_message.to_address = send_all
    mail_message.from_address = MENTOKI_COURSE_EMAIL
    mail_message.content = "Arbeit abgegeben %s zur Aufgabe %s" \
                           % (studentswork.title, studentswork.homework)
    mail_message.html_content = message
    mail_message.reply_to = send_all
    mail_message.app = module
    mail_message.save()
    mail_message.save()
    return send_all

