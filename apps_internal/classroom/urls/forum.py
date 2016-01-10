# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.forum import ForumStartView, ForumRecentView, ForumDetailView
from ..views.post import PostCreateView
from ..views.thread import ThreadCreateView, ThreadUpdateView, ThreadDeleteView

urlpatterns = patterns('',
    url(r'^beitrag/(?P<pk>\d+)$', PostCreateView.as_view(),
        {'template':'classroom/forum/pages/threadcreatepost.html'}, name='thread'),

    url(r'^(?P<pk>\d+)/beitrag/anlegen$', ThreadCreateView.as_view(),
        {'template':'classroom/forum/pages/createthread.html'}, name='thread_create'),

    url(r'^beitrag/(?P<pk>\d+)/aendern$', ThreadUpdateView.as_view(),
        {'template':'classroom/forum/pages/updatethread.html'}, name='thread_update'),

    url(r'^beitrag/(?P<pk>\d+)/loeschen$', ThreadDeleteView.as_view(),
        {'template':'classroom/forum/pages/deletethread.html'}, name='thread_delete'),

    url(r'^start$', ForumStartView.as_view(),
        {'template':'classroom/forum/pages/start.html'}, name='start'),

    url(r'^(?P<pk>\d+)$', ForumDetailView.as_view(),
        {'template':'classroom/forum/pages/forum.html'}, name='detail'),

    url(r'^neueste-beitraege$', ForumRecentView.as_view(),
        {'template':'classroom/forum/pages/contributions.html'}, name='newposts'),
)
