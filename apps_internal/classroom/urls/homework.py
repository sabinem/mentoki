# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.homework import HomeWorkListView, StudentsWorkDetailView, StudentsWorkCommentView


urlpatterns = patterns('',

    url(r'^(?P<pk>\d{1,4})$', HomeWorkListView.as_view(),
        {'template':'classroom/homework/pages/list.html'}, name='list'),

    url(r'^(?P<pk>\d{1,4})/student/(?P<work_pk>\d{1,4})$', StudentsWorkDetailView.as_view(),
        {'template':'classroom/homework/pages/studentswork.html'}, name='studentswork'),

    url(r'^(?P<pk>\d{1,4})/student/(?P<work_pk>\d{1,4})/kommentieren$', StudentsWorkCommentView.as_view(),
        {'template':'classroom/homework/pages/comment.html'}, name='comments'),
    )
