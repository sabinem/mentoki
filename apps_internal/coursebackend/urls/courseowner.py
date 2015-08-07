# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.courseowner import CourseOwnerListView, CourseOwnerUpdateView, CourseOwnerDetailView


urlpatterns = patterns('',
    url(r'^$', CourseOwnerListView.as_view(),
        {'template':'coursebackend/courseowner/pages/list.html'}, name='list'),

    url(r'^(?P<pk>\d+)$', CourseOwnerDetailView.as_view(),
        {'template':'coursebackend/courseowner/pages/detail.html'}, name='detail'),

    url(r'^(?P<pk>\d+)/bearbeiten$', CourseOwnerUpdateView.as_view(),
        {'template':'coursebackend/courseowner/pages/update.html'}, name='update'),
)
