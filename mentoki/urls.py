#import from django
from django.conf.urls import patterns, include, url
from django.views.defaults import *
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from apps.newsletter.feeds import LatestNewsletterFeed



urlpatterns = patterns('',
    # admin urls
    url(r'^admin/', include(admin.site.urls)),

    # homepage and front
    url(r'^', include('apps.home.urls', namespace='home')),

    # courseevents
    url(r'^kurse/', include('apps.courseevent.urls', namespace='courseevent')),

    # desk
    url(r'^schreibtisch/', include('apps.desk.urls', namespace='desk')),

    # coursebackend
    url(r'^(?P<course_slug>[a-z0-9_-]+)/kursvorbereitung/', include('apps.coursebackend.urls', namespace='coursebackend')),
    url(r'^pdf/', include('apps.coursebackend.urls', namespace='coursebackend')),

    # forum and classroom
    url(r'^forum/', include('apps.forum.urls', namespace='forum')),
    url(r'^klassenzimmer/', include('apps.classroom.urls', namespace='classroom')),

    # contact
    url(r'^kontakt/', include('apps.contact.urls', namespace='contact')),

    # file upload ...
    url(r'^upload/', include('apps.upload.urls', namespace='upload')),

    # file markdown ...
    url(r'^markdown/', include('django_markdown.urls')),

    # file newsletter ...
    url(r'^newsletter/', include('apps.newsletter.urls', namespace='newsletter')),

    url(r'^feed/$', LatestNewsletterFeed(), name='feed'),

    # quiz
    #url(r'^q/', include('quiz.urls')),

    # user handling urls
    url(r'^accounts/', include('userauth.urls')),

    (r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^500/$', TemplateView.as_view(template_name="500.html")),
        (r'^404/$', TemplateView.as_view(template_name="404.html")),
    )

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))


