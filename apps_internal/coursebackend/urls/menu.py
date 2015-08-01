# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.forum import MenuStartView, MenuItemCreateView, MenuItemDeleteView,\
   MenuUpdateView


urlpatterns = patterns("apps_data.course.views.forum",

    url(r'^$', MenuStartView.as_view(),
        name='start'),

    url(r'^(?P<pk>\d{1,4})/bearbeiten$', MenuUpdateView.as_view(),
        name='update'),

    url(r'^anlegen$', MenuItemCreateView.as_view(),
        name='create'),

    url(r'^(?P<pk>\d{1,4})/loeschen$', MenuItemDeleteView.as_view(),
        name='delete'),

    )