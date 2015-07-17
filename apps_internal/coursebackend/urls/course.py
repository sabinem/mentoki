# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views import CourseDetailView, CourseUpdateView


urlpatterns = patterns('',
    url(r'^$', CourseDetailView.as_view(), name='detail'),

    url(r'^feld/(?P<field>[a-z_]+)$',
        CourseUpdateView.as_view(), name='update'),
)
