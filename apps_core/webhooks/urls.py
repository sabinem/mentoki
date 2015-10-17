# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from .providers.hook import ProcessHookView, test_view
from .providers.test import my_webhook_view


urlpatterns = patterns('',

    url(r'^test$',
        ProcessHookView.as_view()),

    url(r'^a$',
        my_webhook_view),
)

