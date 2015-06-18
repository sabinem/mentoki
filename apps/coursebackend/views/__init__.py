# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .course import CourseDetailView, CourseUpdateView

from .courseowner import CourseOwnerListView, CourseOwnerUpdateView

from .courseevent import CourseEventDetailView, CourseEventUpdateView, \
    CourseEventPublicInformationUpdateView, CourseEventExcerptUpdateView

from .lesson import LessonBlockView, LessonUpdateView, StepDetailView,\
    LessonDetailView, StartView, \
    LessonCreateView, LessonDeleteView, LessonAddMaterialView

from .material import MaterialCreateView, MaterialDeleteView, MaterialUpdateView, \
    MaterialListView, MaterialDetailView

#from .announcement import AnnouncementCreateView, AnnouncementDeleteView, AnnouncementsListView, AnnouncementUpdateView

