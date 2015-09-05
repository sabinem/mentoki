# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.classlesson import HomeworkListView


urlpatterns = patterns('',

    url(r'^$', HomeworkListView.as_view(),
        {'template':'coursebackend/classlesson/pages/homeworks.html'}, name='list'),

    )