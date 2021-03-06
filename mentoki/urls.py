# -*- coding: utf-8 -*-

"""
urls for mentoki
"""

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView
from django.conf import settings
from django.views.defaults import *
from django.conf.urls import url, include
from django.contrib.sitemaps import views
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse


from django_downloadview import ObjectDownloadView

from apps_data.material.models.material import Material

from .views import PublicViewSitemap, CoursesViewSitemap, \
    MentorsViewSitemap, StaticViewSitemap, CourseListViewSitemap

# for the download of files
download = ObjectDownloadView.as_view(model=Material, file_field='file')

from apps_public.newsletter.feeds import LatestNewsletterFeed

sitemaps = {
    'mentoki': PublicViewSitemap(),
    'homepage': StaticViewSitemap(),
    'kurse': CoursesViewSitemap(),
    'mentoren': MentorsViewSitemap(),
    'kurslisten': CourseListViewSitemap
}


# The Admin Site
urlpatterns = i18n_patterns('',

    # admin urls
    url(r'^admin/',
        include(admin.site.urls)),

    (r'^mail-queue/', include('mailqueue.urls')),
)


# seo
urlpatterns += i18n_patterns('',

    # robots
    (r'^robots\.txt/$',
        TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    (r'^googleb739bc2feb0d0b27\.html/$',
        TemplateView.as_view(template_name='googleb739bc2feb0d0b27.html')),

    (r'^kurse/googleb739bc2feb0d0b27\.html/$',
        TemplateView.as_view(template_name='googleb739bc2feb0d0b27.html')),

    #sitemaps
    url(r'^sitemap\.xml$', views.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap, {'sitemaps': sitemaps}),
)


# Public urls
urlpatterns += i18n_patterns('',

    # courseevent offers
    url(r'^checkout/',
        include('apps_public.checkout.urls', namespace='checkout')),

    # courseevent offers
    url(r'^kurse/',
        include('apps_public.storefront.urls', namespace='storefront')),

    # contact
    url(r'^kontakt/',
        include('apps_public.contact.urls', namespace='contact')),

    url(r'^kontakt',
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

    url(r'^accounts/', include('allauth.urls')),

)

# Data urls
urlpatterns += i18n_patterns('',

    # lesson data urls
    url(r'^unterricht/',
        include('apps_data.lesson.urls', namespace='lesson')),

    url(r'^kurseintern/',
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

)

# utilities
urlpatterns += i18n_patterns('',
    # homepage
    url(r'^',
        include('apps_public.home.urls', namespace='home')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)

# urls or settings
handler500 = 'mentoki.views.server_error'
handler503 = 'mentoki.views.maintenance_mode'

