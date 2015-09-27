from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from apps_data.courseevent.models.courseevent import CourseEvent


class ThreadTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.courseevent = CourseEvent.objects.create(slug='examplecourse')

    def test_threadcreateview(self):
        url = reverse('classroom:forum:thread_create', kwargs={'slug': self.courseevent.slug})

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _('Beitrag'))


