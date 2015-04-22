# import from django
from django.conf.urls import patterns, url
# import from other apps
from .views import DeskStartView


urlpatterns = patterns('',
    url(r'^start$', DeskStartView.as_view(), name='start' ),
)

