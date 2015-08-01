# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.homework import HomeworkStartView, HomeworkDetailView, HomeworkDeleteView,\
   HomeworkCreateView, HomeworkUpdateView


urlpatterns = patterns("apps_data.course.views.forum",

    url(r'^$', HomeworkStartView.as_view(),
        name='start'),

    url(r'^(?P<pk>\d{1,4})$', HomeworkDetailView.as_view(),
        name='detail'),

    url(r'^(?P<pk>\d{1,4})/bearbeiten$', HomeworkUpdateView.as_view(),
        name='update'),

    url(r'^anlegen$', HomeworkCreateView.as_view(),
        name='create'),

    url(r'^(?P<pk>\d{1,4})/loeschen$', HomeworkDeleteView.as_view(),
        name='delete'),

    )