# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.announcement import AnnouncementListView, AnnouncementDetailView,\
   AnnouncementDeleteView, AnnouncementUpdateView, AnnouncementCreateView


urlpatterns = patterns('',

    url(r'^$', AnnouncementListView.as_view(),
        {'template':'coursebackend/announcement/pages/list.html'}, name='list'),

    url(r'^(?P<pk>\d{1,4})$', AnnouncementDetailView.as_view(),
        {'template':'coursebackend/announcement/pages/detail.html'}, name='detail'),

    url(r'^(?P<pk>\d{1,4})/bearbeiten$', AnnouncementUpdateView.as_view(),
        {'template':'coursebackend/announcement/pages/update.html'}, name='update'),

    url(r'^anlegen$', AnnouncementCreateView.as_view(),
        {'template':'coursebackend/announcement/pages/create.html'}, name='create'),

    url(r'^(?P<pk>\d{1,4})/loeschen$', AnnouncementDeleteView.as_view(),
        {'template':'coursebackend/announcement/pages/delete.html'}, name='delete'),

    )
