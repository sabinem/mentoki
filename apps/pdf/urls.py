# In some urls.py...
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django_downloadview import ObjectDownloadView
from .models import Document  # The model we created upward.
from .views import ImageIndexView
from .views import ImageView, ImageDetailView
from django.contrib import admin
from .views import upload_photos, recent_photos
admin.autodiscover()

download_document = ObjectDownloadView.as_view(model=Document)

urlpatterns = patterns('',
    url(r'^download/(?P<slug>[a-zA-Z0-9_-]+)/$', download_document, name="download"),
    url(r'^$', ImageIndexView.as_view(), name='image_index'),

    url(r"^ajax/photos/upload/$", upload_photos, name="upload_photos"),
    url(r"^ajax/photos/recent/$", recent_photos, name="recent_photos"),


    url(r'^upload/', ImageView.as_view(), name='image_upload'),
    url(
        r'^uploaded/(?P<pk>\d+)/$', ImageDetailView.as_view(),
        name='uploaded_image'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
