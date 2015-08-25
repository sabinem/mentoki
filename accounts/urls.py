from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.views import password_reset

urlpatterns = patterns('',

    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'login.html'},
        name='login'),

    url(r'^logout/$',
        'django.contrib.auth.views.logout_then_login',
        name='logout'),

    url(r'^password_reset/$',
        'django.contrib.auth.views.password_reset',
        {'template_name': 'password_reset_form.html'},
        name='password_reset'),

    url(r'^password_reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'password_reset_done.html'},
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name':'password_reset_confirm.html'},
        name='password_reset_confirm'),

    url(r'^reset/done/$',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name':'password_reset_complete.html'},
        name='password_reset_complete'),

    )

