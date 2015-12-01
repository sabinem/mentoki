# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.course import CourseDetailView, \
    CourseUpdateView, CourseEventListView, alter_courseevent



urlpatterns = patterns('',
    url(r'^$', CourseDetailView.as_view(),
        {'template':'coursebackend/course/pages/detail.html'}, name='detail'),

    #choice are the fields allowed for Update by the teachers in a course
    url(r'^(?P<field>title|excerpt|target_group|prerequisites|project|text|structure)$',
        CourseUpdateView.as_view(),
        {'template':'coursebackend/course/pages/update.html'}, name='update'),

    url(r'^kursliste$',
        CourseEventListView.as_view(),
        {'template':'coursebackend/course/pages/list.html'}, name='list'),

    url(r'^(?P<pk>\d+)/(?P<action>\d+)/$', alter_courseevent,
        name='alter_courseevent'),

)