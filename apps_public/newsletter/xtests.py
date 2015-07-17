from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Newsletter

import unittest


class NewsletterCreateAndPublishTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')

    def test_create_unpublished_newsletter(self):
        # create unpublished newsletter
        newsletter = Newsletter(title='Title Me', content='', published=False)
        newsletter.save()
        # retrieve: only one newsletter, but no published one
        self.assertEqual(Newsletter.objects.all().count(), 1)
        self.assertEqual(Newsletter.objects.published().count(), 0)
        # publish newsletter
        newsletter.published = True
        newsletter.save()
        # now there is a published newsletter
        self.assertEqual(Newsletter.objects.published().count(), 1)


class NewslettersViewTests(TestCase):
    def test_feed_url(self):
        # test feed_url
        response = self.client.get('/feed/')
        self.assertIn("xml", response['Content-Type'])