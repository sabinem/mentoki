# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.classlesson import ClassBlockDetailView, ClassLessonStartView,\
    ClassLessonDetailView, ClassStepDetailView
from ..views.classlessonupdate import ClassLessonStepUpdateView, \
    ClassLessonUpdateView, ClassLessonDeleteView, ClassLessonBlockUpdateView, \
    ClassLessonCreateView, ClassLessonStepCreateView
from ..views.lesson_to_classlesson import CopyLessonView, CopyBlockListView, \
    ClassLessonBLockUnlockView


urlpatterns = patterns('',
    url(r'^$', ClassLessonStartView.as_view(),
        {'template':'coursebackend/classlesson/pages/work.html'}, name='start'),

    url(r'^meta$', ClassLessonStartView.as_view(),
        {'template':'coursebackend/classlesson/pages/meta.html'}, name='meta'),

    url(r'^kopieren$', CopyBlockListView.as_view(),
        {'template':'coursebackend/classlesson/pages/copy.html'}, name='copy'),

    url(r'^block/(?P<pk>\d+)/entsperren$', ClassLessonBLockUnlockView.as_view(),
        {'template':'coursebackend/classlesson/pages/unlock.html'}, name='unlock'),

    url(r'^block/(?P<pk>\d+)$', ClassBlockDetailView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonblock.html'}, name='block'),

    url(r'^lektion/(?P<pk>\d+)$', ClassLessonDetailView.as_view(),
        {'template':'coursebackend/classlesson/pages/lesson.html'}, name='lesson'),

    url(r'^abschnitt/(?P<pk>\d+)$', ClassStepDetailView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonstep.html'}, name='step'),
)


urlpatterns += patterns('',

    url(r'^bearbeiten/block/(?P<pk>\d+)$', ClassLessonBlockUpdateView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonblockupdate.html'}, name='blockupdate'),

    url(r'^bearb/lektion/(?P<pk>\d+)$', ClassLessonUpdateView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonupdate.html'}, name='lessonupdate'),

    url(r'^bearbeiten/abschnitt/(?P<pk>\d+)$', ClassLessonStepUpdateView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonstepupdate.html'}, name='stepupdate'),
)

urlpatterns += patterns('',

    url(r'^anlegen/lektion$', ClassLessonCreateView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonupdate.html'}, name='lessoncreate'),

    url(r'^anlegen/abschnitt$', ClassLessonStepCreateView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessonstepupdate.html'}, name='stepcreate'),
)


urlpatterns += patterns('',
    url(r'^(?P<pk>\d+)/loeschen$', ClassLessonDeleteView.as_view(),
        {'template':'coursebackend/classlesson/pages/delete.html'}, name='delete'),
)

urlpatterns += patterns('',

    url(r'^(?P<pk>\d+)/kopieren$', CopyLessonView.as_view(),
        {'template':'coursebackend/classlesson/pages/lessoncopy.html'}, name='lessoncopy'),

)