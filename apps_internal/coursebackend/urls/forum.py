# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.forum import ForumListView, ForumDetailView, ForumDeleteView,\
   ForumCreateView, ForumUpdateView


urlpatterns = patterns('',

    url(r'^$', ForumListView.as_view(),
        {'template':'coursebackend/forum/pages/list.html'}, name='list'),

    url(r'^(?P<pk>\d{1,4})$', ForumDetailView.as_view(),
        {'template':'coursebackend/forum/pages/detail.html'}, name='detail'),

    url(r'^(?P<pk>\d{1,4})/bearbeiten$', ForumUpdateView.as_view(),
        {'template':'coursebackend/forum/pages/update.html'}, name='update'),

    url(r'^anlegen$', ForumCreateView.as_view(),
        {'template':'coursebackend/forum/pages/create.html'}, name='create'),

    url(r'^(?P<pk>\d{1,4})/loeschen$', ForumDeleteView.as_view(),
        {'template':'coursebackend/forum/pages/delete.html'}, name='delete'),

    )