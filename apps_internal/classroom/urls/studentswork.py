# -*- coding: utf-8 -*-

"""
Urls für das Forum
- list: Liste aller Ankündigungen
- detail: Detailansicht einer Ankündigung
"""

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.studentswork import StudentsWorkListPublicView, StudentsWorkListPrivateView, \
    StudentsWorkCreateView


urlpatterns = patterns('',

    url(r'^$', StudentsWorkListPublicView.as_view(),
        {'template':'classroom/studentswork/pages/listpublic.html'}, name='list'),

    url(r'^entwuerfe$', StudentsWorkListPrivateView.as_view(),
        {'template':'classroom/studentswork/pages/listprivate.html'}, name='listprivate'),

    url(r'^anlegen$', StudentsWorkCreateView.as_view(),
        {'template':'classroom/studentswork/pages/create.html'}, name='create'),
    )
