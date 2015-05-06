from django.conf.urls import patterns, url

from .views import HomePageView, StarterkursPageView, TeamPageView, ImpressumPageView, NewsPageView

urlpatterns = patterns("",
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^starterkurs/(?P<tab>[a-z0-9_-]{3,50})$', StarterkursPageView.as_view(), name='starterkurs'),
    url(r'^team$', TeamPageView.as_view(), name='team'),
    url(r'^impressum$', ImpressumPageView.as_view(), name='impressum'),
    url(r'^webinar-online-unterrichten$', NewsPageView.as_view(), name='news'),
)