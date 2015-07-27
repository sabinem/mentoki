# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.studentswork import StudentsWorkDetailView, StudentsWorkListView


urlpatterns = patterns("apps.classroom.views.studentswork",

    url(r'^$', StudentsWorkListView.as_view(),
        name='list'),

    url(r'^(?P<pk>\d{1,4})$', StudentsWorkDetailView.as_view(),
        name='detail'),
    )
