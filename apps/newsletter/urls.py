from django.conf.urls import patterns, url
from .views_read import NewslettersListView, NewsletterDetailView
from .views_update import NewsletterCreateView, NewsletterUpdateView

urlpatterns = patterns("",
    # urls for reading newsletters
    url(r'^alle$', NewslettersListView.as_view(), name='list'),
    url(r'^einzeln/(?P<id>\d{1,4})/$',
        NewsletterDetailView.as_view(), name='single'),

    # urls for writing newsletters
    url(r'^schreiben$', NewsletterCreateView.as_view(), name='create'),
    url(r'^bearbeiten/(?P<pk>\d{1,4})/$', NewsletterUpdateView.as_view(), name='update'),
)