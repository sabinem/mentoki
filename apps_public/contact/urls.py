# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

from .views import  ContactView, AnswerView
from django.shortcuts import redirect

def contact_redirect(request):
    print 'in redirect'
    return HttpResponsePermanentRedirect(reverse('contact:contact'))

urlpatterns = patterns("",

    url(r'^kontakt$', contact_redirect,
        ),

    url(r'^$', ContactView.as_view(),
        {'template':'contact/pages/contact.html'}, name='contact'),

    url(r'^danke$', AnswerView.as_view(),
         {'template':'contact/pages/answer.html'}, name='answer'),

)

