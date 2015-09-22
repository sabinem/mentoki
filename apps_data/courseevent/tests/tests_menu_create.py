# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.test import TestCase

from ..models.menu import ClassroomMenuItem
from .factories import CourseEventFactory


class MenuItemCreateTest(TestCase):
    """
    Test the creation of a menuitem
    A Menuitem with the display_title="title1" and the display_nr 1 and
    item-type "header" is created
    """
    def setUp(self):
        self.courseevent1 = CourseEventFactory.create()

    def test_create_classroommenuitem(self):
        """
        Asserts that a menuitem can be created with just title, nr and item_type given
        """
        self.classroommenuitem = ClassroomMenuItem(display_title='menu1',
                                                   display_nr=1,
                                                   item_type='header',
                                                   courseevent=self.courseevent1
                                                   )
        self.classroommenuitem.save()
        # retrieve: only one menu item
        self.assertEqual(ClassroomMenuItem.objects.all().count(), 1)
