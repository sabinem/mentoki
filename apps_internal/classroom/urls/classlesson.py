# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.classlesson import ClassLessonDetailView, ClassLessonStartView

from ..views.classlessonstep import ClassLessonStepDetailView, \
    StudentsWorkPublicListView, StudentsWorkPrivateListView, \
    StudentsWorkDetailView
from ..views.classlessonstepwork import StudentsWorkUpdatePublicView, \
    StudentsWorkCommentView, StudentsWorkAddTeamView, StudentsWorkCreateView, \
    StudentsWorkDeleteView, StudentsWorkUpdatePrivateView


urlpatterns = patterns('',
    url(r'^$', ClassLessonStartView.as_view(),
        {'template':'classroom/classlesson/pages/start.html'}, name='start'),

    url(r'^lektion/(?P<pk>\d+)$', ClassLessonDetailView.as_view(),
        {'template': 'classroom/classlesson/pages/lesson.html'}, name='lesson'),
)


urlpatterns += patterns('',
    url(r'^abschnitt/(?P<pk>\d+)$', ClassLessonStepDetailView.as_view(),
        {'template':'classroom/classlesson/pages/lessonstep.html'}, name='step'),

    url(r'^abschnitt/(?P<pk>\d+)/arbeit/(?P<work_pk>\d{1,4})$',
        StudentsWorkDetailView.as_view(),
        {'template':'classroom/classlesson/pages/studentswork.html'}, name='studentswork'),

    url(r'^abschnitt/(?P<pk>\d+)/abgegeben$',
        StudentsWorkPublicListView.as_view(),
        {'template':'classroom/classlesson/pages/studentsworks_published.html'}, name='publiclist'),

    url(r'^abschnitt/(?P<pk>\d+)/privat$',
        StudentsWorkPrivateListView.as_view(),
        {'template':'classroom/classlesson/pages/studentsworks_private.html'}, name='privatelist'),
)


urlpatterns += patterns('',
    url(r'^abschnitt/(?P<pk>\d+)/kommentieren/(?P<work_pk>\d{1,4})/kommentieren$',
        StudentsWorkCommentView.as_view(),
        {'template':'classroom/classlesson/pages/comment.html'}, name='comment'),

    url(r'^(?P<pk>\d{1,4})/(?P<work_pk>\d{1,4})/nachbearbeiten$', StudentsWorkUpdatePrivateView.as_view(),
        {'template':'classroom/classlesson/pages/update_private.html'}, name='updateprivate'),

    url(r'^(?P<pk>\d{1,4})/(?P<work_pk>\d{1,4})/bearbeiten$', StudentsWorkUpdatePublicView.as_view(),
        {'template':'classroom/classlesson/pages/update_public.html'}, name='updatepublic'),

    url(r'^(?P<pk>\d{1,4})/anlegen$', StudentsWorkCreateView.as_view(),
        {'template':'classroom/classlesson/pages/create.html'}, name='create'),

    url(r'^(?P<pk>\d{1,4})/(?P<work_pk>\d{1,4})/loeschen$', StudentsWorkDeleteView.as_view(),
        {'template':'classroom/classlesson/pages/delete.html'}, name='delete'),

    url(r'^(?P<pk>\d{1,4})/(?P<work_pk>\d{1,4})/team$', StudentsWorkAddTeamView.as_view(),
        {'template':'classroom/classlesson/pages/addteam.html'}, name='addteam'),
)
