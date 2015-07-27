# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from vanilla import TemplateView, DetailView

from apps_data.courseevent.models.homework import StudentsWork

from ..mixins.base import ClassroomMenuMixin


class StudentsWorkListView(ClassroomMenuMixin, TemplateView):
    """
    AnnouncementList
    """
    template_name = 'classroom/announcement/list.html'

    def get_context_data(self, **kwargs):
        context = super(StudentsWorkListView, self).get_context_data(**kwargs)
        print 'xxxxxxxxxxx------------------'
        print context['courseevent']

        context ['announcements'] = Announcement.objects.published(courseevent = context['courseevent'])
        print "===========ANOUNCEMNTS"
        print context ['announcements']
        return context


class StudentsWorkDetailView(ClassroomMenuMixin, TemplateView):
    """
    Announcement Detail
    """
    template_name = 'classroom/announcement/detail.html'
    model = StudentsWork
    lookup_field = 'pk'
    context_object_name ='announcement'