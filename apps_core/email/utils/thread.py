# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site

from mailqueue.models import MailerMessage

from mentoki.settings import MENTOKI_COURSE_EMAIL
from apps_data.course.models.course import CourseOwner
from apps_data.courseevent.models.forum import Thread


def send_thread_notification(author, thread, forum, courseevent, module):

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
        'betreff':  "Neue Nachricht von Mentoki %s" % courseevent.title
    }
    message = get_template('email/forum/newthread.html').render(Context(context))

    mail_message = MailerMessage()

    mail_message.subject = "Neue Nachricht von %s" % courseevent.title
    mail_message.bcc_address = MENTOKI_COURSE_EMAIL
    mail_message.to_address = send_all
    mail_message.from_address = MENTOKI_COURSE_EMAIL
    mail_message.content = "Neuer Beitrag im Forum %s" % forum.title
    mail_message.html_content = message
    mail_message.reply_to = None
    mail_message.app = module
    mail_message.save()
    return send_all
