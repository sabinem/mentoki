# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.lesson.copy import LessonCopyView
from ..views.lesson.lesson import LessonUpdateView, LessonCreateView
from ..views.lesson.lessonblock import BlockUpdateView, BlockCreateView
from ..views.lesson.lessonstep import LessonStepUpdateView, LessonStepCreateView
from ..views.lesson.list import BlockListView, BlockLessonsView, BlocksCompleteView
from ..views.lesson.detail import BlockDetailView, LessonDetailView, \
    StepDetailView, BlockCompleteView
from ..views.lesson.delete import LessonDeleteView

urlpatterns = patterns('',
    url(r'^$', BlockListView.as_view(),
        {'template': 'coursebackend/lesson/pages/view/blocklist.html'},
        name='blocklist'),

    url(r'^mit-lektionen$', BlockLessonsView.as_view(),
        {'template': 'coursebackend/lesson/pages/view/blockswithlessons.html'},
        name='start'),

    url(r'^komplett$', BlocksCompleteView.as_view(),
        {'template': 'coursebackend/lesson/pages/view/blockscomplete.html'},
        name='complete'),

    url(r'^block/(?P<pk>\d+)$', BlockDetailView.as_view(),
        {'template': 'coursebackend/lesson/pages/view/lessonblock.html'}, name='block'),

    url(r'^block/(?P<pk>\d+)/komplett$', BlockCompleteView.as_view(),
        {'template': 'coursebackend/lesson/pages/view/blockcomplete.html'},
        name='blockcomplete'),

    url(r'^lektion/(?P<pk>\d+)$', LessonDetailView.as_view(),
        {'template': 'coursebackend/lesson/pages/view/lesson.html'}, name='lesson'),

    url(r'^abschnitt/(?P<pk>\d+)$', StepDetailView.as_view(),
        {'template': 'coursebackend/lesson/pages/view/lessonstep.html'}, name='step'),

)


urlpatterns += patterns('',

    url(r'^bearbeiten/block/(?P<pk>\d+)$', BlockUpdateView.as_view(),
        {'template': 'coursebackend/lesson/pages/update/lessonblockupdate.html'}, name='blockupdate'),

    url(r'^bearbeiten/lektion/(?P<pk>\d+)$', LessonUpdateView.as_view(),
        {'template': 'coursebackend/lesson/pages/update/lessonupdate.html'}, name='lessonupdate'),

    url(r'^bearbeiten/abschnitt/(?P<pk>\d+)$', LessonStepUpdateView.as_view(),
        {'template': 'coursebackend/lesson/pages/update/lessonstepupdate.html'}, name='stepupdate'),
)

urlpatterns += patterns('',
    url(r'^(?P<pk>\d+)/loeschen$', LessonDeleteView.as_view(),
        {'template': 'coursebackend/lesson/pages/update/delete.html'}, name='delete'),
)

urlpatterns += patterns('',

    url(r'^anlegen/block$', BlockCreateView.as_view(),
        {'template': 'coursebackend/lesson/pages/update/lessonblockcreate.html'}, name='blockcreate'),

    url(r'^anlegen/lektion$', LessonCreateView.as_view(),
        {'template': 'coursebackend/lesson/pages/update/lessoncreate.html'}, name='lessoncreate'),

    url(r'^anlegen/abschnitt$', LessonStepCreateView.as_view(),
        {'template': 'coursebackend/lesson/pages/update/lessonstepcreate.html'}, name='stepcreate'),

    url(r'^kopieren/lektion/(?P<pk>\d+)$', LessonCopyView.as_view(),
        {'template': 'coursebackend/lesson/pages/update/lessoncopy.html'}, name='lessoncopy'),
)