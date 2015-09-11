# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.classlesson import ClassBlockDetailView, ClassLessonStartView,\
    ClassLessonDetailView, ClassStepDetailView, ClassLessonStepUpdateView, \
    ClassLessonUpdateView, ClassLessonDeleteView, \
    CopyLessonView, CopyLessonListView


urlpatterns = patterns('',
    url(r'^$', ClassLessonStartView.as_view(),
        {'template':'coursebackend/classlesson/pages/work.html'}, name='start'),

    url(r'^meta$', ClassLessonStartView.as_view(),
        {'template':'coursebackend/classlesson/pages/meta.html'}, name='meta'),

    url(r'^kopieren$', CopyLessonListView.as_view(),
        {'template':'coursebackend/classlesson/pages/copy.html'}, name='copy'),

    url(r'^block/(?P<pk>\d+)$', ClassBlockDetailView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonblock.html'}, name='block'),

    url(r'^lektion/(?P<pk>\d+)$', ClassLessonDetailView.as_view(),
        {'template':'coursebackend/classlesson/pages/lesson.html'}, name='lesson'),

    url(r'^abschnitt/(?P<pk>\d+)$', ClassStepDetailView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonstep.html'}, name='step'),
)


urlpatterns += patterns('',

    url(r'^bearbeiten/lektion/(?P<pk>\d+)$', ClassLessonUpdateView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonupdate.html'}, name='lessonupdate'),

    url(r'^bearbeiten/abschnitt/(?P<pk>\d+)$', ClassLessonStepUpdateView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonstepupdate.html'}, name='stepupdate'),
)

urlpatterns += patterns('',
    url(r'^(?P<pk>\d+)/loeschen$', ClassLessonDeleteView.as_view(),
        {'template':'coursebackend/classlesson/pages/delete.html'}, name='delete'),
)

urlpatterns += patterns('',

    url(r'^(?P<pk>\d+)/kopieren$', CopyLessonView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessoncopy.html'}, name='lessoncopy'),

)