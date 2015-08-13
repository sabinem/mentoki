# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.lesson_course import BlockDetailView, LessonStartView,\
    LessonDetailView, StepDetailView, LessonWorkView, BlockUpdateView, LessonStepUpdateView, \
    LessonUpdateView, LessonDeleteView, \
    BlockCreateView, LessonCreateView, LessonStepCreateView


urlpatterns = patterns('',
    url(r'^$', LessonStartView.as_view(),
        {'template':'coursebackend/lesson_course/pages/start.html'}, name='start'),

    url(r'^block/(?P<pk>\d+)$', BlockDetailView.as_view(),
        {'template':'coursebackend/lesson_course/pages/lessonblock.html'}, name='block'),

    url(r'^lektion/(?P<pk>\d+)$', LessonDetailView.as_view(),
        {'template':'coursebackend/lesson_course/pages/lesson.html'}, name='lesson'),

    url(r'^abschnitt/(?P<pk>\d+)$', StepDetailView.as_view(),
        {'template':'coursebackend/lesson_course/pages/lessonstep.html'}, name='step'),
)


urlpatterns += patterns('',
    url(r'^bearbeiten$', LessonWorkView.as_view(),
        {'template':'coursebackend/lesson_course/pages/work.html'}, name='work'),

    url(r'^bearbeiten/block/(?P<pk>\d+)$', BlockUpdateView.as_view(),
        {'template':'coursebackend/lesson_course/pages/lessonblockupdate.html'}, name='blockupdate'),

    url(r'^bearbeiten/lektion/(?P<pk>\d+)$', LessonUpdateView.as_view(),
        {'template':'coursebackend/lesson_course/pages/lessonupdate.html'}, name='lessonupdate'),

    url(r'^bearbeiten/abschnitt/(?P<pk>\d+)$', LessonStepUpdateView.as_view(),
        {'template':'coursebackend/lesson_course/pages/lessonstepupdate.html'}, name='stepupdate'),
)

urlpatterns += patterns('',
    url(r'^(?P<pk>\d+)/loeschen$', LessonDeleteView.as_view(),
        {'template':'coursebackend/lesson_course/pages/delete.html'}, name='delete'),
)

urlpatterns += patterns('',

    url(r'^anlegen/block$', BlockCreateView.as_view(),
        {'template':'coursebackend/lesson_course/pages/lessonblockupdate.html'}, name='blockcreate'),

    url(r'^anlegen/lektion$', LessonCreateView.as_view(),
        {'template':'coursebackend/lesson_course/pages/lessonupdate.html'}, name='lessoncreate'),

    url(r'^anlegen/abschnitt$', LessonStepCreateView.as_view(),
        {'template':'coursebackend/lesson_course/pages/lessonstepupdate.html'}, name='stepcreate'),
)