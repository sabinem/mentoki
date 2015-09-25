# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site

from mailqueue.models import MailerMessage

from mentoki.settings import MENTOKI_COURSE_EMAIL

from apps_data.courseevent.models.courseevent import CourseEventParticipation
from apps_data.course.models.course import CourseOwner


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

    mail_message = MailerMessage()

    mail_message.subject = courseevent.email_greeting
    mail_message.bcc_address = MENTOKI_COURSE_EMAIL
    mail_message.to_address = send_all
    mail_message.from_address = MENTOKI_COURSE_EMAIL
    mail_message.content = "Neue Nachricht von %s and die Teilnehmer" % courseevent.title
    mail_message.html_content = message
    mail_message.reply_to = send_all
    mail_message.app = module
    mail_message.save()
    announcement.publish(mail_distributor=send_all)
    return send_all

