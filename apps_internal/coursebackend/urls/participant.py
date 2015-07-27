# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.participants import CourseParticipantsListView


urlpatterns = patterns('',
        url(r'^$', CourseParticipantsListView.as_view(), name='list'),
        )

