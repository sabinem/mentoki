# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, TemplateView, UpdateView, DeleteView, FormView

from braces.views import FormValidMessageMixin, MessageMixin

from mailqueue.models import MailerMessage

from apps_data.courseevent.models.announcement import Announcement
from apps_core.email.utils.announcements import send_announcement
from apps_data.courseevent.models.courseevent import CourseEvent, CourseEventParticipation
from apps_data.course.models.course import CourseOwner

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

        context ['announcements_unpublished'] = \
            Announcement.objects.unpublished(courseevent = context['courseevent'])
        context ['announcements_published'] = \
            Announcement.objects.published(courseevent = context['courseevent'])
        context ['announcements_archived'] = \
            Announcement.objects.archived(courseevent = context['courseevent'])

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


class AnnouncementMailContextMixin(CourseMenuMixin):
    def get_context_data(self, **kwargs):
        context = super(AnnouncementMailContextMixin, self).get_context_data(**kwargs)
        context['participants_emails'] = \
            CourseEventParticipation.objects.learners_emails(courseevent=context['courseevent'])
        context['teachers_emails'] = \
            CourseOwner.objects.teachers_emails(course=context['course'])
        return context


class AnnouncementUpdateView(
    AnnouncementMailContextMixin,
    MessageMixin,
    AnnouncementRedirectDetailMixin,
    UpdateView):
    """
    Announcement Update
    """
    model = Announcement
    form_class = AnnouncementUpdateForm
    context_object_name ='announcement'

    def form_valid(self, form):
        if form.cleaned_data['published']:
            form.instance.mail_distributor = send_announcement(
                announcement=form.instance,
                module=self.__module__,
                courseevent=form.instance.courseevent
            )
            self.messages.success(u'Die Ank\u00fcndigung wurde verschickt.')
        else:
            self.messages.success(u'Der Entwurf wurde gespeichert.')

        return super(AnnouncementUpdateView, self).form_valid(form)


class AnnouncementCreateView(
    AnnouncementMailContextMixin,
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
        if not hasattr(self, 'courseevent'):
            self.courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])

        announcement = Announcement.objects.create(
            courseevent=self.courseevent,
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title']
        )
        self.object = announcement

        if form.cleaned_data['published']:
            mail_distributor = send_announcement(
                announcement=announcement,
                module=self.__module__,
                courseevent=self.courseevent,
            )
            self.messages.success(u'Die Ank\u00fcndigung wurde verschickt.')
        else:
            self.messages.success(u'Der Entwurf wurde gespeichert.')

        return super(AnnouncementCreateView, self).form_valid(form)


def archive_announcement(request, course_slug, slug, pk):
    messages.success(request, "Die Ankündigung wurde archiviert.")
    announcement = get_object_or_404(Announcement, pk=pk)
    announcement.archive()
    return HttpResponseRedirect(reverse('coursebackend:announcement:list',
                                        kwargs={'course_slug':course_slug,
                                                'slug':slug,
                                                }))


def unarchive_announcement(request, course_slug, slug, pk):
    messages.success(request, "Die Ankündigung wurde wieder sichtbar gemacht.")
    announcement = get_object_or_404(Announcement, pk=pk)
    announcement.unarchive()
    return HttpResponseRedirect(reverse('coursebackend:announcement:list',
                                        kwargs={'course_slug':course_slug,
                                                'slug':slug,
                                               }))