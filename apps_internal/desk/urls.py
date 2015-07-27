# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url

from .views import *


urlpatterns = patterns('',
    url(r'^start$', DeskStartView.as_view(), name='start' ),
    url(r'^test$', DeskTestView.as_view(), name='test' ),
)

