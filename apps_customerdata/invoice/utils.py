# coding: utf-8

"""
These are utility functions for mailing turnedin homeworks.

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
logger = logging.getLogger(__name__)


def payment_event(self):
    """
    payrexx payment success
    :return:
    """
    return True

