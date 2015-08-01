# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.plain import PlainListView


urlpatterns = patterns('',

    url(r'^$', PlainListView.as_view(),
        {'template':'classroom/plain.html'})
)
