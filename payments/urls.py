# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import  PaymentView


urlpatterns = patterns("",

    url(r'^$', PaymentView.as_view(),
        {'template':'payments/payments.html'}, name='pay'),

)