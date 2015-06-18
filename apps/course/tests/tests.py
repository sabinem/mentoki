from django.test import TestCase
from django.contrib.auth import get_user_model


# tests.py
import random
import string

from django.test import TestCase

from ..models import Course


def random_string(length=10):
    return u''.join(random.choice(string.ascii_letters) for x in range(length))


class CourseCreateTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')

    def test_create_course(self):
        # create unpublished newsletter
        course = Course(title='Title Me', slug='titleme')
        course.save()
        # retrieve: only one newsletter, but no published one
        self.assertEqual(Course.objects.all().count(), 1)



def random_string(length=10):
    return u''.join(random.choice(string.ascii_letters) for x in range(length))


class ThingTestCase(TestCase):

    def create_thing(self, **kwargs):
        "Create a random test thing."
        options = {
            'name': random_string(),
            'description': random_string(),
        }
        options.update(kwargs)
        return Thing.objects.create(**options)

    def test_something(self):
        # Get a completely random thing
        thing = self.create_thing()
        # Test assertions would go here

    def test_something_else(self):
        # Get a thing with an explicit name
        thing = self.create_thing(name='Foo')
        # Test assertions would go here