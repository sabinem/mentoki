# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views.braintree_singlestep import PaymentView
from .views.payment_success import SuccessView
from .views.braintree_anonymous import AnonymousPaymentView
from .views.payment_redirect import PaymentStartView
from .views.construction import ConstructionView
#from .views.test import TestWizard


urlpatterns = patterns('',

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<pk>[a-z0-9]{3,50})/danke$', SuccessView.as_view(),
        name='payment_success'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/buchen$',
        PaymentView.as_view(), name='braintree_authenticated'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/zahlen$',
        AnonymousPaymentView.as_view(), name='braintree_anomymous'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/zahlstart$',
        PaymentStartView.as_view(), name='start'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/baustelle$',
        ConstructionView.as_view(), name='construction'),

    #url(r'^test$',
    #    TestWizard.as_view(), name='test'),

)

