from django.conf.urls import patterns, url

from .views import HomePageView, TeachPageView, TeamPageView, ImpressumPageView, \
    NewsLetterView, WebinarView, NewHomePageView

urlpatterns = patterns("",
    url(r'^$', NewHomePageView.as_view(), name='home'),
    url(r'^team$', TeamPageView.as_view(), name='team'),
    url(r'^impressum$', ImpressumPageView.as_view(), name='impressum'),
    url(r'^newsletters$', NewsLetterView.as_view(), name='newsletter'),
    url(r'^unterrichten$', TeachPageView.as_view(), name='teach'),
    url(r'^unterrichten/(?P<goto>\S+)$', TeachPageView.as_view(), name='teach'),

    #old urls still maintained
    url(r'^webinar-online-unterrichten$', WebinarView.as_view(), name='webinar'),
)