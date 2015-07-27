# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.courseevent import CourseEventDetailView, CourseEventUpdateView


urlpatterns = patterns('',
    url(r'^$',
        CourseEventDetailView.as_view(), name='detail'),

    #choice are the fields allowed for Update by the teachers in a courseevent
    url(r'^(?P<field>title|excerpt|target_group|prerequisites|project|text|structure|video_url|workload|format|nr_weeks|max_participants|status_internal|event_type|start_date)$',
        CourseEventUpdateView.as_view(), name='update'),

)
