from django.conf.urls import patterns, include, url
from .views import login_view, logout_view
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.views import password_reset

urlpatterns = patterns('',
    url(r'^logout/$', logout_view , name='logout'),
    url(r'^login/$', login_view, name='login'),
    #url (r'^password/reset/$', password_reset, {'template_name': 'my_templates/password_reset.html'}),
    url (r'^password/reset/$', password_reset, name='reset'),
    url (r'^password/reset/done$', 'django.contrib.auth.views.password_change_done', name='password_reset_done'),
    )

