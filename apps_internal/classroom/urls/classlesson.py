# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.classlesson import ClassLessonDetailView, ClassLessonStepDetailView,\
    ClassLessonStartView


urlpatterns = patterns('',

    url(r'^$', ClassLessonStartView.as_view(),
        {'template':'classroom/classlesson/pages/start.html'}, name='start'),

    url(r'^lektion/(?P<pk>\d+)$', ClassLessonDetailView.as_view(),
        {'template': 'classroom/classlesson/pages/lesson.html'}, name='lesson'),

    url(r'^abschnitt/(?P<pk>\d+)$', ClassLessonStepDetailView.as_view(),
        {'template':'classroom/csslesson/pages/lessonstep.html'}, name='step'),
)
