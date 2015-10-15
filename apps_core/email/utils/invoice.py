# coding: utf-8

"""
These are utility functions for mailing notifications about
forum posts.

django_mailqueue is used for the actual mailing.
"""

from __future__ import unicode_literals, absolute_import

import urllib
from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site
from django.conf import settings

from mailqueue.models import MailerMessage

from apps_data.course.models.course import CourseOwner
from apps_data.courseevent.models.forum import Post

from collections import OrderedDict

urllib.urlencode(OrderedDict([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')]))
# Out: 'k1=v1&k2=v2&k3=v3'

import logging
logger = logging.getLogger(__name__)

def send_invoice(invoice, module):
    print "invoice in send_invoice %s" % invoice

    betreff = "Ihre Bestellung: Mentokis %s" % invoice.product.courseevent.title
    url_parms = urllib.urlencode(OrderedDict([
        ('tid', invoice.payrexx_tld),
        ('invoice_amount', invoice.amount),
        ('invoice_currency', invoice.currency),
        ('contact_forename',invoice.first_name),
        ('contact_surname',invoice.last_name),
        ('invoice_number',invoice.title ),
        ('contact_email',invoice.email),
    ]))

    #url_input = {
    #      'tid': invoice.payrexx_tld,
    #      'invoice_amount' : invoice.amount,
    #      'invoice_currency' : invoice.currency,
    #      'contact_forename': invoice.first_name,
    #      'contact_surname': invoice.last_name,
    #      'invoice_number' : invoice.title,
    #
    #      }

    #url_parms = urllib.urlencode(url_input)
    print url_parms
    context = {
        'site': Site.objects.get_current(),
        'pay_site': settings.PAYREXX_SITE,
        'product': invoice.product,
        'betreff': betreff,
        'invoice': invoice,
        'url_parms':url_parms
    }

    message = get_template('email/invoice/payment_link.html').render(Context(context))

    mail_message = MailerMessage()
    mail_message = MailerMessage(
       subject = betreff,
       bcc_address = settings.MENTOKI_COURSE_EMAIL,
       to_address = invoice.email,
       from_address = settings.MENTOKI_COURSE_EMAIL,
       content = "Neuer Kunde: Zahlungslink verschickt an %s über %s: Rechnungsnr. %s" %
                 (invoice.email, invoice.product.courseevent.title, invoice.invoice_nr),
       html_content = message,
       reply_to = None,
       app = 'module'
    )
    mail_message.save()

    logger.info("[%s %s %s %s  gesendet an %s"
            % (invoice.product,
               invoice.email,
               invoice.invoice_nr,
               invoice.currency,
               invoice.email))
    return