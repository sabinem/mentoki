# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.participant import CourseParticipantListView


urlpatterns = patterns('',
        url(r'^$', CourseParticipantListView.as_view(), name='list'),
        )

