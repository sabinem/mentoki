# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.forum import ForumStartView, ForumDetailView, ForumDeleteView,\
   ForumCreateView, ForumUpdateView


urlpatterns = patterns("apps_data.course.views.forum",

    url(r'^$', ForumStartView.as_view(),
        name='start'),

    url(r'^(?P<pk>\d{1,4})$', ForumDetailView.as_view(),
        name='detail'),

    url(r'^(?P<pk>\d{1,4})/bearbeiten$', ForumUpdateView.as_view(),
        name='update'),

    url(r'^anlegen$', ForumCreateView.as_view(),
        name='create'),

    url(r'^(?P<pk>\d{1,4})/loeschen$', ForumDeleteView.as_view(),
        name='delete'),

    )