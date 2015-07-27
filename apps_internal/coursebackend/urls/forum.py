# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.forum import ForumStartView, ForumDetailView


urlpatterns = patterns('',

    url(r'^$', ForumStartView.as_view(), name='start'),

    url(r'^(?P<pk>\d+)$', ForumDetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/bearbeiten$', ForumUpdateView.as_view(), name='update'),
    #url(r'^(?P<pk>\d+)/bewegen$', ForumMoveView.as_view(), name='move'),
    #url(r'^anlegen$', ForumCreateView.as_view(), name='create'),
    #url(r'^(?P<pk>\d+)/loeschen$', ForumDeleteView.as_view(), name='delete'),
)