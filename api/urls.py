from django.conf.urls import url
from .views import *
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^coursesperteacher/$', CoursesPerTeacherList.as_view()),
    #url(r'^course/(?P<pk>[0-9]+)/$', CourseDetail.as_view(), name='course-detail'),
    url(r'^course/(?P<course_pk>[0-9]+)/lessons/all/$', LessonsAllList.as_view()),
    url(r'^lesson/(?P<pk>[0-9]+)/$', LessonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
