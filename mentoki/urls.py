#import from django
from django.conf.urls import patterns, include, url
from django.views.defaults import *
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings



urlpatterns = patterns('',
    # admin urls
    url(r'^admin/', include(admin.site.urls)),

    # homepage and front
    url(r'^', include('apps.home.urls', namespace='home')),

    # courseevents
    url(r'^kurse/', include('apps.courseevent.urls', namespace='courseevent')),

    # desk
    url(r'^schreibtisch/', include('apps.desk.urls', namespace='desk')),

    # course
    url(r'^kursvorlage/', include('apps.course.urls', namespace='course')),

    # forum and classroom
    url(r'^forum/', include('apps.forum.urls', namespace='forum')),
    url(r'^klassenzimmer/', include('apps.classroom.urls', namespace='classroom')),

    # contact
    url(r'^kontakt/', include('apps.contact.urls', namespace='contact')),

    # file upload ...
    url(r'^upload/', include('apps.upload.urls', namespace='upload')),

    # user handling urls
    url(r'^accounts/password/change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'userauth/password_change_form.html'},
        name='password_change'),
    url(r'^accounts/password/changed/$', 'django.contrib.auth.views.password_change_done',
        {'template_name': 'userauth/password_change_done.html'},
        name='password_change_done'),
    url(r'^accounts/', include('userauth.urls', namespace='userauth')),
    url(r'^user/password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    (r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/user/password/done/',
         'template_name': 'registration/password_reset_confirm.html'}),
    (r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'),
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


