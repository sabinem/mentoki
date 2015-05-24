from django.conf.urls import patterns, url
from .feeds import LatestNewsletterFeed
from .views_public import NewslettersListView, NewsletterDetailView
from .views_admin import NewsletterCreateView, NewsletterUpdateView, NewsletterAdminListView

urlpatterns = patterns("",
    # urls for reading newsletters
    url(r'^newsletter/alle$', NewslettersListView.as_view(), name='list'),
    url(r'^newsletter/(?P<slug>\S+)/$',
        NewsletterDetailView.as_view(), name='single'),

    # feed urls
    url(r'^feed/$', LatestNewsletterFeed(), name='feed'),

    # urls for writing newsletters
    url(r'^verwalten$', NewsletterAdminListView.as_view(), name='adminlist'),
    url(r'^anlegen$', NewsletterCreateView.as_view(), name='create'),
    url(r'^bearbeiten/(?P<pk>\d+)/$', NewsletterUpdateView.as_view(), name='update'),
)