# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.lesson import LessonDetailView, StepDetailView, LessonStartView

urlpatterns = patterns('',

    url(r'^$', LessonStartView.as_view(),
        {'template':'classroom/lesson/pages/start.html'}, name='start'),

    url(r'^lektion/(?P<pk>\d+)$', LessonDetailView.as_view(),
        {'template': 'classroom/lesson/pages/lesson.html'}, name='detail'),

    url(r'^abschnitt/(?P<pk>\d+)$', StepDetailView.as_view(),
        {'template':'classroom/lesson/pages/lessonstep.html'}, name='step'),
)
