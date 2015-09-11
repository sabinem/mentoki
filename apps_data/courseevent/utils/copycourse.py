# coding: utf-8

from __future__ import unicode_literals, absolute_import

import datetime

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.core.validators import ValidationError
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.course.models.course import Course


def copy_course_description(self, courseevent_pk):
    """
    copies the description of the course to the courseevent
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

    return(HttpResponseRedirect(reverse('coursebackend:courseevent:detail',
                               kwargs={'course_slug': courseevent.course.slug, 'slug': courseevent.slug})))

