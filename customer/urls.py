# coding: utf-8

from django.conf.urls import url
from .views import PaymentView, SuccessView


urlpatterns = [

    url(r'^$', PaymentView.as_view()),

    url(r'^thankyou/$', SuccessView.as_view(), name='payment_success'),
]