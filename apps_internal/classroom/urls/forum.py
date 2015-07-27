# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.forum import ForumDetailView, ForumNewPostsView, \
    ForumThreadView, ForumStartView


urlpatterns = patterns('',
    url(r'^beitrag/(?P<pk>\d+)$', ForumThreadView.as_view(), name='thread'),

    url(r'^$', ForumStartView.as_view(), name='start'),

    url(r'^(?P<pk>\d+)$', ForumDetailView.as_view(), name='detail'),

    url(r'neusteposts$', ForumNewPostsView.as_view(), name='newposts'),
)