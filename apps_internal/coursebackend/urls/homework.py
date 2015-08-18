# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.homework import HomeworkListView, HomeworkDetailView, HomeworkDeleteView,\
   HomeworkCreateView, HomeworkUpdateView


urlpatterns = patterns('',

    url(r'^$', HomeworkListView.as_view(),
        {'template':'coursebackend/homework/pages/list.html'}, name='list'),

    url(r'^(?P<pk>\d{1,4})$', HomeworkDetailView.as_view(),
        {'template':'coursebackend/homework/pages/detail.html'}, name='detail'),

    url(r'^(?P<pk>\d{1,4})/bearbeiten$', HomeworkUpdateView.as_view(),
        {'template':'coursebackend/homework/pages/update.html'}, name='update'),

    url(r'^anlegen$', HomeworkCreateView.as_view(),
        {'template':'coursebackend/homework/pages/create.html'}, name='create'),

    url(r'^(?P<pk>\d{1,4})/loeschen$', HomeworkDeleteView.as_view(),
        {'template':'coursebackend/homework/pages/delete.html'}, name='delete'),

    )