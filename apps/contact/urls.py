from django.conf.urls import patterns, url
from .views_contact import  ContactView, AnswerView

urlpatterns = patterns("",
    url(r'^$', ContactView.as_view(), name='contact'),
    url(r'^danke$', AnswerView.as_view(), name='answer'),
)