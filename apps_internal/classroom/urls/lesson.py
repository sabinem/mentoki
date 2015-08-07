# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.lesson import LessonDetailView, LessonStepDetailView, LessonStartView, \
    LessonBlockDetailView

urlpatterns = patterns('',

    url(r'^$', LessonStartView.as_view(),
        {'template':'classroom/lesson/pages/start.html'}, name='start'),

    url(r'^block/(?P<pk>\d+)$', LessonBlockDetailView.as_view(),
        {'template':'classroom/lesson/pages/lessonblock.html'}, name='lessonblock_detail'),

    url(r'^lektion/(?P<pk>\d+)$', LessonDetailView.as_view(),
        {'template': 'classroom/lesson/pages/lesson.html'}, name='lesson_detail'),

    url(r'^abschnitt/(?P<pk>\d+)$', LessonStepDetailView.as_view(),
        {'template':'classroom/lesson/pages/lessonstep.html'}, name='lessonstep_detail'),
)
