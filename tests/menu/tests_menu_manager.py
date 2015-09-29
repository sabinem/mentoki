# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.test import TestCase

from ..factories import CourseEventFactory, ForumFactory, ClassLessonFactory
from apps_data.lesson.tests.factories import ClassLessonFactory

from apps_data.courseevent.models.menu import ClassroomMenuItem
from apps_data.courseevent.models.forum import Forum


class MenuItemManagerTest(TestCase):
    """
    Tests the mamager methods for menu items

    Setup:
    - there are 2 courseevents: courseevent1 and courseevent2
    - there are 3 forums: forum1, forum2 belong to courseevent1
                          forum3 belongs to courseevent2
    - there are 3 classlessons: classlesson1 and classlesson2 that
                   belongs to courseevent1
                   and classlesson 3 belongs to courseevent2
    - there are 2 classlessons: classlesson1 and classlesson2 that
                   belongs to courseevent1
                   and classlesson 3 belongs to courseevent2
    """
    def setUp(self):
        self.courseevent1_slug = 'ceslug1'
        self.courseevent1 = CourseEventFactory.create(title="cetitle1",
                                                slug=self.courseevent1_slug)
        self.courseevent2_slug = 'ceslug2'
        self.courseevent2 = CourseEventFactory.create(title="cetitle2",
                                                slug=self.courseevent2_slug)
        self.rootforum = ForumFactory(parent=None,
                                      display_nr=1,
                                      title="rootforum",
                                      courseevent=self.courseevent1
                                      )
        self.forum1 = ForumFactory(
            parent=self.rootforum,
            display_nr=1,
            title="forum1",
            courseevent=self.courseevent1
        )
        self.forum2 = ForumFactory(
            parent=self.rootforum,
            display_nr=2,
            title="forum2",
            courseevent=self.courseevent1
        )
        self.forum3 = ForumFactory(
            parent=self.rootforum,
            display_nr=3,
            title="forum3",
            courseevent=self.courseevent2
        )
        self.classlessonroot = ClassLessonFactory(
            parent=None,
            courseevent=self.courseevent1,
            course=self.courseevent1.course,
            title="classlessonroot1",
            nr=1
        )
        self.classlessonblock = ClassLessonFactory(
            parent=self.classlessonroot,
            courseevent=self.courseevent1,
            course=self.courseevent1.course,
            nr=1,
            title="classlessonblock1"
        )
        self.classlesson1 = ClassLessonFactory(
            parent=self.classlessonblock,
            courseevent=self.courseevent1,
            course=self.courseevent1.course,
            nr=1,
            title="classlesson1",
        )
        self.menuitem1 = ClassroomMenuItemFactory(courseevent=self.courseevent1,
                                                  display_nr=1,
                                                  display_title="display_title1",
                                                  item_type="header_item",
                                                  is_shortlink=False)
        self.menuitem2 = ClassroomMenuItemFactory(courseevent=self.courseevent2,
                                                  display_nr=2,
                                                  display_title="display_title2",
                                                  item_type="header_item")
        self.menuitem3 = ClassroomMenuItemFactory(courseevent=self.courseevent1,
                                                  display_nr=1,
                                                  display_title="display_title3",
                                                  item_type="header_item",
                                                  is_shortlink=True)
        self.menuitem4 = ClassroomMenuItemFactory(courseevent=self.courseevent1,
                                                  display_nr=1,
                                                  forum = self.forum1,
                                                  display_title="display_title4",
                                                  item_type="forum_item",
                                                  is_shortlink=True)
        self.menuitem5 = ClassroomMenuItemFactory(courseevent=self.courseevent1,
                                                  display_nr=4,
                                                  classlesson = self.classlesson1,
                                                  display_title="display_title5",
                                                  item_type="lesson_item",
                                                  is_shortlink=True)

    def test_classroommenitem_qs_all_for_courseevent(self):
        """
        Classrommmenitem.objects.all_for_courseevent (queryset in CourseOwnerManager)
        --------------------------------
        expected all menu_items_for_one_courseevent
        """
        menu_qs = ClassroomMenuItem.objects.all_for_courseevent(
            courseevent=self.courseevent1)
        self.assertQuerysetEqual(
            menu_qs,
            [repr(self.menuitem1),repr(self.menuitem3)],
            ordered=False)

    def test_classroommenuitem_qs_shortlinks_for_courseevent(self):
        """
        Classrommmenitem.objects.all_for_courseevent (queryset in CourseOwnerManager)
        --------------------------------
        expected all menu_items_for_one_courseevent
        """
        menu_qs = ClassroomMenuItem.objects.shortlinks_for_courseevent(
            courseevent=self.courseevent1)
        self.assertQuerysetEqual(menu_qs, [repr(self.menuitem3),
                                           repr(self.menuitem4),
                                           repr(self.menuitem5)])