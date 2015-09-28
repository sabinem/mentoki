"""
should I test __unicode__ method and get_absolute_url?
"""

# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model
from django.core.validators import ValidationError

from django.test import TestCase, Client

from apps_data.courseevent.models.courseevent import CourseEvent
from .factories import CourseFactory


class AnnouncementModelTest(TestCase):
    """
    Test the creation of a course
    A Course with the title="title" is created
    """
"""
should I test __unicode__ method and get_absolute_url?
"""

# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model
from django.core.validators import ValidationError

from django.test import TestCase, Client

from apps_data.course.models.course import Course, CourseOwner, foto_location
from .factories import CourseFactory


class CourseandCourseOwnerTest(TestCase):
    """
    Test the methods and attributes and querysets of course and courseowner:
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
        ownership1: testuser1 for course1: display, 1.
        ownership2: testuser2 for course1: display=False, 2.
        ownership3: testuser3 for course2:

        Courseevents are created
        -------------------------
        event1: "Event 1" slug: "event1" belongs to: course1
        event2: "Event 2" slug: "event2  belongs to: course1
        event3: "Event 3" slug: "event3  belongs to: course2

        Participants are created
        ------------------------
        participant1: testuser3 for course1
        participant2: testuser4 for course1
        participant3: testuser5 for course2
        participant4: testuser6 for course2

        Announcements are created:
        ---------------------------
        announcement1: "Announcement 1" for "event1": published, archived=False
        announcement2: "Announcement 2" for "event1": published=False
        announcement3: "Announcement 3" for "event1": published, archived
        announcement4: "Announcement 4" for "event1": published, archived=False
        announcement5: "Announcement 5" for "event2": published, archived=False
        announcement6: "Announcement 6" for "event2": published=False
        announcement7: "Announcement 7" for "event2": published, archived
        announcement8: "Announcement 8" for "event3": published, archived=False
        announcement9: "Announcement 9" for "event3": published=False
        announcementa: "Announcement a" for "event3": published, archived
        """
        # create courses
        self.course_slug1 = "course1"
        self.course_slug2 = "course2"
        self.course = CourseFactory.create(title="Course 1", slug=self.course_slug1)
        self.course2 = CourseFactory.create(title="Course 2", slug=self.course_slug2)
        # create users
        self.title = "title"
        self.email1 = "u1@gmail.com"
        self.email2 = "u2@gmail.com"
        self.domain = '127.0.0.1:8000'
        # create courseownerships

        # create courseevents

        # create participations

        # create announcements
        self.site = SiteFactory.create(name='localhost', domain=self.domain)
        self.course = CourseFactory.create(title=self.title, slug=self.slug)
        self.course2 = CourseFactory.create(title="ttile2", slug="slug2")
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
        self.ownership1 = CourseOwner(course=self.course, user=self.user1,
                                 display_nr=1, display=True)
        self.ownership1.save()
        self.ownership2 = CourseOwner(course=self.course, user=self.user2,
                                 display_nr=2, display=False)
        self.ownership2.save()
        self.ownership3 = CourseOwner(course=self.course2, user=self.user3,
                                 display_nr=1, display=True)
        self.ownership3.save()


    def test_create_course(self):
        """
        Asserts that a course exists after the creation
        """
        self.courseevent = CourseEvent(title='title1')
        #self.Site = Site.objects.create()
        self.course.save()
        # retrieve exactly one course
        self.assertEqual(Course.objects.all().count(), 1)


