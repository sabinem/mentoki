# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views import MaterialUpdateView, MaterialDeleteView, MaterialCreateView, \
    MaterialListView, MaterialDetailView


urlpatterns = patterns('',
    url(r'^$', MaterialListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', MaterialDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/bearbeiten$', MaterialUpdateView.as_view(), name='update'),
    url(r'^anlegen$', MaterialCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/loeschen$', MaterialDeleteView.as_view(), name='delete'),
)
