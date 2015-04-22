from django.conf.urls import patterns, url
from django.contrib import admin
from .views_contact import  ContactView, AnswerView, ApplicationView, \
    PrebookView, AnswerApplicationView, AnswerPrebookView


urlpatterns = patterns("",
    url(r'^starterkursbewerbung$', ApplicationView.as_view(), name='application'),
    url(r'^voranmeldung$', PrebookView.as_view(), name='prebook'),
    url(r'^kontakt$', ContactView.as_view(), name='contact'),
    url(r'^kontakt/danke$', AnswerView.as_view(), name='answer'),
    url(r'^voranmeldung/(?P<slug>[a-z0-9_-]{3,50})/danke$',
        AnswerPrebookView.as_view(), name='answerprebook'),
    url(r'^starterkursbewerbung/danke$',
        AnswerApplicationView.as_view(), name='answerapplication'),
)