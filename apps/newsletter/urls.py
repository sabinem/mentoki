from django.conf.urls import patterns, url

from .views import NewslettersListView, NewsletterDetailView, NewsletterCreateView, NewsletterUpdateView

urlpatterns = patterns("",
    url(r'^alle$', NewslettersListView.as_view(), name='list'),
    url(r'^einzeln/(?P<id>\d{1,4})/$',
        NewsletterDetailView.as_view(), name='single'),
    url(r'^schreiben$', NewsletterCreateView.as_view(), name='create'),
    url(r'^bearbeiten/(?P<pk>\d{1,4})/$', NewsletterUpdateView.as_view(), name='update'),
)