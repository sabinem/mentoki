# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns("apps.classroom.views.announcement",

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/ankuendigungen$', AnnouncementsListView.as_view(),
        name='list'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/ankuendigungen/(?P<announcement>\d{1,4})/bearbeiten$', AnnouncementUpdateView.as_view(),
        name='detail'),

    )
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/ankuendigungen$', AnnouncementsListView.as_view(), name='start'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/ankuendigungen/(?P<id>\d{1,4})/$',
        AnnouncementDetailView.as_view(), name='announcementdetail'),