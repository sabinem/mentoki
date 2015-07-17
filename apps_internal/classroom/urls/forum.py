
from django.conf.urls import patterns, url
from django_downloadview import ObjectDownloadView


# import from django
from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()
# import from own app
#from .forum import SubForumCreateView


# for the download of files
#download = ObjectDownloadView.as_view(model=CourseMaterialUnit, file_field='file')


urlpatterns = patterns('',
#    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/forum/anlegen$',
#        SubForumCreateView.as_view(), name='createsubforum'),
#    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/forum/(?P<subforum>\d{1,4})/bearbeiten$',
#        SubForumUpdateView.as_view(), name='updatesubforum'),
)
