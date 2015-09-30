from django.conf.urls import patterns, url

from .views import HomePageView, AboutPageView, MotivationPageView

urlpatterns = patterns("",

    # alter url: muss so bleiben, wegen google
    url(r'^team$',
        AboutPageView.as_view(),
        name='about'),

    # alter url: muss so bleiben, wegen google
    url(r'^$',
        HomePageView.as_view(),
        name='home'),

    # neuer url: kann auch anderers heissen
    url(r'^motivation$',
        MotivationPageView.as_view(),
        name='motivation'),

    # neuer url: kann auch anderers heissen
    url(r'^mentor/(?P<username>[a-z0-9_-]+)/$',
        MotivationPageView.as_view(),
        name='mentor'),
)