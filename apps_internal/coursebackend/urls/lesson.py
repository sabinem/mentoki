# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.lesson.copy import LessonCopyView
from ..views.lesson.lesson import LessonUpdateView, LessonCreateView
from ..views.lesson.lessonblock import BlockUpdateView, BlockCreateView
from ..views.lesson.lessonstep import LessonStepUpdateView, LessonStepCreateView
from ..views.lesson.list import BlockListView, BlockLessonsView, HomeworkListView
from ..views.lesson.detail import BlockDetailView, LessonDetailView, StepDetailView
from ..views.lesson.delete import LessonDeleteView

urlpatterns = patterns('',
    url(r'^$', BlockListView.as_view(),
        {'template':'coursebackend/lessontest/pages/view/blocklist.html'},
        name='blocklist'),

    url(r'^mit-lektionen$', BlockLessonsView.as_view(),
        {'template':'coursebackend/lessontest/pages/view/blockswithlessons.html'},
        name='blockswithlessons'),

    url(r'^block/(?P<pk>\d+)$', BlockDetailView.as_view(),
        {'template':'coursebackend/lessontest/pages/view/lessonblock.html'}, name='block'),

    url(r'^lektion/(?P<pk>\d+)$', LessonDetailView.as_view(),
        {'template':'coursebackend/lessontest/pages/view/lesson.html'}, name='lesson'),

    url(r'^abschnitt/(?P<pk>\d+)$', StepDetailView.as_view(),
        {'template':'coursebackend/lessontest/pages/view/lessonstep.html'}, name='step'),

    url(r'^aufgaben$', HomeworkListView.as_view(),
        {'template':'coursebackend/lesson/pages/homeworks.html'}, name='homeworklist'),
)


urlpatterns += patterns('',

    url(r'^bearbeiten/block/(?P<pk>\d+)$', BlockUpdateView.as_view(),
        {'template':'coursebackend/lessontest/pages/update/lessonblockupdate.html'}, name='blockupdate'),

    url(r'^bearbeiten/lektion/(?P<pk>\d+)$', LessonUpdateView.as_view(),
        {'template':'coursebackend/lessontest/pages/update/lessonupdate.html'}, name='lessonupdate'),

    url(r'^bearbeiten/abschnitt/(?P<pk>\d+)$', LessonStepUpdateView.as_view(),
        {'template':'coursebackend/lessontest/pages/update/lessonstepupdate.html'}, name='stepupdate'),
)

urlpatterns += patterns('',
    url(r'^(?P<pk>\d+)/loeschen$', LessonDeleteView.as_view(),
        {'template':'coursebackend/lessontest/pages/update/delete.html'}, name='delete'),
)

urlpatterns += patterns('',

    url(r'^anlegen/block$', BlockCreateView.as_view(),
        {'template':'coursebackend/lessontest/pages/update/lessonblockcreate.html'}, name='blockcreate'),

    url(r'^anlegen/lektion$', LessonCreateView.as_view(),
        {'template':'coursebackend/lessontest/pages/update/lessoncreate.html'}, name='lessoncreate'),

    url(r'^anlegen/abschnitt$', LessonStepCreateView.as_view(),
        {'template':'coursebackend/lessontest/pages/update/lessonstepcreate.html'}, name='stepcreate'),

    url(r'^kopieren/lektion/(?P<pk>\d+)$', LessonCopyView.as_view(),
        {'template':'coursebackend/lessontest/pages/update/lessoncopy.html'}, name='lessoncopy'),
)