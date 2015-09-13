# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.classlesson import ClassLessonDetailView, ClassLessonStepDetailView,\
    ClassLessonStartView, StudentsWorkDetailView, StudentsWorkCommentView


urlpatterns = patterns('',

    url(r'^$', ClassLessonStartView.as_view(),
        {'template':'classroom/classlesson/pages/start.html'}, name='start'),

    url(r'^lektion/(?P<pk>\d+)$', ClassLessonDetailView.as_view(),
        {'template': 'classroom/classlesson/pages/lesson.html'}, name='lesson'),

    url(r'^abschnitt/(?P<pk>\d+)$', ClassLessonStepDetailView.as_view(),
        {'template':'classroom/classlesson/pages/lessonstep.html'}, name='step'),

    url(r'^abschnitt/(?P<pk>\d+)/abgegeben/(?P<work_pk>\d{1,4})$',
        StudentsWorkDetailView.as_view(),
        {'template':'classroom/classlesson/pages/studentswork.html'}, name='studentswork'),

    url(r'^abschnitt/(?P<pk>\d+)/abgegeben/(?P<work_pk>\d{1,4})/kommentieren$',
        StudentsWorkCommentView.as_view(),
        {'template':'classroom/classlesson/pages/comment.html'}, name='comment'),
)
