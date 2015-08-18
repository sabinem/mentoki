from django.conf.urls import patterns, url
from .feeds import LatestNewsletterFeed
from .views_public import NewsletterPublicListView, NewsletterDetailView
from .views_admin import NewsletterCreateView, NewsletterUpdateView, \
    NewsletterAdminListView, NewsletterDeleteView

urlpatterns = patterns("",
    # urls for reading newsletters
    url(r'^$', NewsletterPublicListView.as_view(), name='index'),
    # urls for writing newsletters
    url(r'^verwalten$', NewsletterAdminListView.as_view(), name='admin'),
    url(r'^anlegen$', NewsletterCreateView.as_view(), name='create'),
    url(r'^bearbeiten/(?P<slug>\S+)/$', NewsletterUpdateView.as_view(), name='update'),
    url(r'^loeschen/(?P<slug>\S+)/$', NewsletterDeleteView.as_view(), name='delete'),

    url(r'^(?P<slug>\S+)/$',
        NewsletterDetailView.as_view(), name='detail'),
)