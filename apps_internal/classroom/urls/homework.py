# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.announcement import AnnouncementListView, AnnouncementDetailView


urlpatterns = patterns("apps.classroom.views.announcement",

    url(r'^$', AnnouncementListView.as_view(),
        name='list'),

    url(r'^(?P<pk>\d{1,4})$', AnnouncementDetailView.as_view(),
        name='detail'),
    )
