# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from apps_data.courseevent.models.courseevent import CourseEventParticipation

from .mixins.base import CourseMenuMixin


class CourseParticipantListView(
    CourseMenuMixin,
    TemplateView):
    """
    Participants of the course are listed
    """
    def get_context_data(self, **kwargs):
        context = super(CourseParticipantListView, self).get_context_data(**kwargs)

        context['participants'] = CourseEventParticipation.objects.learners(
            courseevent=context['courseevent'])
        return context


def hide_participant(request, course_slug, slug, pk):
    messages.success(request, "Der Teilnehmerstatus wurde geändert.")
    participant = get_object_or_404(CourseEventParticipation, pk=pk)
    participant.hide()
    return HttpResponseRedirect(reverse('coursebackend:participant:list',
                                        kwargs={'course_slug':course_slug,
                                                'slug':slug,
                                                }))


def unhide_participant(request, course_slug, slug, pk):
    messages.success(request, "Der Teilnehmerstatus wurde geändert.")
    participant = get_object_or_404(CourseEventParticipation, pk=pk)
    participant.unhide()
    return HttpResponseRedirect(reverse('coursebackend:participant:list',
                                        kwargs={'course_slug':course_slug,
                                                'slug':slug,
                                               }))

