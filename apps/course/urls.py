# import from django
from django.conf.urls import patterns, url
# import from 3rd party apps
from django_downloadview import ObjectDownloadView
# import from this app
from .models import CourseMaterialUnit
from .views_coursedescription import CourseDetailView, CourseUpdateTextView, \
    CourseUpdateProjectView, CourseUpdatePrerequisitesView, \
    CourseUpdateTargetgroupView, CourseUpdateExcerptView, CourseUpdateStructureView
from .views_owners import CourseOwnersListView, CourseOwnerUpdateView
from .views_coursedescription import CourseEventDetailView, CourseEventUpdateWorkloadView, \
    CourseEventUpdateTextView, CourseEventUpdateProjectView, CourseEventUpdateExcerptView, \
    CourseEventUpdateFormatView, CourseEventUpdateStructureView, \
    CourseEventUpdateTargetgroupView, CourseEventUpdatePrerequisitesView

from .views_participants import CourseParticipantsListView
from .views_lessonsview import LessonsView, BlockDetailView, UnitDetailView, MaterialDetailView
from .views_lessonscreate import BlockCreateView, UnitCreateView, MaterialCreateView
from .views_lessonsupdate import BlockUpdateView, UnitUpdateView, MaterialUpdateView
# import from django
from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()
# import from netteachers apps
# import from own app
from .views_announcements import AnnouncementCreateView, AnnouncementDeleteView, \
    AnnouncementsListView, AnnouncementUpdateView
from .views_publication import LessonsPublishView, create_publication, delete_publication
from .views_forumbuild import ForumBuildView
from .views_forumbuild import SubForumCreateView, SubForumUpdateView
    # SubForumUpdateView, SubForumDeleteView



# for the download of files
download = ObjectDownloadView.as_view(model=CourseMaterialUnit, file_field='file')


urlpatterns = patterns('',
    # urls for update of course description parts
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung$', CourseDetailView.as_view(), name='start'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/text/bearbeiten$',
        CourseUpdateTextView.as_view(), name='coursetextupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/abstrakt/bearbeiten$',
        CourseUpdateExcerptView.as_view(), name='courseexcerptupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/zielgruppe/bearbeiten$',
        CourseUpdateTargetgroupView.as_view(), name='coursetargetgroupupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/voraussetzungen/bearbeiten$',
        CourseUpdatePrerequisitesView.as_view(), name='courseprerequisitesupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/projekt/bearbeiten$',
        CourseUpdateProjectView.as_view(), name='courseprojectupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/gliederung/bearbeiten$',
        CourseUpdateStructureView.as_view(), name='coursestructureupdate'),

    # urls for showing and update of courseowners information
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/kursleitung$', CourseOwnersListView.as_view(), name='ownerslist'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/kursleitung/(?P<user>\d{1,4})/aendern$',
        CourseOwnerUpdateView.as_view(), name='ownerupdate'),

    # url for courseevents
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/(?P<ce_slug>[a-z0-9_-]{3,50})$',
        CourseEventDetailView.as_view(), name='courseevent'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/(?P<ce_slug>[a-z0-9_-]{3,50})/text/bearbeiten$',
        CourseEventUpdateTextView.as_view(), name='courseeventtextupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/(?P<ce_slug>[a-z0-9_-]{3,50})/abstrakt/bearbeiten$',
        CourseEventUpdateExcerptView.as_view(), name='courseeventexcerptupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/(?P<ce_slug>[a-z0-9_-]{3,50})/format/bearbeiten$',
        CourseEventUpdateFormatView.as_view(), name='courseeventformatupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/(?P<ce_slug>[a-z0-9_-]{3,50})/arbeitslast/bearbeiten$',
        CourseEventUpdateWorkloadView.as_view(), name='courseeventworkloadupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/(?P<ce_slug>[a-z0-9_-]{3,50})/projekt/bearbeiten$',
        CourseEventUpdateProjectView.as_view(), name='courseeventprojectupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/(?P<ce_slug>[a-z0-9_-]{3,50})/gliederung/bearbeiten$',
        CourseEventUpdateStructureView.as_view(), name='courseeventstructureupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/(?P<ce_slug>[a-z0-9_-]{3,50})/zielgruppe/bearbeiten$',
        CourseEventUpdateTargetgroupView.as_view(), name='courseeventtargetgroupupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/beschreibung/(?P<ce_slug>[a-z0-9_-]{3,50})/voraussetzungen/bearbeiten$',
        CourseEventUpdatePrerequisitesView.as_view(), name='courseeventprerequisitesupdate'),


    # urls for viewing lessons
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/unterricht/ansicht$',
        LessonsView.as_view(), name='lessons'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/unterricht/ansicht/block/(?P<block>\d{1,4})$',
        BlockDetailView.as_view(), name='blockdetail'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/unterricht/ansicht/lektion/(?P<unit>\d{1,4})$',
        UnitDetailView.as_view(), name='unitdetail'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/unterricht/ansicht/material/(?P<material>\d{1,4})$',
        MaterialDetailView.as_view(), name='materialdetail'),

    # urls for create lessons view
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/unterricht/bearbeiten/block$',
        BlockCreateView.as_view(), name='blockcreate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/unterricht/bearbeiten/lektion$',
        UnitCreateView.as_view(), name='unitcreate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/unterricht/bearbeiten/material$',
        MaterialCreateView.as_view(), name='materialcreate'),

    # urls for update lessons view
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/unterricht/bearbeiten/block/(?P<block>\d{1,4})/aendern$',
        BlockUpdateView.as_view(), name='blockupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/unterricht/bearbeiten/lektion/(?P<unit>\d{1,4})/aendern$',
        UnitUpdateView.as_view(), name='unitupdate'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/unterricht/bearbeiten/material/(?P<material>\d{1,4})/aendern$',
        MaterialUpdateView.as_view(), name='materialupdate'),


    # urls for downloading pdf files
    url(r'^download/(?P<slug>[a-zA-Z0-9_-]+)/$', download, name="download"),

    # url for courseparticipants
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/teilnehmer$',
        CourseParticipantsListView.as_view(), name='participantslist'),

    # publications
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/Lektionen/freischalten$', LessonsPublishView.as_view(),
        name='publishlessons'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/(?P<unit>\d{1,4})/sperren$', delete_publication,
        name='deletepublication'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/(?P<unit>\d{1,4})/freischalten$', create_publication,
        name='createpublication'),


    # announcements
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/ankuendigungen$', AnnouncementsListView.as_view(),
        name='listannouncements'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/ankuendigungen/(?P<announcement>\d{1,4})/bearbeiten$', AnnouncementUpdateView.as_view(),
        name='updateannouncement'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/ankuendigungen/(?P<announcement>\d{1,4})/loeschen$', AnnouncementDeleteView.as_view(),
        name='deleteannouncement'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/ankuendigungen/schreiben$', AnnouncementCreateView.as_view(),
        name='createannouncement'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/forum$', ForumBuildView.as_view(),
        name='buildforum'),

    # forum
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/forum/anlegen$',
        SubForumCreateView.as_view(), name='createsubforum'),
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/forum/(?P<subforum>\d{1,4})/bearbeiten$',
        SubForumUpdateView.as_view(), name='updatesubforum'),
    #url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/forum/(?P<subforum>\d{1,4})/loeschen$', SubForumDeleteView.as_view(),
    #    name='deletesubforum'),

)
