# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


from .views.info import \
    CourseGroupDetailView
from .views.list import CourseProductGroupsListView, \
    ListNowView, ListPreviewView, ListSingleView
from .views.prebook import ProductPrebookView, AnswerView

urlpatterns = patterns('',
    url(r'^$',
        CourseProductGroupsListView.as_view(), name='list'),

    url(r'^jetzt-buchbar$',
        ListNowView.as_view(), name='list_now'),

    url(r'^vorschau$',
        ListPreviewView.as_view(), name='list_preview'),

    url(r'^(?P<pk>\d{1,4})/admin$',
        ListSingleView.as_view(), name='admin'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/$',
        CourseGroupDetailView.as_view(), name='detail'),

)

