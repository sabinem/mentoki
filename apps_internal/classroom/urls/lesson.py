# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.lesson import LessonDetailView, StepDetailView

urlpatterns = patterns('',
    url(r'^lektion/(?P<pk>\d+)$', LessonDetailView.as_view(), name='detail'),
    url(r'^abschnitt/(?P<pk>\d+)$', StepDetailView.as_view(), name='step'),
)
