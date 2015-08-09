# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.lesson import BlockDetailView, LessonStartView,\
    LessonDetailView, StepDetailView, LessonWorkView, BlockUpdateView, LessonStepUpdateView, \
    LessonUpdateView, LessonDeleteView, \
    BlockCreateView, LessonCreateView, LessonStepCreateView


urlpatterns = patterns('',
    url(r'^$', LessonStartView.as_view(),
        {'template':'coursebackend/lesson/pages/start.html'}, name='start'),

    url(r'^block/(?P<pk>\d+)$', BlockDetailView.as_view(),
        {'template':'coursebackend/lesson/pages/lessonblock.html'}, name='block'),

    url(r'^lektion/(?P<pk>\d+)$', LessonDetailView.as_view(),
        {'template':'coursebackend/lesson/pages/lesson.html'}, name='lesson'),

    url(r'^abschnitt/(?P<pk>\d+)$', StepDetailView.as_view(),
        {'template':'coursebackend/lesson/pages/lessonstep.html'}, name='step'),
)


urlpatterns += patterns('',
    url(r'^bearbeiten$', LessonWorkView.as_view(),
        {'template':'coursebackend/lesson/pages/work.html'}, name='work'),

    url(r'^bearbeiten/block/(?P<pk>\d+)/bearbeiten$', BlockUpdateView.as_view(),
        {'template':'coursebackend/lesson/pages/lessonblockupdate.html'}, name='blockupdate'),

    url(r'^bearbeiten/lektion/(?P<pk>\d+)/bearbeiten$', LessonUpdateView.as_view(),
        {'template':'coursebackend/lesson/pages/lessonupdate.html'}, name='lessonupdate'),

    url(r'^bearbeiten/abschnitt/(?P<pk>\d+)/bearbeiten$', LessonStepUpdateView.as_view(),
        {'template':'coursebackend/lesson/pages/lessonstepupdate.html'}, name='stepupdate'),
)

urlpatterns += patterns('',
    url(r'^(?P<pk>\d+)/loeschen$', LessonDeleteView.as_view(),
        {'template':'coursebackend/lesson/pages/delete.html'}, name='delete'),
)

urlpatterns += patterns('',

    url(r'^anlegen/block/(?P<pk>\d+)/bearbeiten$', BlockCreateView.as_view(),
        {'template':'coursebackend/lesson/pages/lessonblockupdate.html'}, name='blockupdate'),

    url(r'^anlegen/lektion/(?P<pk>\d+)/bearbeiten$', LessonCreateView.as_view(),
        {'template':'coursebackend/lesson/pages/lessonupdate.html'}, name='lessonupdate'),

    url(r'^anlegen/abschnitt/(?P<pk>\d+)/bearbeiten$', LessonStepCreateView.as_view(),
        {'template':'coursebackend/lesson/pages/lessonstepupdate.html'}, name='stepupdate'),
)