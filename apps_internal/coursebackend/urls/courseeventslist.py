# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.course import CourseEventListView


urlpatterns = patterns('',

    url(r'^kursliste$',
        CourseEventListView.as_view(),
        {'template':'coursebackend/course/pages/list.html'}, name='list'),
)