# -*- coding: utf-8 -*-

"""
Mentoki general pages urls: all this urls are public and will be targeted
by the search engines. Therefore they need to be stable

Urls in google so far:
/:
   Homepage
/team:
   Teampage

Neue Urls (noch ohne Aufwand veränderbar)
/was-uns-antreibt
   Motivation
"""

from django.conf.urls import patterns, url

from .views import HomePageView, AboutPageView, MotivationPageView, \
    MentorsPageView, StandardPageView, CourseAGBPageView

urlpatterns = patterns("",

    # alter url: muss so bleiben, wegen google
    url(r'^team$',
        AboutPageView.as_view(),
        name='about'),

    # alter url: muss so bleiben, wegen google
    url(r'^$',
        HomePageView.as_view(),
        name='home'),

    # neuer url: kann auch anderers heissen
    url(r'^motivation$',
        MotivationPageView.as_view(),
        name='motivation'),

    # neuer url: kann auch anderers heissen
    url(r'^standards$',
        StandardPageView.as_view(),
        {'pagecode': 'standards'},
        name='standards'),

    # neuer url: kann auch anderers heissen
    url(r'^motivation$',
        CourseAGBPageView.as_view(),
        name='course_agb'),

    # neuer url: kann auch anderers heissen
    url(r'^mentor/(?P<username>[a-z0-9_-]+)/$',
        MentorsPageView.as_view(),
        name='mentor'),
)