# import from django
from django.conf.urls import patterns, url
# import from this app
from .views_public import CourseEventListView, CourseEventDetailView
# from .views_internal import CourseEventInternalListView, CourseEventInternalDetailView, bookcourse


urlpatterns = patterns('',
    # public visible courseevent informations
    url(r'^$', CourseEventListView.as_view(), name='publiclist'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/$', CourseEventDetailView.as_view(), name='publicdetail'),

    # internal visible courseevent informations
    #url(r'^intern$', CourseEventInternalListView.as_view(), name='internallist'),
    #url(r'^intern/(?P<slug>[a-z0-9_-]{3,50})/listeneintrag$', CourseEventInternalListView.as_view(),
    #    name='internallist'),
    #url(r'^intern/(?P<slug>[a-z0-9_-]{3,50})/detail$', CourseEventInternalDetailView.as_view(),
    #    name='internaldetail'),
    # booking of an internal event
    #url(r'^buchen/(?P<slug>[a-z0-9_-]{3,50})/$', bookcourse, name='bookcourse'),
)

