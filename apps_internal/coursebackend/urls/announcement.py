# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.announcement import AnnouncementListView, AnnouncementDetailView,\
   AnnouncementDeleteView, AnnouncementUpdateView, AnnouncementCreateView


urlpatterns = patterns("apps_data.course.views.announcement",

    url(r'^$', AnnouncementListView.as_view(),
        name='list'),

    url(r'^(?P<pk>\d{1,4})$', AnnouncementDetailView.as_view(),
        name='detail'),

    url(r'^(?P<pk>\d{1,4})/bearbeiten$', AnnouncementUpdateView.as_view(),
        name='update'),

    url(r'^anlegen$', AnnouncementCreateView.as_view(),
        name='create'),

    url(r'^(?P<pk>\d{1,4})/loeschen$', AnnouncementDeleteView.as_view(),
        name='delete'),

    )
