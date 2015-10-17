# coding: utf-8

from __future__ import unicode_literals, absolute_import

import json

from django.views.generic import View

from braces.views import CsrfExemptMixin

import logging
logger = logging.getLogger(__name__)

class ProcessHookView(CsrfExemptMixin, View):
    def post(self, request, args, *kwargs):
        print(json.loads(request.body))
        return HttpResponse()

def test_view(request):
    now = datetime.datetime.now()
    print "now"
    html = "<html><body>It is now %s.</body></html>" % now
    print(json.loads(request.body))
    print "HALLO -------------------"
    return HttpResponse()

# Set your secret key: remember to change this to your live secret key in production
# See your keys here https://dashboard.stripe.com/account/apikeys


import json
from django.http import HttpResponse

# Using Django
#@require_POST
#@csrf_exempt

def my_webhook_view(request):
  # Retrieve the request's body and parse it as JSON
  event_json = json.load(request.body)

  # Do something with event_json
  print event_json

  return HttpResponse(status=200)

import json

# Webhooks are always sent as HTTP POST requests, so we want to ensure
# that only POST requests will reach your webhook view. We can do that by
# decorating `webhook()` with `require_POST`.
#
# Then to ensure that the webhook view can receive webhooks, we need
# also need to decorate `webhook()` with `csrf_exempt`.
#@require_POST
#@csrf_exempt
#def webhook(request):
  # Process webhook data in `request.body