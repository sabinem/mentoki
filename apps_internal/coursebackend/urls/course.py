# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.course import CourseDetailView, CourseUpdateView


urlpatterns = patterns('',
    url(r'^$', CourseDetailView.as_view(), name='detail'),

    #choice are the fields allowed for Update by the teachers in a course
    url(r'^(?P<field>title|excerpt|target_group|prerequisites|project|text|structure)$',
        CourseUpdateView.as_view(), name='update'),
)