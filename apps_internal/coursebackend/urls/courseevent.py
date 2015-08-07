# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.courseevent import CourseEventDetailView, CourseEventUpdateView, CourseEventListView


urlpatterns = patterns('',

    url(r'^liste$',
        CourseEventListView.as_view(),
        {'template':'coursebackend/courseevent/pages/list.html'}, name='list'),

    url(r'^(?P<slug>[a-z0-9_-]+)/$',
        CourseEventDetailView.as_view(),
        {'template':'coursebackend/courseevent/pages/detail.html'}, name='detail'),

    #choice are the fields allowed for Update by the teachers in a courseevent
    url(r'^(?P<slug>[a-z0-9_-]+)/(?P<field>title|excerpt|target_group|prerequisites|project|text|structure|video_url|workload|format|nr_weeks|max_participants|status_internal|event_type|start_date)$',
        CourseEventUpdateView.as_view(),
        {'template':'coursebackend/courseevent/pages/update.html'}, name='update'),

)
