# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model

from django.test import TestCase, Client

from ..models.course import Course, CourseOwner
from .factories import CourseFactory


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
        self.Site.create()
        self.course.save()
        # retrieve exactly one course
        self.assertEqual(Course.objects.all().count(), 1)


class CourseandCourseOwnerTest(TestCase):
    """
    Test the methods and attributes of course
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
        ownership1 = CourseOwner(course=self.course, user=self.user1,
                                 display_nr=1, display=True)
        ownership1.save()
        ownership2 = CourseOwner(course=self.course, user=self.user2,
                                 display_nr=2, display=False)
        ownership2.save()

    def test_course_property_teachersrecord(self):
        """
        Teachers should be showed as a record with main teacher appearing first
        """
        self.assertEqual(self.course.teachersrecord,
                         "firstname1 lastname1 und firstname2 lastname2")

    def test_course_property_teachers(self):
        """
        Teachers should be the user records in the appropriate order
        """
        self.assertQuerysetEqual(self.course.teachers,
                                 [repr(self.user1), repr(self.user2)])

    def test_course_method_is_owner(self):
        """
        Teachers should be the user records in the appropriate order
        """
        self.assertEqual(self.course.is_owner(self.user1), True)
        self.assertEqual(self.course.is_owner(self.user2), True)
        self.assertEqual(self.course.is_owner(self.user3), False)

    def test_course_method_get_absolute_url(self):
        """
        The course should be fetched from the slug
        """
        url = self.course.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_course_unicode(self):
        pass

    def test_courseownermanager_qs_teachers_courseinfo_display(self):
        courseowners_qs = CourseOwner.objects.\
            teachers_courseinfo_display(self, self.course)
        self.assertQuerysetEqual(courseowners_qs, [repr(self.user1)])

    def test_courseownermanager_qs_teachers_courseinfo_all(self):
        courseowners_qs = CourseOwner.objects.\
            teachers_courseinfo_display(self, self.course)
        self.assertQuerysetEqual(courseowners_qs, [repr(self.user1), repr(self.user2)])

    def test_courseownermanager_qs_teachers_emails(self):
        courseowners_qs = CourseOwner.objects.\
            teachers_emails(self, self.course)
        self.assertQuerysetEqual(courseowners_qs, ['u1@gmail.com', 'u1@gmail.com'])

    def test_foto_location(self):
        instance = self.course
        filename = 'x'
        #foto_location(instance, filename)

    def test_courseowner_method_get_absolute_url(self):
        pass

    def test_courseowner_method_clean(self):
        pass

    def test_courseowner_unicode(self):
        pass

