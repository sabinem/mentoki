# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms.models import modelform_factory
from django.forms.widgets import NumberInput, DateInput,TextInput, Select, \
    CheckboxInput
from django.views.generic import DetailView, UpdateView, TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib import messages

from braces.views import FormValidMessageMixin

from froala_editor.widgets import FroalaEditor

from apps_data.courseevent.models.courseevent import CourseEvent, \
    CourseEventParticipation
from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.courseevent.models.announcement import Announcement
from apps_data.courseevent.models.forum import Forum
from apps_data.courseevent.models.menu import ClassroomMenuItem
from .constants import AlterCourseEvent


from .mixins.base import CourseMenuMixin


class CourseEventDetailView(
    CourseMenuMixin,
    DetailView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    model = CourseEvent
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    context_object_name ='courseevent'

    def get_context_data(self, **kwargs):
        context = super(CourseEventDetailView, self).\
            get_context_data(**kwargs)

        courseevent = context['courseevent']

        # lessons in the courseevent
        blocks_for_courseevent = ClassLesson.objects.\
            blocks_for_courseevent(courseevent=courseevent)
        context['blocks_for_courseevent'] = blocks_for_courseevent
        context['published_lessons'] = ClassroomMenuItem.objects.\
            lessons_published_in_class(courseevent=courseevent)
        context['published_forums'] = ClassroomMenuItem.objects.\
            forums_published_in_class(courseevent=courseevent)
        menuitems_for_courseevent = ClassroomMenuItem.objects.\
            all_for_courseevent(courseevent=courseevent)
        context['menuitems_for_courseevent'] = menuitems_for_courseevent

        context['menuitems_forum'] = \
            ClassroomMenuItem.objects.forum_ids_published_in_class(
                courseevent=courseevent
            )
        context['menuitems_lesson'] = \
            ClassroomMenuItem.objects.lesson_ids_published_in_class(
                courseevent=courseevent
            )
        context['menuitems_lessonstep'] = \
            ClassroomMenuItem.objects.homeworks_published_in_class(
                courseevent=courseevent
            )
        forums_for_courseevent = Forum.objects.\
            forums_for_courseevent(courseevent=courseevent)
        context['forums_for_courseevent'] = forums_for_courseevent


        announcements_for_courseevent = Announcement.objects.\
            published_in_class(courseevent=courseevent)
        context['announcements_for_courseevent'] = announcements_for_courseevent

        participants_for_courseevent = CourseEventParticipation.objects.\
            active(courseevent=courseevent)
        context['participants_for_courseevent'] = participants_for_courseevent

        return context


class CourseEventUpdateView(
    CourseMenuMixin,
    FormValidMessageMixin,
    UpdateView):
    """
    Update the course one field at a time
    """
    model = CourseEvent
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    context_object_name ='courseevent'
    form_valid_message="Das Kursereignis wurde geändert!"

    def get_form_class(self, **kwargs):
        field_name = self.kwargs['field']
        if field_name in ['max_participants', 'nr_weeks']:
            widget = NumberInput
        elif field_name in ['video_url', 'title', 'email_greeting']:
            widget = TextInput
        elif field_name in ['you_okay']:
            widget = CheckboxInput
        elif field_name == 'start_date':
            widget = DateInput
        elif field_name in ['status_internal', 'event_type']:
            widget = Select
        elif field_name in ['target_group',
                            'pricemodel',
                            'excerpt',
                            'text',
                            'format',
                            'workload',
                            'project',
                            'structure',
                            'project',
                            'prerequisites']:
            widget = FroalaEditor
        return modelform_factory(CourseEvent, fields=(field_name,),
                                 widgets={ field_name: widget })


class CopyCourseDescriptionView(
    CourseMenuMixin,
    TemplateView):
    """
    Update the course one field at a time
    """



