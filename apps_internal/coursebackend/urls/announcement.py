# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.announcement import AnnouncementListView


urlpatterns = patterns("apps.course.views.announcement",

    url(r'^$', AnnouncementListView.as_view(),
        name='list'),
    #url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/ankuendigungen/(?P<announcement>\d{1,4})/bearbeiten$', AnnouncementUpdateView.as_view(),
    #    name='update'),
    #url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/ankuendigungen/(?P<announcement>\d{1,4})/loeschen$', AnnouncementDeleteView.as_view(),
    #    name='delete'),
    #url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/ankuendigungen/schreiben$', AnnouncementCreateView.as_view(),
    #    name='create'),
    )
