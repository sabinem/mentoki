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
    MentorsPageView, StandardPageView, CourseAGBPageView, MentorsListView, \
    ImpressumPageView, StarterkursPageView, TeachOnlinePageView,  \
    CourseReadyPageView, EducationMentoringPageView

urlpatterns = patterns("",

    # alter url: muss so bleiben, wegen google
    url(r'^team$',
        AboutPageView.as_view(),
        name='about'),

    # neuer url: kann auch anderers heissen
    url(r'^online-mentor-werden/$',
        StarterkursPageView.as_view(),
        {'pagecode': 'starterkurs'},
        name='starterkurs'),

    # neuer url: kann auch anderers heissen
    url(r'^bildungsmentoring/$',
        EducationMentoringPageView.as_view(),
        {'pagecode': 'bildungsmentoring'},
        name='educationmentor'),


    # neuer url: kann auch anderers heissen
    url(r'^online-unterrichten/$',
        TeachOnlinePageView.as_view(),
        {'pagecode': 'unterrichten'},
        name='teachonline'),

    # neuer url: kann auch anderers heissen
    url(r'^online-kurs-anbieten/$',
        CourseReadyPageView.as_view(),
        {'pagecode': 'kursfertig'},
        name='teachready'),

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
    url(r'^mentoki-allgemeine-geschaeftsbedingungen$',
        CourseAGBPageView.as_view(),
        {'pagecode': 'agb'},
        name='agb'),

    # neuer url: kann auch anderers heissen
    url(r'^impressum$',
        ImpressumPageView.as_view(),
        {'pagecode': 'impressum'},
        name='impressum'),

    # neuer url: kann auch anderers heissen
    url(r'^mentor/(?P<username>[a-z0-9_-]+)/$',
        MentorsPageView.as_view(),
        name='mentor'),

    # neuer url: kann auch anderers heissen
    url(r'^mentoren-team/$',
        MentorsListView.as_view(),
        name='mentorslist'),

)