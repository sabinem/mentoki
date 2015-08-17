# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, TemplateView, UpdateView, DeleteView, FormView

from braces.views import FormValidMessageMixin

from apps_data.courseevent.models.announcement import Announcement
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin
from ..forms.announcement import AnnouncementForm


class AnnouncementListView(
    CourseMenuMixin,
    TemplateView):
    """
    lists all announcements
    """
    template_name = 'coursebackend/announcement/pages/list.html'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementListView, self).get_context_data(**kwargs)

        context ['announcements_unpublished'] = Announcement.objects.unpublished(courseevent = context['courseevent'])
        context ['announcements_published'] = Announcement.objects.published(courseevent = context['courseevent'])

        return context


class AnnouncementRedirectMixin(object):
    """
    redirects to the list page
    """
    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:announcement:list',
                           kwargs={'course_slug': self.kwargs['course_slug'], 'slug': self.kwargs['slug']})


class AnnouncementDetailView(
    CourseMenuMixin,
    DetailView):
    """
    Announcement Detail
    """
    model = Announcement
    context_object_name ='announcement'


class AnnouncementUpdateView(
    CourseMenuMixin,
    FormValidMessageMixin,
    AnnouncementRedirectMixin,
    UpdateView):
    """
    Announcement Update
    """
    model = Announcement
    form_class = AnnouncementForm
    context_object_name ='announcement'
    form_valid_message="Die Ankündigung wurde geändert!"


class AnnouncementDeleteView(
    CourseMenuMixin,
    FormValidMessageMixin,
    AnnouncementRedirectMixin,
    DeleteView):
    """
    Announcement Delete
    """
    model = Announcement
    context_object_name ='announcement'
    form_valid_message="Die Ankündigung wurde gelöscht!"


class AnnouncementCreateView(
    CourseMenuMixin,
    FormValidMessageMixin,
    AnnouncementRedirectMixin,
    FormView):
    """
    Announcement Create
    """
    model = Announcement
    form_class = AnnouncementForm
    context_object_name ='announcement'
    form_valid_message="Die Ankündigung wurde gespeichert!"

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        Announcement.objects.create(
            courseevent=courseevent,
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            published=form.cleaned_data['published'])

        return HttpResponseRedirect(self.get_success_url())



