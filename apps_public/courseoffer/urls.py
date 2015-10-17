# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views.info import CourseEventProductView, CourseEventListView,\
    CourseEventOfferView, CourseEventMentorsView

from.views.braintree import PaymentView, SuccessView

from .views.paymentprocessing import PaymentEmailView


urlpatterns = patterns('',

    url(r'^$',
        CourseEventListView.as_view(), name='list'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<pk>[a-z0-9]{3,50})/danke$', SuccessView.as_view(),
        name='payment_success'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/$',
        CourseEventProductView.as_view(), name='detail'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/angebot$',
        CourseEventOfferView.as_view(), name='offer'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/kursleitung$',
        CourseEventMentorsView.as_view(), name='mentors'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<pk>\d+)/zahlen$',
        PaymentView.as_view(), name='braintree'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<pk>\d+)/xzahlen$',
        PaymentEmailView.as_view(), name='pay_per_mail'),

    #url(r'^zahlungsproblem/$', PaymentFailedView.as_view(), name='payment_failed'),

)

