from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Course


class CourseCreateTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')

    def test_create_course(self):
        # create unpublished newsletter
        course = Course(title='Title Me', slug='titleme')
        course.save()
        # retrieve: only one newsletter, but no published one
        self.assertEqual(Course.objects.all().count(), 1)
