"""
should I test __unicode__ method and get_absolute_url?
"""

# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.core.validators import ValidationError

from django.test import TestCase, Client

from apps_data.courseevent.models.courseevent import CourseEvent, \
    CourseEventParticipation
from apps_data.courseevent.models.announcement import Announcement
from apps_data.course.models.course import CourseOwner
from ..factories import CourseFactory, SiteFactory, CourseEventFactory, \
   AnnouncementFactory


class AnnouncementModelTest(TestCase):
    """
    Tests everything for announcements: creation, delete, publication,
    archive them, etc.
    """
    def setUp(self):
        """
        Courses are created:
        --------------------
        course1: "Course 1" slug: "course1"
        course2: "Course 2" slug: "course2"

        Users are created:
        ------------------
        testuser1: "firstname1 lastname1" "username1" "u1@gmail.com"
        testuser2: "firstname2 lastname2" "username2" "u2@gmail.com"
        testuser3: "firstname3 lastname3" "username3" "u3@gmail.com"
        testuser4: "firstname4 lastname4" "username4" "u4@gmail.com"
        testuser5: "firstname5 lastname5" "username5" "u5@gmail.com"
        testuser6: "firstname6 lastname6" "username6" "u6@gmail.com"

        CourseOwnerships are created
        -----------------------------
        ownership1: testuser1 for course1:
        ownership2: testuser2 for course1:
        ownership3: testuser3 for course2:

        Courseevents are created
        -------------------------
        event1: "Event 1" slug: "event1" belongs to: course1
        event2: "Event 2" slug: "event2  belongs to: course1
        event3: "Event 3" slug: "event3  belongs to: course2

        Participants are created
        ------------------------
        participant1: user3 for event1
        participant2: user4 for event1
        participant3: user5 for event2
        participant4: user6 for event3

        Announcements are created:
        ---------------------------
        announcement1: "Announcement 1" for "event1": published
        announcement2: "Announcement 2" for "event1": published=False
        announcement3: "Announcement 3" for "event2": published
        announcement4: "Announcement 4" for "event2": published=False
        announcement5: "Announcement 5" for "event3": published
        announcement6: "Announcement 6" for "event3": published=False
        """

        # client
        self.client = Client()

        # create site
        self.domain = '127.0.0.1:8000'
        self.site = SiteFactory.create(name='localhost', domain=self.domain)

        # create courses
        self.course_slug1 = "course1"
        self.course1 = CourseFactory.create(title="Course 1",
                                            slug=self.course_slug1)
        self.course_slug2 = "course2"
        self.course2 = CourseFactory.create(title="Course 2",
                                            slug=self.course_slug2)

        # create users
        self.email1 = "u1@gmail.com"
        self.email2 = "u2@gmail.com"
        self.email3 = "u3@gmail.com"
        self.email4 = "u4@gmail.com"
        self.email5 = "u5@gmail.com"
        self.email6 = "u6@gmail.com"
        self.user1 = get_user_model().objects.create(
            username='testuser1',
            first_name="firstname1",
            last_name="lastname1",
            email=self.email1)
        self.user2 = get_user_model().objects.create(
            username='testuser2',
            first_name="firstname2",
            last_name="lastname2",
            email=self.email2)
        self.user3 = get_user_model().objects.create(
            username='testuser3',
            first_name="firstname3",
            last_name="lastname3",
            email="u3@gmail.com")
        self.user4 = get_user_model().objects.create(
            username='testuser4',
            first_name="firstname4",
            last_name="lastname4",
            email="u4@gmail.com")
        self.user5 = get_user_model().objects.create(
            username='testuser5',
            first_name="firstname5",
            last_name="lastname5",
            email="u5@gmail.com")
        self.user6 = get_user_model().objects.create(
            username='testuser6',
            first_name="firstname6",
            last_name="lastname6",
            email="u6@gmail.com")

        # create ownerships
        self.ownership1 = CourseOwner(course=self.course1, user=self.user1)
        self.ownership1.save()
        self.ownership2 = CourseOwner(course=self.course1, user=self.user2)
        self.ownership2.save()
        self.ownership3 = CourseOwner(course=self.course2, user=self.user3)
        self.ownership3.save()

        #create courseevents
        self.event_slug1 = "event1"
        self.event1 = CourseEventFactory.create(title="Event 1",
                                                 slug=self.event_slug1,
                                                 course=self.course1)
        self.event_slug2 = "event2"
        self.event2 = CourseEventFactory.create(title="Event 2",
                                                 slug=self.event_slug2,
                                                 course=self.course1)
        self.event_slug3 = "event3"
        self.event3 = CourseEventFactory.create(title="Event 3",
                                                 slug=self.event_slug3,
                                                 course=self.course2)
        # create ownerships
        self.participation1 = CourseEventParticipation(
            courseevent=self.event1, user=self.user3)
        self.participation1.save()
        self.participation2 = CourseEventParticipation(
            courseevent=self.event1, user=self.user4)
        self.participation2.save()
        self.participation3 = CourseEventParticipation(
            courseevent=self.event2, user=self.user5)
        self.participation3.save()
        self.participation4 = CourseEventParticipation(
            courseevent=self.event3, user=self.user6)
        self.participation4.save()

        # set up announcements in the background so that we know whether
        # the announcements get differentiated
        self.announcement1 = Announcement(title='title1', text="text1",
                                         courseevent=self.event1,
                                         published=True)
        self.announcement1.save()
        self.announcement2 = Announcement(title='title2', text="text2",
                                         courseevent=self.event2,
                                         published=True)
        self.announcement2.save()
        self.announcement3 = Announcement(title='title3', text="text3",
                                         courseevent=self.event3,
                                         published=True)
        self.announcement3.save()
        self.announcement4 = Announcement(title='title4', text="text4",
                                         courseevent=self.event1,
                                         published=False)
        self.announcement4.save()
        self.announcement5 = Announcement(title='title5', text="text5",
                                         courseevent=self.event2,
                                         published=False)
        self.announcement5.save()
        self.announcement6 = Announcement(title='title6', text="text6",
                                         courseevent=self.event3,
                                         published=False)
        self.announcement6.save()


    def test_create_announcement(self):
        """
        apps_data.course.models.course
        model: Announcement,  method: create, delete
        --------------------------------------
        Asserts that an announcement exists after the creation
        """
        self.assertEqual(Announcement.objects.all().count(), 6)
        self.announcement = Announcement(title='title1', text="text1",
                                         courseevent=self.event1)
        self.announcement.save()
        self.assertEqual(Announcement.objects.all().count(), 7)
        self.announcement.delete()
        self.assertEqual(Announcement.objects.all().count(), 6)

    def test_create_without_courseevent(self):
        """
        apps_data.course.models.course
        model: Announcement,  method: create
        ---------------------------------------------
        it is important that each announcement has a courseevent.
        """
        self.announcement = Announcement(title='title1', text="text1")
        self.assertRaises(IntegrityError, self.announcement.save)

    def test_lifecycle_of_annnouncement_that_starts_as_draft(self):
        """
        apps_data.course.models.course
        model: Announcement,  method: archive_announcement,
        unarchive_announcement publish_announcement
        model manager: Announcement, method:archived_announcements
        published_in_class, drafts_in_backend
        ----------------------------------------------------------
        it is important that each announcement has a courseevent.
        """
        self.assertEqual(Announcement.objects.all().count(), 6)
        self.assertEqual(Announcement.objects.archived_announcements(
            courseevent=self.event1
        ).count(), 0)
        self.assertEqual(Announcement.objects.published_in_class(
            courseevent=self.event1
        ).count(), 1)
        self.assertEqual(Announcement.objects.drafts_in_backend(
            courseevent=self.event1
        ).count(), 1)

        # establish one announcement as draft, the other as published
        self.announcement = Announcement(title='title1', text="text1",
                                         courseevent=self.event1)
        self.announcement.save()
        self.assertEqual(Announcement.objects.archived_announcements(
            courseevent=self.event1
        ).count(), 0)
        self.assertEqual(Announcement.objects.published_in_class(
            courseevent=self.event1
        ).count(), 1)
        self.assertEqual(Announcement.objects.drafts_in_backend(
            courseevent=self.event1
        ).count(), 2)

        # archivation of drafts should not be possible
        #self.assertRaises(IntegrityError,
        #                  self.announcement.archive_announcement())

        # publish the draft
        # during publication, there is a mail distributor established,
        # when the view tries to mail it out
        self.announcement.publish_announcement(mail_distributor=[])
        self.assertEqual(Announcement.objects.archived_announcements(
            courseevent=self.event1
        ).count(), 0)
        self.assertEqual(Announcement.objects.published_in_class(
            courseevent=self.event1
        ).count(), 2)
        self.assertEqual(Announcement.objects.drafts_in_backend(
            courseevent=self.event1
        ).count(), 1)

        # archive the announcement
        self.announcement.archive_announcement()
        self.assertEqual(Announcement.objects.archived_announcements(
            courseevent=self.event1
        ).count(), 1)
        self.assertEqual(Announcement.objects.published_in_class(
            courseevent=self.event1
        ).count(), 1)
        self.assertEqual(Announcement.objects.drafts_in_backend(
            courseevent=self.event1
        ).count(), 1)

        # pull the announcement back from archivation
        self.announcement.unarchive_announcement()
        self.assertEqual(Announcement.objects.archived_announcements(
            courseevent=self.event1
        ).count(), 0)
        self.assertEqual(Announcement.objects.published_in_class(
            courseevent=self.event1
        ).count(), 2)
        self.assertEqual(Announcement.objects.drafts_in_backend(
            courseevent=self.event1
        ).count(), 1)




