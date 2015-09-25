# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site

from mailqueue.models import MailerMessage

from mentoki.settings import MENTOKI_COURSE_EMAIL
from apps_data.course.models.course import CourseOwner
from apps_data.courseevent.models.forum import Post


def send_post_notification(post, thread, courseevent, module):

    course = courseevent.course
    thread_emails = \
        list(Post.objects.contributors_emails(thread=thread))
    teachers_emails = \
        list(CourseOwner.objects.teachers_emails(course=course))
    all_emails = set(thread_emails + teachers_emails)
    send_all = (", ".join(all_emails))


    context = {
        'site': Site.objects.get_current(),
        'courseevent': courseevent,
        'post': post,
        'thread': thread,
        'betreff':  courseevent.email_greeting
    }
    message = get_template('email/forum/newpost.html').render(Context(context))

    mail_message = MailerMessage()

    mail_message.subject = courseevent.email_greeting
    mail_message.bcc_address = MENTOKI_COURSE_EMAIL
    mail_message.to_address = send_all
    mail_message.from_address = MENTOKI_COURSE_EMAIL
    mail_message.content = "Neuer Post zum Beitrag %s" % thread.title
    mail_message.html_content = message
    mail_message.reply_to = None
    mail_message.app = module
    mail_message.save()
    return send_all


