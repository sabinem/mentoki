# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.homework import HomeWorkListView, HomeWorkDetailView


urlpatterns = patterns("apps.classroom.views.homework",

    url(r'^(?P<pk>\d{1,4})$', HomeWorkListView.as_view(),
        name='list'),

    url(r'^(?P<pk_studentswork>\d{1,4})$', HomeWorkDetailView.as_view(),
        name='detail'),
    )
