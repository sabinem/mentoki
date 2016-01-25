# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.lessonold import HomeworkListView


urlpatterns = patterns('',

    url(r'^$', HomeworkListView.as_view(),
        {'template':'coursebackend/lesson/pages/homeworks.html'}, name='list'),

    )