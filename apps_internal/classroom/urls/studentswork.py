# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.studentswork import StudentsWorkDetailView, StudentsWorkListView, \
    StudentsWorkUpdateView, StudentsWorkCreateView, StudentsWorkDeleteView, StudentsWorkAddTeamView


urlpatterns = patterns('',

    url(r'^$', StudentsWorkListView.as_view(),
        {'template':'classroom/studentswork/pages/list.html'}, name='list'),

    url(r'^(?P<pk>\d{1,4})$', StudentsWorkDetailView.as_view(),
        {'template':'classroom/studentswork/pages/detail.html'}, name='detail'),

    url(r'^(?P<pk>\d{1,4})/bearbeiten$', StudentsWorkUpdateView.as_view(),
        {'template':'classroom/studentswork/pages/update.html'}, name='update'),

    url(r'^anlegen$', StudentsWorkCreateView.as_view(),
        {'template':'classroom/studentswork/pages/create.html'}, name='create'),

    url(r'^(?P<pk>\d{1,4})/loeschen$', StudentsWorkDeleteView.as_view(),
        {'template':'classroom/studentswork/pages/delete.html'}, name='delete'),

    url(r'^(?P<pk>\d{1,4})/team$', StudentsWorkAddTeamView.as_view(),
        {'template':'classroom/studentswork/pages/addteam.html'}, name='addteam'),
    )