class CourseandCourseOwnerTest(TestCase):
    """
    Test the methods and attributes and querysets of course and courseowner:
    """
    def setUp(self):
        """
        A Course is created: title = "title", slug = "slug"
        Users are created: testuser1: "firstname1 lastname1"
                           testuser2: "firstname2 lastname2"
                           testuser3: "firstname3 lastname3"
        The testuser1 and testuser2 are both declared to teachers
        of the course: testuser1 being the main teacher is displayed
        first and full. Whereas teacher2 is the assistant teacher
        appearing second. testuser3 stays unassigned.
        """
        self.client = Client()
        self.slug = "slug"
        self.title = "title"
        self.email1 = "u1@gmail.com"
        self.email2 = "u2@gmail.com"
        self.domain = '127.0.0.1:8000'
        self.site = SiteFactory.create(name='localhost', domain=self.domain)
        self.course = CourseFactory.create(title=self.title, slug=self.slug)
        self.course2 = CourseFactory.create(title="ttile2", slug="slug2")
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
        self.ownership1 = CourseOwner(course=self.course, user=self.user1,
                                 display_nr=1, display=True)
        self.ownership1.save()
        self.ownership2 = CourseOwner(course=self.course, user=self.user2,
                                 display_nr=2, display=False)
        self.ownership2.save()
        self.ownership3 = CourseOwner(course=self.course2, user=self.user3,
                                 display_nr=1, display=True)
        self.ownership3.save()

    def test_course_property_teachersrecord(self):
        """
        course.teachersrecord:
        -----------------------------------
        Teachers should be shown as a record with main teacher appearing first
        """
        self.assertEqual(self.course.teachersrecord,
                         "firstname1 lastname1 und firstname2 lastname2")

    def test_course_property_teachers(self):
        """
        course.teachers:
        -----------------------------------
        expected: the users as queryset in the appropriate order
        """
        self.assertQuerysetEqual(self.course.teachers,
                                 [repr(self.user1), repr(self.user2)])
        self.assertQuerysetEqual(self.course2.teachers,
                                 [repr(self.user3)])

    def test_course_method_is_owner(self):
        """
        course.is_owner(user):
        -----------------------------------
        True if user is a teacher
        """
        self.assertEqual(self.course.is_owner(self.user1), True)
        self.assertEqual(self.course.is_owner(self.user2), True)
        self.assertEqual(self.course.is_owner(self.user3), False)

    def test_course_method_get_absolute_url(self):
        """
        course.get_absolute_url
        --------------------------------
        test absolute_url of course
        """
        url = self.course.get_absolute_url()
        self.assertEqual(url, '/de-de/slug/kursvorbereitung/vorlage/')

    def test_courseownermanager_qs_teachers_courseinfo_display(self):
        """
        CourseOwner.objects.teachers_courseeinfo_display
        --------------------------------
        expected ownership records for the teachers whoes profiles should be
        displayed on the public page of the course
        """
        courseowners_qs = CourseOwner.objects.\
            teachers_courseinfo_display(self.course)
        self.assertQuerysetEqual(courseowners_qs, [repr(self.ownership1)])

    def test_courseownermanager_qs_teachers_courseinfo_all(self):
        """
        CourseOwner.objects.teachers_courseeinfo_all
        --------------------------------
        expected ownership records of all teachers of the course
        """
        courseowners_qs = CourseOwner.objects.\
            teachers_courseinfo_all(self.course)
        self.assertQuerysetEqual(courseowners_qs, [repr(self.ownership1),
                                                   repr(self.ownership2)])

    def test_courseownermanager_qs_teachers_emails(self):
        """
        CourseOwner.objects.teachers_emails (queryset in CourseOwnerManager)
        --------------------------------
        expected flat list of emails of all teachers of the course
        expected: user 1
        """
        courseowners_qs = CourseOwner.objects.\
            teachers_emails(self.course)
        self.assertQuerysetEqual(courseowners_qs, [repr(self.email1),
                                                   repr(self.email2)])

    def test_courseownermanager_qs_other_teachers_for_display(self):
        """
        CourseOwner.objects (queryset in CourseOwnerManager)
        --------------------------------
        expected return ownershiprecords of teachers other then the given
        user, that will be displayed on the public page of the course.
        """
        courseowners_qs = CourseOwner.objects.\
            other_teachers_for_display(self.course, self.user2)
        self.assertQuerysetEqual(courseowners_qs, [repr(self.ownership1)])
        courseowners_qs = CourseOwner.objects.\
            other_teachers_for_display(self.course2, self.user3)
        self.assertQuerysetEqual(courseowners_qs, [])

    def test_foto_location(self):
        """
        foto_location (function)
        --------------------------------
        foto  is stored in the directory with course slug under its filename
        expected:  <course-slug>/<filename>
        """
        instance = self.ownership1
        filename = 'filename'
        foto_location(instance, filename)
        self.assertEqual(foto_location(instance, filename), 'slug/filename')

    def test_courseowner_method_get_absolute_url(self):
        """
        courseowner.get_absolute_url
        --------------------------------
        test absolute_url of course
        """
        url = self.ownership1.get_absolute_url()
        self.assertEqual(url, '/de-de/slug/kursvorbereitung/leitung/1')

    def test_courseowner_method_clean(self):
        """
        courseowner.clean
        --------------------------------
        test clean method of model CourseOwner
        expected: one teacher of the course must be displayed on the public
        page
        """
        with self.assertRaises(ValidationError):
            self.ownership1.display = False
            self.ownership1.save()

    def test_course_unicode(self):
        """
        course.__unicode__
        --------------------------------------
        self representation of Course
        """
        self.assertEqual(repr(self.course), '<Course: title>')

    def test_courseowner_unicode(self):
        """
        courseowner.__unicode__
        --------------------------------------
        self representation of CourseOwner
        """
        self.assertEqual(repr(self.ownership1), '<CourseOwner: title testuser1>')
