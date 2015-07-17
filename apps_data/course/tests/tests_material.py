# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.test import TestCase

from ..models import Material

from .factories import CourseFactory, MaterialFactory

from django.test import Client


client = Client()

class MaterialCreateTest(TestCase):
    """
    Test the creation of a courseowner
    For a User: testuser1
    and a Course: with title="title" and slug="slug" a courseowner is created
    """
    def setUp(self):
        self.slug = "slug"
        self.course = CourseFactory.create(slug=self.slug)

    def test_create_material(self):
        """
        asserts that one courseowner records exists
        """
        material = Material(title="title")
        material.save()
        self.assertEqual(Material.objects.all().count(), 1)

