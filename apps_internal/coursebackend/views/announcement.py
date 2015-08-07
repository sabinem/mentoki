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


class AnnouncementChangeMixin(CourseMenuMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:announcement:list',
                           kwargs={'course_slug': self.kwargs['course_slug'], 'slug': self.kwargs['slug']})


class AnnouncementListView(CourseMenuMixin, TemplateView):
    """
    Announcements list
    """
    template_name = 'coursebackend/announcement/pages/list.html'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementListView, self).get_context_data(**kwargs)

        context ['announcements_unpublished'] = Announcement.objects.unpublished(courseevent = context['courseevent'])
        context ['announcements_published'] = Announcement.objects.published(courseevent = context['courseevent'])

        return context


class AnnouncementDetailView(CourseMenuMixin, DetailView):
    """
    Announcement Detail
    """
    model = Announcement
    lookup_field = 'pk'
    context_object_name ='announcement'


class AnnouncementUpdateView(AnnouncementChangeMixin, UpdateView):
    """
    Announcement Update
    """
    model = Announcement
    form_class = AnnouncementForm
    lookup_field = 'pk'
    context_object_name ='announcement'


class AnnouncementDeleteView(AnnouncementChangeMixin, DeleteView):
    """
    Announcement Delete
    """
    model = Announcement
    lookup_field = 'pk'
    context_object_name ='announcement'


class AnnouncementCreateView(AnnouncementChangeMixin, FormView):
    """
    Announcement Create
    """
    model = Announcement
    form_class = AnnouncementForm
    context_object_name ='announcement'

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        Announcement.objects.create(
            courseevent=courseevent,
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            published=form.cleaned_data['published'])

        return HttpResponseRedirect(self.get_success_url())



