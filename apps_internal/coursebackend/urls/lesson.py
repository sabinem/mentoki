# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.lesson import LessonBlockView, LessonStartView,\
    LessonDetailView, StepDetailView, \
    LessonUpdateView, LessonCreateView, LessonDeleteView, LessonAddMaterialView, LessonMoveView


urlpatterns = patterns('',
    url(r'^$', LessonStartView.as_view(),
        {'template':'coursebackend/lesson/pages/start.html'}, name='start'),

    url(r'^block/(?P<pk>\d+)$', LessonBlockView.as_view(),
        {'template':'coursebackend/lesson/pages/list.html'}, name='block'),

    url(r'^lektion/(?P<pk>\d+)$', LessonDetailView.as_view(),
        {'template':'coursebackend/lesson/pages/list.html'}, name='detail'),

    url(r'^abschnitt/(?P<pk>\d+)$', StepDetailView.as_view(),
        {'template':'coursebackend/lesson/pages/list.html'}, name='step'),

    url(r'^(?P<pk>\d+)/bearbeiten$', LessonUpdateView.as_view(),
        {'template':'coursebackend/lesson/pages/list.html'}, name='update'),

    url(r'^(?P<pk>\d+)/bewegen$', LessonMoveView.as_view(),
        {'template':'coursebackend/lesson/pages/list.html'}, name='move'),

    url(r'^anlegen$', LessonCreateView.as_view(),
        {'template':'coursebackend/lesson/pages/list.html'}, name='create'),

    url(r'^(?P<pk>\d+)/loeschen$', LessonDeleteView.as_view(),
        {'template':'coursebackend/lesson/pages/list.html'}, name='delete'),

    url(r'^(?P<pk>\d+)/material$', LessonAddMaterialView.as_view(),
        {'template':'coursebackend/lesson/pages/list.html'}, name='material'),
)
