# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from vanilla import TemplateView

from apps_data.courseevent.models.announcement import Announcement

from ..mixins.base import CourseMenuMixin


class AnnouncementListView(CourseMenuMixin, TemplateView):
    """
    Owners of the course are listed
    """
    template_name = 'coursebackend/announcement/list.html'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementListView, self).get_context_data(**kwargs)

        context ['announcements_unpublished'] = Announcement.objects.unpublished(courseevent = context['courseevent'])
        context ['announcements_published'] = Announcement.objects.published(courseevent = context['courseevent'])

        return context

