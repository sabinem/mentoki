# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.announcement import AnnouncementListView, AnnouncementDetailView


urlpatterns = patterns('',

    url(r'^$', AnnouncementListView.as_view(),
        {'template':'classroom/announcement/pages/list.html'}, name='list'),

    url(r'^(?P<pk>\d{1,4})$', AnnouncementDetailView.as_view(),
         {'template':'classroom/announcement/pages/detail.html'}, name='detail'),
    )