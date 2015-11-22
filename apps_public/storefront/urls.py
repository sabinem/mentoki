# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views.info import \
    CourseGroupDetailView, CourseGroupMentorsView
from .views.list import CourseProductGroupsListView, \
    ListNowView, ListPreviewView
from .views.sales import CourseGroupOfferView
from .views.prebook import ProductPrebookView, AnswerView


urlpatterns = patterns('',

    url(r'^$',
        CourseProductGroupsListView.as_view(), name='list'),

    url(r'^jetzt-buchbar$',
        ListNowView.as_view(), name='list_now'),

    url(r'^vorschau$',
        ListPreviewView.as_view(), name='list_preview'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/$',
        CourseGroupDetailView.as_view(), name='detail'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/angebot$',
        CourseGroupOfferView.as_view(), name='offer'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/kursleitung$',
        CourseGroupMentorsView.as_view(), name='mentors'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/warteliste$',
        ProductPrebookView.as_view(), name='prebook'),

    url(r'^(?P<pk>\d{1,4})/danke$',
        AnswerView.as_view(), name='prebooking_sucess'),

)

