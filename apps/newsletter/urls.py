from django.conf.urls import patterns, url
from .feeds import LatestNewsletterFeed
from .views_public import NewslettersListView, NewsletterDetailView
from .views_admin import NewsletterCreateView, NewsletterUpdateView

urlpatterns = patterns("",
    # urls for reading newsletters
    url(r'^newsletter/alle$', NewslettersListView.as_view(), name='list'),
    url(r'^newsletter/(?P<slug>\S+)/$',
        NewsletterDetailView.as_view(), name='single'),

    # feed urls
    url(r'^feed/$', LatestNewsletterFeed(), name='feed'),

    # urls for writing newsletters
    url(r'^schreiben$', NewsletterCreateView.as_view(), name='create'),
    url(r'^bearbeiten/(?P<pk>\d{1,4})/$', NewsletterUpdateView.as_view(), name='update'),
)