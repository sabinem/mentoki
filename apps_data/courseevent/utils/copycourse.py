# coding: utf-8

"""
utility for courseevents:
utilities that handle data from courseevents
"""

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.course.models.course import Course

import logging
logger = logging.getLogger(__name__)

def copy_course_description(self, courseevent_pk):
    """
    this utility copies the description from a course to the courseevent
    when it finishes it call the courseevent detail page
    """
    courseevent = get_object_or_404(CourseEvent, pk=courseevent_pk)
    course = get_object_or_404(Course, pk=courseevent.course_id)

    courseevent = get_object_or_404(CourseEvent, pk=courseevent_pk)
    courseevent.target_group = course.target_group
    courseevent.excerpt = course.excerpt
    courseevent.text = course.text
    courseevent.prerequisites = course.prerequisites
    courseevent.project = course.project
    courseevent.save()

    logger.info("""[%s] [course %s %s]:
                Beschreibung aus der Kursvorlage in den Kurs kopiert"""
                % (courseevent, course.id, course))
    return(HttpResponseRedirect(courseevent.get_absolute_url()))

