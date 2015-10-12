# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views.info import CourseEventProductView, CourseEventListView,\
    CourseEventAGBView, CourseEventMentorsView

from .views.braintreeview import BraintreeView

from .views.paymentredirect import paymentmanger
from .views.paymentmethodbraintree import PaymentView, SuccessView


urlpatterns = patterns('',

    url(r'^$',
        CourseEventListView.as_view(), name='list'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/danke$', SuccessView.as_view(),
        name='payment_success'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/$',
        CourseEventProductView.as_view(), name='detail'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/agb$',
        CourseEventAGBView.as_view(), name='agb'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/kursleitung$',
        CourseEventMentorsView.as_view(), name='mentors'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<pk>\d+)/zahlungsmethode$',
        PaymentView.as_view(), name='paymentmethod'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<pk>\d+)/braintreemethode$',
        BraintreeView.as_view(), name='braintreemethod'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<pk>\d+)/zahlungsmanager$',
        paymentmanger, name='paymentmanager'),



    #url(r'^zahlungsproblem/$', PaymentFailedView.as_view(), name='payment_failed'),

)

