# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views import CourseOwnerListView, CourseOwnerUpdateView


urlpatterns = patterns('',
    url(r'^$', CourseOwnerListView.as_view(), name='list'),

    url(r'^(?P<pk>\d+)$',
        CourseOwnerUpdateView.as_view(), name='update'),
)
