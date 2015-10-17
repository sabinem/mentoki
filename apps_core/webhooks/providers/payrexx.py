# coding: utf-8

"""
These are utility functions for mailing announcements.
django_mailqueue is used for the actual mailing.
"""

from __future__ import unicode_literals, absolute_import

import json

from django.http import HttpResponse
from django.views.generic import View

from braces.views import CsrfExemptMixin
import logging
logger = logging.getLogger(__name__)

class PayrexxProcessHookView(CsrfExemptMixin, View):
    def post(self, request, args, *kwargs):
        print(json.loads(request.body))
        return HttpResponse()
