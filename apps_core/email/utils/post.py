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
from django.conf import settings

from mailqueue.models import MailerMessage

from apps_data.course.models.course import CourseOwner
from apps_data.courseevent.models.forum import Post
from apps_data.notification.models.classroomnotification import ClassroomNotification
from accounts.models import User

import logging
logger = logging.getLogger(__name__)

def send_post_notification(post, thread, courseevent, module):

    course = courseevent.course
    #contributors_ids = Post.objects.contributors_ids(thread=thread)
    #contributors = User.objects.filter(id__in=contributors_ids)

    #for contributor in contributors:
    #    ClassroomNotification.objects.create(
    #        user = contributor,
    #        courseevent=courseevent,
    #        thread = post.thread,
    #        description = "Neuer Post zum Beitrag %s." %
    #            thread.title
    #    )


    thread_emails = \
        list(Post.objects.contributors_emails(thread=thread))
    thread_emails.append(thread.author.email)
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

    mail_message = MailerMessage(
       subject = "%s: Forum" % courseevent.title,
       bcc_address = settings.MENTOKI_COURSE_EMAIL,
       to_address = send_all,
       from_address = settings.MENTOKI_COURSE_EMAIL,
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


