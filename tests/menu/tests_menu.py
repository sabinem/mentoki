# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.test import TestCase, Client

from apps_data.courseevent.models.menu import ClassroomMenuItem
from ..factories import CourseFactory, CourseEventFactory, ForumFactory, \
    ClassLessonFactory, SiteFactory


class MenuItemCreateTest(TestCase):
    """
    Test the creation of a menuitem
    A Menuitem with the display_title="title1" and the display_nr 1 and
    item-type "header" is created
    """
    def setUp(self):
        # client
        self.client = Client()

        # create site
        self.domain = '127.0.0.1:8000'
        self.site = SiteFactory.create(name='localhost', domain=self.domain)

        # create courses
        self.course_slug1 = "course1"
        self.course1 = CourseFactory.create(title="Course 1",
                                            slug=self.course_slug1)
        self.course_slug2 = "course2"
        self.course2 = CourseFactory.create(title="Course 2",
                                            slug=self.course_slug2)
        #create courseevents
        self.event_slug1 = "event1"
        self.event1 = CourseEventFactory.create(title="Event 1",
                                                 slug=self.event_slug1,
                                                 course=self.course1)
        self.event_slug2 = "event2"
        self.event2 = CourseEventFactory.create(title="Event 2",
                                                 slug=self.event_slug2,
                                                 course=self.course1)
        self.event_slug3 = "event3"
        self.event3 = CourseEventFactory.create(title="Event 3",
                                                 slug=self.event_slug3,
                                                 course=self.course2)

    def test_create_classroommenuitem(self):
        """
        apps_data.courseevent.models.menu
        model: ClassroomMenuItem,  method: create
        -------------------------------------------
        Asserts that a menuitem can be created with just title, nr
        and item_type given
        """
        self.classroommenuitem = ClassroomMenuItem(
            display_title='menu1',
            display_nr=1,
            item_type='header',
            courseevent=self.event1
            )
        self.classroommenuitem.save()
        self.assertEqual(ClassroomMenuItem.objects.all().count(), 1)

    def test_clean_classroommenuitem(self):
        """
        apps_data.courseevent.models.menu
        model: ClassroomMenuItem,  method: create
        -------------------------------------------
        Asserts that a menuitem can be created with just title, nr
        and item_type given
        """
        self.classroommenuitem = ClassroomMenuItem(
            display_title='menu1',
            display_nr=1,
            item_type='header',
            courseevent=self.event1
            )
        self.classroommenuitem.save()
        self.assertEqual(ClassroomMenuItem.objects.all().count(), 1)