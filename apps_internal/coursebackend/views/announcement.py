# -*- coding: utf-8 -*-

"""
These views handle the writing and publishing of announcements by the teachers.
The lifecycle of an announcement is as follows:
1. It may start as a draft.
As draft a teacher may still delete or update it.

2. At publication an email notification is send to all participants in the
courseevent. After publication it will be visible in the classromm and no
further changes are allowed.

3. It may get archived, when the teacher, does not want to show it any longer
in the classroom.

Logging: database transactions are logged.

TODO:
1. write tests
2. eventually restructure: create and update could share a form_valid mixin
"""

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, TemplateView, UpdateView, \
    DeleteView, FormView

from braces.views import FormValidMessageMixin, MessageMixin

from apps_data.courseevent.models.announcement import Announcement
from apps_core.email.utils.announcements import send_announcement
from apps_data.courseevent.models.courseevent import CourseEvent, \
    CourseEventParticipation
from apps_data.course.models.course import CourseOwner

from .mixins.base import CourseMenuMixin
from ..forms.announcement import AnnouncementUpdateForm

import logging
logger = logging.getLogger(__name__)


class AnnouncementListView(
    CourseMenuMixin,
    TemplateView):
    """
    lists all announcements: drafts, published announcements and archived ones
    the three states of annnouncements are collected in seperate lists.
    """
    template_name = 'coursebackend/announcement/pages/list.html'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementListView, self).get_context_data(**kwargs)

        context ['announcements_unpublished'] = \
            Announcement.objects.drafts_in_backend(
                courseevent = context['courseevent'])

        context ['announcements_published'] = \
            Announcement.objects.published_in_class(
                courseevent = context['courseevent'])

        context ['announcements_archived'] = \
            Announcement.objects.archived_announcements(
                courseevent = context['courseevent'])
        self.request.session['last_courseeventbackend_url'] = self.request.path

        return context


class AnnouncementRedirectListMixin(object):
    """
    redirects to the list view
    """
    def get_success_url(self):
       return reverse_lazy('coursebackend:announcement:list',
                           kwargs={'course_slug': self.kwargs['course_slug'],
                                   'slug': self.kwargs['slug']})


class AnnouncementRedirectDetailMixin(object):
    """
    redirects to the detail view
    """
    def get_success_url(self):
       return reverse_lazy('coursebackend:announcement:detail',
                           kwargs={'pk': self.object.pk,
                                   'course_slug': self.kwargs['course_slug'],
                                   'slug': self.kwargs['slug']})


class AnnouncementDetailView(
    CourseMenuMixin,
    DetailView):
    """
    shows one announcement in Detail
    """
    model = Announcement
    context_object_name ='announcement'


class AnnouncementDeleteView(
    CourseMenuMixin,
    FormValidMessageMixin,
    AnnouncementRedirectListMixin,
    DeleteView):
    """
    deletes an announcement
    """
    model = Announcement
    context_object_name ='announcement'
    form_valid_message="Die Ankündigung wurde gelöscht!"


class AnnouncementMailContextMixin(CourseMenuMixin):
    """
    provides the emails that the announcement should be sent to: these
    are the mentors and the teachers
    """
    def get_context_data(self, **kwargs):
        context = \
            super(AnnouncementMailContextMixin, self).\
                get_context_data(**kwargs)

        context['participants_emails'] = \
            CourseEventParticipation.objects.learners_emails(
                courseevent=context['courseevent'])

        context['teachers_emails'] = \
            CourseOwner.objects.teachers_emails(
                course=context['course'])

        return context

    def form_valid(self, form):
        """
        when the announcement is published it will be send
        as email to the mentors and the class.
        """
        if form.cleaned_data['published']:
            mail_distributor = send_announcement(
                announcement=self.object,
                module=self.__module__,
                courseevent=self.object.courseevent
            )
            self.messages.success(u'Die Ank\u00fcndigung wurde verschickt.')
            logger.info("[%s] [Ankündigung %s %s]: Email gesendet an %s" % (
                self.object.courseevent,
                self.object.id,
                self.object.title,
                mail_distributor))
        else:
            self.messages.success(u'Der Entwurf wurde gespeichert.')
            logger.info("[%s] [Ankündigung %s %s]: gespeichert" % (
                self.object.courseevent,
                self.object.id,
                self.object.title,
                ))
        return super(AnnouncementMailContextMixin, self).form_valid(form)


class AnnouncementUpdateView(
    AnnouncementMailContextMixin,
    MessageMixin,
    AnnouncementRedirectDetailMixin,
    UpdateView):
    """
    updates an announcement and mails it when it gets published
    """
    model = Announcement
    form_class = AnnouncementUpdateForm
    context_object_name ='announcement'


class AnnouncementCreateView(
    AnnouncementMailContextMixin,
    MessageMixin,
    AnnouncementRedirectDetailMixin,
    FormView):
    """
    creates an announcement
    """
    model = Announcement
    form_class = AnnouncementUpdateForm
    context_object_name ='announcement'

    def form_valid(self, form):
        """
        the announcement may be published immediately. In that case it is
        mailed out
        """
        if not hasattr(self, 'courseevent'):
            self.courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        self.object = Announcement.objects.create(
            courseevent=self.courseevent,
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title']
        )
        logger.info("[%s] [Ankündigung %s %s]: neu angelegt" % (
            self.courseevent,
            self.object.id,
            self.object.title))
        return super(AnnouncementCreateView, self).form_valid(form)


def archive_announcement(request, course_slug, slug, pk):
    """
    announcements can be archived, which means they are no longer visible in
    the classroom.
    """
    messages.success(request, "Die Ankündigung wurde archiviert.")
    announcement = get_object_or_404(Announcement, pk=pk)
    announcement.archive_announcement()
    logger.info("[Ankündigung %s %s]: archiviert: %s" % (
        announcement.courseevent,
        announcement.id,
        announcement.title))
    return HttpResponseRedirect(reverse('coursebackend:announcement:list',
                                        kwargs={'course_slug':course_slug,
                                                'slug':slug,
                                                }))


def unarchive_announcement(request, course_slug, slug, pk):
    """
    announcements can be pulled back from archivation, which means
    they will again be visible in the classroom.
    """
    messages.success(request, "Die Ankündigung wurde wieder sichtbar gemacht.")
    announcement = get_object_or_404(Announcement, pk=pk)
    announcement.unarchive_announcement()
    logger.info("[Ankündigung %s %s]: unarchiviert: %s" % (
        announcement.courseevent,
        announcement.id,
        announcement.title))
    return HttpResponseRedirect(reverse('coursebackend:announcement:list',
                                        kwargs={'course_slug':course_slug,
                                                'slug':slug,
                                               }))