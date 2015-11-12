# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views.payment_result import PaymentSuccessView, PaymentFailureView
from .views.payment import PaymentView
from .views.redirect import CheckoutStartView

urlpatterns = patterns('',

    url(r'^$',
        CheckoutStartView.as_view(), name='redirect'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/redirect$',
        CheckoutStartView.as_view(), name='redirect_to_product'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/zahlen$',
        PaymentView.as_view(), name='payment'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<order_pk>\d{1,4})/danke$',
        PaymentSuccessView.as_view(),
        name='payment_success'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<order_pk>\d{1,4})/fehler$',
        PaymentFailureView.as_view(),
        name='payment_failure'),
)

