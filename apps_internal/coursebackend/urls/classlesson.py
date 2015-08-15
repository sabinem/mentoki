# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.classlesson import BlockDetailView, LessonStartView,\
    LessonDetailView, StepDetailView, LessonStepUpdateView, \
    LessonUpdateView, LessonDeleteView, \
    CopyLessonView, CopyLessonListView


urlpatterns = patterns('',
    url(r'^$', LessonStartView.as_view(),
        {'template':'coursebackend/classlesson/pages/work.html'}, name='start'),

    url(r'^kopieren$', CopyLessonListView.as_view(),
        {'template':'coursebackend/classlesson/pages/copy.html'}, name='copy'),

    url(r'^block/(?P<pk>\d+)$', BlockDetailView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonblock.html'}, name='block'),

    url(r'^lektion/(?P<pk>\d+)$', LessonDetailView.as_view(),
        {'template':'coursebackend/classlesson/pages/lesson.html'}, name='lesson'),

    url(r'^abschnitt/(?P<pk>\d+)$', StepDetailView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonstep.html'}, name='step'),
)


urlpatterns += patterns('',

    url(r'^bearbeiten/lektion/(?P<pk>\d+)$', LessonUpdateView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonupdate.html'}, name='lessonupdate'),

    url(r'^bearbeiten/abschnitt/(?P<pk>\d+)$', LessonStepUpdateView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonstepupdate.html'}, name='stepupdate'),
)

urlpatterns += patterns('',
    url(r'^(?P<pk>\d+)/loeschen$', LessonDeleteView.as_view(),
        {'template':'coursebackend/classlesson/pages/delete.html'}, name='delete'),
)

urlpatterns += patterns('',

    url(r'^(?P<pk>\d+)/kopieren$', CopyLessonView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessoncopy.html'}, name='lessoncopy'),

)