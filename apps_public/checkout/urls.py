# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views.payment_success import SuccessView
from .views.braintree_payment import PaymentView
from .views.checkorder import CheckOrderView

urlpatterns = patterns('',

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/checkorder$',
        CheckOrderView.as_view(), name='checkorder'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<temporder_pk>\d{1,4})/zahlen$',
        PaymentView.as_view(), name='payment'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<pk>[a-z0-9]{3,50})/danke$', SuccessView.as_view(),
        name='payment_success'),
)

