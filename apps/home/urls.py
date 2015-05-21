from django.conf.urls import patterns, url

from .views import HomePageView, TeachPageView, TeamPageView, ImpressumPageView, \
    NewsLetterView, WebinarView

urlpatterns = patterns("",
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^team$', TeamPageView.as_view(), name='team'),
    url(r'^impressum$', ImpressumPageView.as_view(), name='impressum'),
    url(r'^webinar-online-unterrichten$', WebinarView.as_view(), name='webinar'),
    url(r'^newsletters$', NewsLetterView.as_view(), name='newsletter'),
    url(r'^unterrichten$', TeachPageView.as_view(), name='teach'),
    url(r'^unterrichten/(?P<goto>\S+)$', TeachPageView.as_view(), name='teach'),
)