"""
should I test __unicode__ method and get_absolute_url?
"""

# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model

from django.test import TestCase, Client

from ..models.course import Course, CourseOwner, foto_location
from .factories import CourseFactory, SiteFactory


class CourseCreateTest(TestCase):
    """
    Test the creation of a course
    A Course with the title="title" is created
    """
    def setUp(self):
        pass

    def test_create_course(self):
        """
        Asserts that a course exists after the creation
        """
        self.course = Course(title='title1')
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
        self.domain = '127.0.0.1:8000'
        self.site = SiteFactory.create(name='localhost', domain=self.domain)
        self.course = CourseFactory.create(title="title", slug=self.slug)
        self.user1 = get_user_model().objects.create(
            username='testuser1',
            first_name="firstname1",
            last_name="lastname1",
            email="u1@gmail.com")
        self.user2 = get_user_model().objects.create(
            username='testuser2',
            first_name="firstname2",
            last_name="lastname2",
            email="u2@gmail.com")
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
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

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
        self.assertQuerysetEqual(courseowners_qs, [repr(self.ownership1), repr(self.ownership2)])

    def test_courseownermanager_qs_teachers_emails(self):
        """
        CourseOwner.objects.teachers_emails (queryset in CourseOwnerManager)
        --------------------------------
        expected flat list of emails of all teachers of the course
        expected: user 1
        """
        courseowners_qs = CourseOwner.objects.\
            teachers_emails(self.course)
        print courseowners_qs
        self.assertQuerysetEqual(courseowners_qs, ['u1@gmail.com', 'u2@gmail.com'])

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
        pass

    def test_courseowner_method_clean(self):
        pass

    def test_courseowner_unicode(self):
        pass

