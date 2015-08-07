# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.material import MaterialUpdateView, MaterialDeleteView, MaterialCreateView, \
    MaterialListView, MaterialDetailView


urlpatterns = patterns('',

    url(r'^$', MaterialListView.as_view(),
        {'template':'coursebackend/material/pages/list.html'}, name='list'),

    url(r'^(?P<pk>\d+)$', MaterialDetailView.as_view(),
        {'template':'coursebackend/material/pages/detail.html'}, name='detail'),

    url(r'^(?P<pk>\d+)/bearbeiten$', MaterialUpdateView.as_view(),
        {'template':'coursebackend/material/pages/update.html'}, name='update'),

    url(r'^anlegen$', MaterialCreateView.as_view(),
        {'template':'coursebackend/material/pages/create.html'}, name='create'),

    url(r'^(?P<pk>\d+)/loeschen$', MaterialDeleteView.as_view(),
        {'template':'coursebackend/material/pages/delete.html'}, name='delete'),
)
