from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Newsletter


class NewsletterSingleTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')

    def test_create_unpublished(self):
        newsletter = Newsletter(title='Title Me', content='', published=False)
        newsletter.save()
        self.assertEqual(Newsletter.objects.all().count(), 1)
        self.assertEqual(Newsletter.objects.published().count(), 0)
        newsletter.published = True
        newsletter.save()
        self.assertEqual(Newsletter.objects.published().count(), 1)


class NewslettersViewTests(TestCase):
    def test_feed_url(self):
        response = self.client.get('/feed/')
        self.assertIn("xml", response['Content-Type'])

