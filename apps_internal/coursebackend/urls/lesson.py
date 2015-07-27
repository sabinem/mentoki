# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.lesson import LessonBlockView, LessonStartView,\
    LessonDetailView, StepDetailView, \
    LessonUpdateView, LessonCreateView, LessonDeleteView, LessonAddMaterialView, LessonMoveView


urlpatterns = patterns('',
    url(r'^$', LessonStartView.as_view(), name='start'),

    url(r'^block/(?P<pk>\d+)$', LessonBlockView.as_view(), name='block'),
    url(r'^lektion/(?P<pk>\d+)$', LessonDetailView.as_view(), name='detail'),
    url(r'^abschnitt/(?P<pk>\d+)$', StepDetailView.as_view(), name='step'),

    url(r'^(?P<pk>\d+)/bearbeiten$', LessonUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/bewegen$', LessonMoveView.as_view(), name='move'),
    url(r'^anlegen$', LessonCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/loeschen$', LessonDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/material$', LessonAddMaterialView.as_view(), name='material'),
)
