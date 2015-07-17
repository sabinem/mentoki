# import from django
from django.conf.urls import patterns, url
# import from other apps
from .views import *


urlpatterns = patterns('',
    url(r'^start$', DeskStartView.as_view(), name='start' ),
    url(r'^test$', DeskTestView.as_view(), name='test' ),
)

