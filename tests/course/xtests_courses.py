"""
Tests Courses: models, updates, CourseOwner Updates,
Views and Forms

tested are the following apps and models/views:

1. apps_data.course.models.course: models Course and CourseOwner
2. apps_internal.coursebackend.views.course

"""

# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model
from django.core.validators import ValidationError

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from apps_data.course.models.course import CourseOwner, foto_location
from ..factories import CourseFactory, SiteFactory
from apps_internal.coursebackend.views.mixins.base import AuthMixin

from django.test import Client


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
        testuser4: is_superuser "username4" "u4@gmail.com"

        CourseOwnerships are created
        -----------------------------
        ownership1: testuser1 for course1: display, display_nr=1
        ownership2: testuser2 for course1: display=False, display_nr=2
        ownership3: testuser3 for course2:
        """
        # client
        self.client = Client()

        # create site
        self.domain = '127.0.0.1:8000'
        self.site = SiteFactory.create(name='localhost', domain=self.domain)

        # create courses
        self.course_slug1 = "course1"
        self.course1 = CourseFactory.create(title="Course 1", slug=self.course_slug1)
        self.course_slug2 = "course2"
        self.course2 = CourseFactory.create(title="Course 2", slug=self.course_slug2)

        # create users
        self.email1 = "u1@gmail.com"
        self.email2 = "u2@gmail.com"
        self.email3 = "u3@gmail.com"
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
            is_superuser=True,
            email="u4@gmail.com")

        # create ownerships
        self.ownership1 = CourseOwner(course=self.course1, user=self.user1,
                                 display_nr=1, display=True)
        self.ownership1.save()
        self.ownership2 = CourseOwner(course=self.course1, user=self.user2,
                                 display_nr=2, display=False)
        self.ownership2.save()
        self.ownership3 = CourseOwner(course=self.course2, user=self.user3,
                                 display_nr=1, display=True)
        self.ownership3.save()

    def test_course_property_teachersrecord(self):
        """
        apps_data.course.models.course
        model: Course, method: teachersrecord
        -------------------------------------
        Teachers should be shown as a record of names
        with main teacher appearing first
        """
        self.assertEqual(self.course1.teachersrecord,
                         "firstname1 lastname1 und firstname2 lastname2")

    def test_course_property_teachers(self):
        """
        apps_data.course.models.course
        model: Course, method: teachers
        -----------------------------------
        expected: owners as queryset in the appropriate order
        """
        self.assertQuerysetEqual(self.course1.teachers,
                                 [repr(self.user1), repr(self.user2)])
        self.assertQuerysetEqual(self.course2.teachers,
                                 [repr(self.user3)])

    def test_course_method_is_owner(self):
        """
        apps_data.course.models.course
        model: Course, method: is_owner(user)
        ---------------------------------------
        True if user is a teacher
        """
        self.assertEqual(self.course1.is_owner(self.user1), True)
        self.assertEqual(self.course1.is_owner(self.user2), True)
        self.assertEqual(self.course1.is_owner(self.user3), False)

    def test_course_method_get_absolute_url(self):
        """
        apps_data.course.models.course
        model: Course, method: get_absolute_url
        ---------------------------------------
        test absolute_url of course
        """
        url = self.course1.get_absolute_url()
        self.assertEqual(url, '/de/course1/kursvorbereitung/vorlage/')

    def test_courseownermanager_qs_teachers_courseinfo_display(self):
        """
        apps_data.course.models.course
        CourseOwner.objects.teachers_courseeinfo_display
        --------------------------------
        expected ownership records for the teachers whoes profiles should be
        displayed on the public page of the course
        """
        courseowners_qs = CourseOwner.objects.\
            teachers_courseinfo_display(self.course1)
        self.assertQuerysetEqual(courseowners_qs, [repr(self.ownership1)])

    def test_courseownermanager_qs_teachers_courseinfo_all(self):
        """
        apps_data.course.models.course
        model: CourseOwner, manager_method: teachers_courseeinfo_all
        ------------------------------------------------------------
        expected ownership records of all teachers of the course
        """
        courseowners_qs = CourseOwner.objects.\
            teachers_courseinfo_all(self.course1)
        self.assertQuerysetEqual(courseowners_qs, [repr(self.ownership1),
                                                   repr(self.ownership2)])

    def test_courseownermanager_qs_teachers_emails(self):
        """
        apps_data.course.models.course
        model: CourseOwner, manager_method: teachers_emails
        ----------------------------------------------------
        expected flat list of emails of all teachers of the course
        expected: user 1
        """
        courseowners_qs = CourseOwner.objects.\
            teachers_emails(self.course1)
        self.assertQuerysetEqual(courseowners_qs, [repr(self.email1),
                                                   repr(self.email2)])

    def test_courseownermanager_qs_other_teachers_for_display(self):
        """
        apps_data.course.models.course
        model: CourseOwner, manager_method: other_teachers_for_display
        ----------------------------------------------------------------
        expected return ownershiprecords of teachers other then the given
        user, that will be displayed on the public page of the course.
        """
        courseowners_qs = CourseOwner.objects.\
            other_teachers_for_display(self.course1, self.user2)
        self.assertQuerysetEqual(courseowners_qs, [repr(self.ownership1)])
        courseowners_qs = CourseOwner.objects.\
            other_teachers_for_display(self.course2, self.user3)
        self.assertQuerysetEqual(courseowners_qs, [])

    def test_foto_location(self):
        """
        apps_data.course.models.course
        function: foto_location
        --------------------------------
        foto  is stored in the directory with course slug under its filename
        expected:  <course-slug>/<filename>
        """
        instance = self.ownership1
        filename = 'filename'
        foto_location(instance, filename)
        self.assertEqual(foto_location(instance, filename), 'course1/filename')

    def test_courseowner_method_clean(self):
        """
        apps_data.course.models.course
        model: CourseOwner,  method: clean
        --------------------------------
        test clean method of model CourseOwner
        expected: one teacher of the course must be displayed on the public
        page
        """
        self.ownership1.display = False
        self.assertRaises(ValidationError, self.ownership1.clean)

    def test_course_unicode(self):
        """
        apps_data.course.models.course
        model: Course,  method: __unicode__
        --------------------------------------
        self representation of Course
        """
        self.assertEqual(repr(self.course1), '<Course: Course 1>')

    def test_courseowner_unicode(self):
        """
        apps_data.course.models.course
        model: CourseOwner,  method: __unicode__
        ------------------------------------------
        self representation of CourseOwner
        """
        self.assertEqual(repr(self.ownership1), '<CourseOwner: Course 1 testuser1>')

    def test_auth_mixin_coursebackend(self):
        """
        apps_internal.coursebackend.views.mixins.base
        class: AuthMixin method:test_func(user):
        -----------------------------------------
        expected: only owners and the superuser are allowed. In these
        cases the function returns True, otherwise it returns False.
        """
        self.client.login(username='testuser1', password='asdf1234')
        url = reverse('coursebackend:course:detail',
                      kwargs={'course_slug': self.course_slug1})
        self.assertEqual(url,'/de-de/course1/kursvorbereitung/vorlage/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, _('Beitrag'))
