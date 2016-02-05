# -*- coding: utf-8 -*-

"""
These views show announcements in the classroom. Announcements are
the way a teachers adresses his students. They are listed by date.
They are written published in the backend of the course.

Logging: no logging required since nothing is written to the database here.
"""

from __future__ import unicode_literals

from django.views.generic import TemplateView, DetailView

from apps_data.courseevent.models.announcement import Announcement

from .mixins.base import ClassroomMenuMixin, AuthClassroomAccessMixin


class AnnouncementListView(
    AuthClassroomAccessMixin,
    ClassroomMenuMixin,
    TemplateView):
    """
    Announcements are listed in the classroom:
    announcements are chosen for a courseevent and only if they are published,
    but not archived.
    """
    def get_context_data(self, **kwargs):
        context = super(AnnouncementListView, self).get_context_data(**kwargs)

        context ['announcements'] = \
            Announcement.objects.published_in_class(courseevent =
                                                    context['courseevent'])

        return context


class AnnouncementDetailView(
    AuthClassroomAccessMixin,
    ClassroomMenuMixin,
    DetailView):
    """
    This shows a published not archived announcement in the
    classroom in detail.
    """
    model = Announcement
    context_object_name ='announcement'