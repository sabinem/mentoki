# coding: utf-8

"""
These are utility functions for mailing announcements.
django_mailqueue is used for the actual mailing.
"""

from __future__ import unicode_literals, absolute_import

from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site
from django.conf import settings

from mailqueue.models import MailerMessage

from apps_data.course.models.course import CourseOwner

import logging
logger = logging.getLogger('email.sendout')

def send_receipt(order, transaction, user, module):

    #send also email to teacher

    student_email = user.email
    courseproduct = order.courseproduct
    courseevent = courseproduct.courseevent
    teachers_emails = \
        list(CourseOwner.objects.teachers_emails(course=courseevent.course))
    bcc_mentoki = [settings.MENTOKI_COURSE_EMAIL]
    bcc_list = bcc_mentoki + teachers_emails
    bcc_send = ", ".join(bcc_list)
    context = {
        'site': Site.objects.get_current(),
        'order': order,
        'user':user,
        'courseevent':courseevent,
        'transaction': transaction,

    }

    message = get_template('email/payment/receipt.html').render(Context(context))

    mail_message = MailerMessage(
       subject = "Buchungsbestätigung für Ihre Buchung bei Mentoki",
       bcc_address = bcc_send,
       to_address = user.email,
       from_address = settings.MENTOKI_COURSE_EMAIL,
       content = "Buchungsbestätigung für den Mentokikurs %s" % courseproduct.name,
       html_content = message,
       reply_to = settings.MENTOKI_COURSE_EMAIL,
       app = module
    )
    mail_message.save()

    logger.info("Auftrag [%s]: Buchungsbestätigung geschickt an [%s], bcc [%s]"
            % (order.id,
               bcc_send,
               user.email,
               ))
    message_send = True

    return message_send

