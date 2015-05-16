from django.conf.urls import patterns, url
from django.contrib import admin
from .views_contact import  ContactView, AnswerView, ApplicationView, WebinarView, NewsletterView, \
    PrebookView


urlpatterns = patterns("",
    url(r'^starterkursbewerbung$', ApplicationView.as_view(), name='application'),
    url(r'^voranmeldung$', PrebookView.as_view(), name='prebook'),
    url(r'^kontakt$', ContactView.as_view(), name='contact'),
    url(r'^webinaranmeldung$', PrebookView.as_view(), name='webinar'),
    url(r'^newsletteranmeldung$', ContactView.as_view(), name='newsletter'),
    url(r'^danke$', AnswerView.as_view(), name='answer'),
)