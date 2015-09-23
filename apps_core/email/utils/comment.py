# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site

from mailqueue.models import MailerMessage

from mentoki.settings import MENTOKI_COURSE_EMAIL

from apps_data.courseevent.models.courseevent import CourseEventParticipation
from apps_data.course.models.course import CourseOwner
from apps_data.courseevent.models.homework import StudentsWork, Comment


def send_work_comment_notification(studentswork, comment, courseevent, module):
    commenters_emails = \
        list(Comment.objects.commentors_emails(studentswork=studentswork))
    workers_emails = \
        list(studentswork.workers_emails())
    teachers_emails = \
        list(CourseOwner.objects.teachers_emails(course=courseevent.course))
    all_emails = commenters_emails + workers_emails + teachers_emails
    send_all = ", ".join(all_emails)
    context = {
        'site': Site.objects.get_current(),
        'courseevent': courseevent,
        'studentswork': studentswork,
        'homework': studentswork.homework,
        'comment': comment,
        'betreff':  "Neue Nachricht von Mentoki %s" % courseevent.title
    }
    message = get_template('email/homework/newcomment.html').render(Context(context))

    mail_message = MailerMessage()

    mail_message.subject = "Neue Nachricht von %s" % courseevent.title
    mail_message.bcc_address = MENTOKI_COURSE_EMAIL
    mail_message.to_address = send_all
    mail_message.from_address = MENTOKI_COURSE_EMAIL
    mail_message.content = "Neuer Kommentar von %s zur Aufgabe %s" \
                           % (comment.author, studentswork.homework)
    mail_message.html_content = message
    mail_message.reply_to = send_all
    mail_message.app = module
    mail_message.save()
    mail_message.save()
    return send_all

