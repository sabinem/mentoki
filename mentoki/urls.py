# -*- coding: utf-8 -*-

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView
from django.conf import settings
from django.views.defaults import *
from django.conf.urls import url, include


from django_downloadview import ObjectDownloadView

from apps_data.material.models.material import Material

# for the download of files
download = ObjectDownloadView.as_view(model=Material, file_field='file')

from apps_public.newsletter.feeds import LatestNewsletterFeed


# The Admin Site
urlpatterns = i18n_patterns('',

    # admin urls
    url(r'^admin/',
        include(admin.site.urls)),

    (r'^mail-queue/', include('mailqueue.urls')),
)


# Public urls
urlpatterns += i18n_patterns('',

    # homepage
    url(r'^',
        include('apps_public.home.urls', namespace='home')),

    # courseevent offers
    url(r'^kurse/',
        include('apps_public.courseoffer.urls', namespace='courseoffer')),

    # contact
    url(r'^kontakt/',
        include('apps_public.contact.urls', namespace='contact')),

    # file newsletter ...
    url(r'^newsletter/',
        include('apps_public.newsletter.urls', namespace='newsletter')),

    # feed
    url(r'^feed/$',
        LatestNewsletterFeed(),
        name='feed'),
)


# User Account urls
urlpatterns += i18n_patterns('',

    # desk: startpoint for all activities
    url(r'^schreibtisch/',
        include('apps_internal.desk.urls', namespace='desk')),

    # user handling urls
    #url(r'^benutzer/',
    #    include('accounts.urls')),

    url(r'^accounts/', include('allauth.urls')),

)

# Data urls
urlpatterns += i18n_patterns('',

    # lesson data urls
    url(r'^unterricht/',
        include('apps_data.lesson.urls', namespace='lesson')),

    url(r'^kurse/',
        include('apps_data.courseevent.urls', namespace='courseevent')),
)


# Classroom urls
urlpatterns += i18n_patterns('',

    # classroom
    url(r'^(?P<slug>[a-z0-9_-]+)/klassenzimmer/',
        include('apps_internal.classroom.urls', namespace='classroom')),
)


# teachers dashboard
urlpatterns += i18n_patterns('',

    # coursebackend
    url(r'^(?P<course_slug>[a-z0-9_-]+)/kursvorbereitung/',
        include('apps_internal.coursebackend.urls', namespace='coursebackend')),
)


# utilities
urlpatterns += i18n_patterns('',

    url(r'^download/(?P<slug>[a-zA-Z0-9_-]+)/$',
        download, name="download"),

    # file markdown ...
    url(r'^markdown/',
        include('django_markdown.urls')),

    # froala editor
    url(r'^froala_editor/',
        include('froala_editor.urls')),

    # robots
    (r'^robots\.txt/$',
        TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
)


if settings.DEBUG:
    print "============= settings.STATIC_URL %s" % settings.STATIC_URL
    print "============= settings.MEDIA_URL %s" % settings.MEDIA_URL
    print "============= settings.BASE_DIR %s" % settings.BASE_DIR
    #print "============= settings.BASE_DIR_PROJ %s" % settings.BASE_DIR_PROJECT
    print "============= settings.STATIC_ROOT %s" % settings.STATIC_ROOT
    print "============= settings.MEDIA_ROOT %s" % settings.MEDIA_ROOT
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)