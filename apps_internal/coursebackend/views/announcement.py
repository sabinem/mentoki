# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, TemplateView, UpdateView, DeleteView, FormView

from braces.views import FormValidMessageMixin, MessageMixin

from apps_data.courseevent.models.announcement import Announcement, send_announcement
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin
from ..forms.announcement import AnnouncementUpdateForm, AnnouncementCreateForm


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


class AnnouncementRedirectListMixin(object):
    def get_success_url(self):
       return reverse_lazy('coursebackend:announcement:list',
                           kwargs={'course_slug': self.kwargs['course_slug'], 'slug': self.kwargs['slug']})


class AnnouncementRedirectDetailMixin(object):
    def get_success_url(self):
       return reverse_lazy('coursebackend:announcement:detail',
                           kwargs={'pk': self.object.pk,
                                   'course_slug': self.kwargs['course_slug'],
                                   'slug': self.kwargs['slug']})


class AnnouncementDetailView(
    CourseMenuMixin,
    DetailView):
    """
    Announcement Detail
    """
    model = Announcement
    context_object_name ='announcement'


class AnnouncementDeleteView(
    CourseMenuMixin,
    FormValidMessageMixin,
    AnnouncementRedirectListMixin,
    DeleteView):
    """
    Announcement Delete
    """
    model = Announcement
    context_object_name ='announcement'
    form_valid_message="Die Ankündigung wurde gelöscht!"


class AnnouncementUpdateView(
    CourseMenuMixin,
    MessageMixin,
    AnnouncementRedirectDetailMixin,
    UpdateView):
    """
    Announcement Update
    """
    model = Announcement
    form_class = AnnouncementUpdateForm
    context_object_name ='announcement'
    form_valid_message="Die Ankündigung wurde geändert!"

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        if form.cleaned_data['published']:
            message = send_announcement(
                announcement=form.instance,
                module=self.__module__,
                courseevent=courseevent,
            )
            self.messages.success(message)
        else:
            self.messages.success('Die Ankündigung wurde gespeichert.')

        return super(AnnouncementUpdateView, self).form_valid(form)


class AnnouncementCreateView(
    CourseMenuMixin,
    MessageMixin,
    AnnouncementRedirectDetailMixin,
    FormView):
    """
    Announcement Create
    """
    model = Announcement
    form_class = AnnouncementCreateForm
    context_object_name ='announcement'

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        self.object = Announcement.objects.create(
            courseevent=courseevent,
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            published=form.cleaned_data['published'])
        if form.cleaned_data['published']:
            message = send_announcement(
                announcement=self.object,
                module=self.__module__,
                courseevent=courseevent,
            )
            self.messages.success(message)
        else:
            self.messages.success('Die Ankündigung wurde gespeichert.')

        return HttpResponseRedirect(self.get_success_url())

