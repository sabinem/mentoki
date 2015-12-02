# -*- coding: utf-8 -*-

"""
Views for internally viewing and editing courses. These views are only
accessible by teachers. Access is tested by CourseMenuMixin.
"""

from __future__ import unicode_literals

from django.forms.models import modelform_factory
from django.forms.widgets import TextInput
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from braces.views import FormValidMessageMixin

from froala_editor.widgets import FroalaEditor

from apps_data.course.models.course import Course
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin

from .constants import AlterCourseEvent

import logging
logger = logging.getLogger('activity.courseeventupdate')


class CourseDetailView(
    CourseMenuMixin,
    DetailView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    model = Course
    context_object_name ='course'
    slug_url_kwarg = 'course_slug'
    slug_field = 'slug'


class CourseUpdateView(
    CourseMenuMixin,
    FormValidMessageMixin,
    UpdateView):
    """
    Update the course one field at a time
    """
    model = Course
    slug_url_kwarg = 'course_slug'
    slug_field = 'slug'
    context_object_name ='course'
    form_valid_message="Die Kursvorlage wurde geändert!"

    def get_form_class(self, **kwargs):
        field_name = self.kwargs['field']
        if field_name == 'title':
            widget = TextInput
        else:
            widget = FroalaEditor
        return modelform_factory(Course, fields=(field_name,),
                                 widgets={ field_name: widget })


class CourseEventListView(
    CourseMenuMixin,
    TemplateView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    def get_context_data(self, **kwargs):
        context = super(CourseEventListView, self).get_context_data(**kwargs)

        context['courseevents'] = \
            CourseEvent.objects.\
                active_courseevents_for_course(course=context['course'])
        context['courseevents_hidden'] = \
            CourseEvent.objects.\
                hidden_courseevents_for_course(course=context['course'])
        context['AlterCourseEvent'] = AlterCourseEvent
        return context


def alter_courseevent(request, course_slug, pk, action):
    logger.info('-----------------------------------------')
    logger.info('Kursereignis wird geändert [%s], Aktionscode [%s]' % (pk, action))
    logger.info('-----------------------------------------')
    action_code = int(action)
    try:
        courseevent = CourseEvent.objects.get(
            pk=pk)
        logger.info('Kursereignis gefunden [%s]' % courseevent)
        if action_code == AlterCourseEvent.CLOSE:
            courseevent.close()
            logger.info('Klassenzimmer geschlossen')
            messages.success(request, 'Das Klassenzimmer wurde geschlossen')
        elif action_code == AlterCourseEvent.OPEN:
            courseevent.open()
            logger.info('Klassenzimmer geöffnet')
            messages.success(request, 'Das Klassenzimmer wurde geöffnet')
        elif action_code == AlterCourseEvent.HIDE:
            courseevent.hide()
            logger.info('Kursereignis versteckt')
            messages.success(request, 'Der Kurs wird versteckt')
        elif action_code == AlterCourseEvent.UNHIDE:
            courseevent.unhide()
            logger.info('Kursereignis sichtbar gemacht')
            messages.success(request, 'Der Kurs wird angezeigt')
        else:
            logger.info('keine Aktion ausgewählt')
            messages.error(request, "Keine Aktion ausgewählt")
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        messages.error(request, "Etwas ist falsch gelaufen.")
        logger.info('Kein Kursereignis gefunden')

    return HttpResponseRedirect(reverse('coursebackend:course:list',
                                        kwargs={'course_slug':course_slug,
                                                }))