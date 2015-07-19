# -*- coding: utf-8 -*-

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView
from django.conf import settings
from django.views.defaults import *
from django.conf.urls import url, include
from rest_framework import routers
from api import views

from rest_framework_extensions.routers import (
    ExtendedDefaultRouter as DefaultRouter
)
router = DefaultRouter()


router.register(r'accounts', views.AccountViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'materials', views.MaterialViewSet)
router.register(r'lessons', views.LessonViewSet)


course_routes = router.register(
    r'courses',
    views.CourseViewSet,
    base_name='course'
)
course_routes.register(
    r'materials',
    views.MaterialViewSet,
    base_name='course-material',
    parents_query_lookups=['course']
)


#router.register(r'lessons', views.LessonViewSet)
#router.register(r'courseevents', views.CourseEventsViewSet)
router.register(r'materials', views.MaterialViewSet)
#router.register(r'announcements', views.AnnouncementViewSet)
#router.register(r'forums', views.ForumViewSet)
#router.register(r'owner', views.OwnerViewSet)
#router.register(r'participation', views.ParticipationViewSet)


from apps_public.newsletter.feeds import LatestNewsletterFeed

urlpatterns = i18n_patterns('',

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # admin urls
    url(r'^admin/', include(admin.site.urls)),

    # course urls
    url(r'^api/', include('api.urls')),

    # homepage and front
    url(r'^', include('apps_public.home.urls', namespace='home')),

    # courses on offer
    url(r'^kurse/', include('apps_public.courseoffer.urls', namespace='courseoffer')),

    # desk
    url(r'^schreibtisch/', include('apps_internal.desk.urls', namespace='desk')),

    # coursebackend
    url(r'^(?P<course_slug>[a-z0-9_-]+)/kursvorbereitung/', include('apps_internal.coursebackend.urls', namespace='coursebackend')),
    url(r'^pdf/', include('apps_internal.coursebackend.urls', namespace='coursebackend')),

    # classroom
    #url(r'^(?P<course_slug>[a-z0-9_-]+)/(?P<courseevent_slug>[a-z0-9_-]+)klassenzimmer/', include('apps_internal.classroom.urls', namespace='classroom')),

    # contact
    url(r'^kontakt/', include('apps_public.contact.urls', namespace='contact')),

    # file upload ...
    url(r'^upload/', include('apps_core.upload.urls', namespace='upload')),

    # file markdown ...
    url(r'^markdown/', include('django_markdown.urls')),

    # file newsletter ...
    url(r'^newsletter/', include('apps_public.newsletter.urls', namespace='newsletter')),

    # feed
    url(r'^feed/$', LatestNewsletterFeed(), name='feed'),

    # user handling urls
    url(r'^accounts/', include('authentication.urls')),

    # robots
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


