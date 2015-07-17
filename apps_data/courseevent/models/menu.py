# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from .courseevent import CourseEvent
from .forum import Forum
from apps_data.course.models import Lesson, Course


class Menu(models.Model):
    """
    Units (Lessons) are published in a class, when the instructor decides
    students are ready for them. Publication is decided on the level of the
    CourseUnit. See app course for details.
    """
    course = models.ForeignKey(Course)
    courseevent = models.ForeignKey(CourseEvent)
    lesson = models.ForeignKey(Lesson, blank=True, null=True)
    forum = models.ForeignKey(Forum, blank=True, null=True)

    item_type = models.StatusField
    item_nr = models.IntegerField()
    published = models.BooleanField()
    is_start_item =models.BooleanField()

    def __unicode__(self):
        return u'%s / %s' % (self.courseevent, self.unit)



class CourseeventUnitPublish(models.Model):
    """
    Units (Lessons) are published in a class, when the instructor decides
    students are ready for them. Publication is decided on the level of the
    CourseUnit. See app course for details.
    """
    courseevent = models.ForeignKey(CourseEvent)
    unit = models.ForeignKey(CourseUnit)
    published_at_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s / %s' % (self.courseevent, self.unit)

