# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.participant import CourseParticipantListView, hide_participant, unhide_participant


urlpatterns = patterns('',
    url(r'^$', CourseParticipantListView.as_view(),
        {'template':'coursebackend/participant/pages/list.html'}, name='list'),

    url(r'^(?P<pk>\d+)/hide$', hide_participant,
        name='hide'),

    url(r'^(?P<pk>\d+)/unhide$', unhide_participant,
        name='unhide'),
    )

