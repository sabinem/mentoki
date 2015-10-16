# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from .utils import payment_event


urlpatterns = patterns('',

    url(r'^payment-event$',
        payment_event)
                       )

