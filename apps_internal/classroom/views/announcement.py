# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import TemplateView, DetailView

from apps_data.courseevent.models.announcement import Announcement

from .mixins.base import ClassroomMenuMixin


class AnnouncementListView(ClassroomMenuMixin, TemplateView):
    """
    AnnouncementList
    """
    def get_context_data(self, **kwargs):
        context = super(AnnouncementListView, self).get_context_data(**kwargs)

        context ['announcements'] = \
            Announcement.objects.classroom(courseevent = context['courseevent'])

        return context


class AnnouncementDetailView(ClassroomMenuMixin, DetailView):
    """
    Announcement Detail
    """
    model = Announcement
    context_object_name ='announcement'