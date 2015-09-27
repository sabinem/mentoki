# coding: utf-8

"""
These are utility functions for mailing notifications about
forum posts.

django_mailqueue is used for the actual mailing.
"""

from __future__ import unicode_literals, absolute_import

from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site

from mailqueue.models import MailerMessage

from mentoki.settings import MENTOKI_COURSE_EMAIL
from apps_data.course.models.course import CourseOwner
from apps_data.courseevent.models.forum import Post

import logging
logger = logging.getLogger(__name__)

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
    mail_message = MailerMessage(
       subject = courseevent.email_greeting,
       bcc_address = MENTOKI_COURSE_EMAIL,
       to_address = send_all,
       from_address = MENTOKI_COURSE_EMAIL,
       content = "Neuer Post zum Beitrag %s" % thread.title,
       html_content = message,
       reply_to = None,
       app = module
    )
    mail_message.save()

    logger.info("[%s] [Beitrag %s %s][Post %s %s][Email %s %s]: gesendet an %s"
            % (courseevent,
               thread.id,
               thread.title,
               post.id,
               post.title,
               mail_message.id,
               mail_message,
               send_all))

    return send_all


