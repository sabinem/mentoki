from django.conf.urls import patterns, url
from .views_units import LessonDetailView, LessonMaterialView
from .views_announcements import AnnouncementsListView, AnnouncementDetailView
from .views_forum import ForumListView, SubForumListView, ForumRecentListView
from .views_thread import ThreadCreateView, ThreadListPostCreateView

urlpatterns = patterns('',
    #start
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/ankuendigungen$', AnnouncementsListView.as_view(), name='start'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/ankuendigungen/(?P<id>\d{1,4})/$',
        AnnouncementDetailView.as_view(), name='announcementdetail'),

    #display one lesson
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/lektion/(?P<unit>\d{1,4})$',
        LessonDetailView.as_view(), name='lesson'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/lektion/(?P<unit>\d{1,4})/material/(?P<material>\d{1,4})$',
        LessonMaterialView.as_view(),name='lessonmaterial'),
    #display the forum of the classroom
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/forum$', ForumListView.as_view(),
        name='forum'),

    #display the forum of the classroom
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/aktuell$', ForumRecentListView.as_view(),
        name='recent'),

    #display all subforums starting from a given subforum.
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/forum/(?P<subforum>\d{1,4})$',
        SubForumListView.as_view(),
        name='subforum'),

    #display thread with postcreationform
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/forum/(?P<subforum>\d{1,4})/thread/(?P<thread>\d{1,4})$',
        ThreadListPostCreateView.as_view(),
        name='thread'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/forum/(?P<subforum>\d{1,4})/createthread$', ThreadCreateView.as_view(),
        name='createthread'),

)
