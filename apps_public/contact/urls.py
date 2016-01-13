# -*- coding: utf-8 -*-

"""
Urls for the Contact Form and for the Answer Page
"""

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import  ContactView, AnswerView


urlpatterns = patterns("",
    url(r'^$', ContactView.as_view(),
        {'template':'contact/pages/contact.html'}, name='contact'),

    url(r'^danke$', AnswerView.as_view(),
         {'template':'contact/pages/answer.html'}, name='answer'),

)

