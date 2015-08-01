# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect

from vanilla import TemplateView, DetailView, UpdateView, FormView, DeleteView

from apps_data.courseevent.models.announcement import Announcement
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin
from ..forms.announcement import AnnouncementForm


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



class AnnouncementMixin(CourseMenuMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('classroom:studentswork:list',
                           kwargs={'slug': self.kwargs['slug']})


class AnnouncementListView(CourseMenuMixin, TemplateView):
    """
    Work List
    """
    template_name = 'classroom/studentswork/pages/list.html'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementListView, self).get_context_data(**kwargs)

        context['studentworks'] = Announcement.objects.mywork(user=self.request.user,
                                                              courseevent=context['courseevent'])
        return context


class AnnouncementDetailView(CourseMenuMixin, DetailView):
    """
    Work Detail
    """
    template_name = 'classroom/studentswork/pages/detail.html'
    model = Announcement
    lookup_field = 'pk'
    context_object_name ='work'


class AnnouncementUpdateView(AnnouncementMixin, UpdateView):
    """
    Work Update
    """
    template_name = 'classroom/studentswork/pages/update.html'
    model = Announcement
    form_class = AnnouncementForm
    lookup_field = 'pk'
    context_object_name ='work'


class AnnouncementDeleteView(AnnouncementMixin, DeleteView):
    """
    Work Delete
    """
    template_name = 'classroom/studentswork/pages/delete.html'
    model = Announcement
    lookup_field = 'pk'
    context_object_name ='work'


class AnnouncementCreateView(AnnouncementMixin, FormView):
    """
    Work Create
    """
    template_name = 'classroom/studentswork/pages/create.html'
    model = Announcement
    lookup_field = 'pk'
    form_class = AnnouncementForm
    context_object_name ='work'

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        Announcement.objects.create_new_work(
            courseevent=courseevent,
            homework=form.cleaned_data['homework'],
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            user=self.request.user)

        return HttpResponseRedirect(self.get_success_url())



