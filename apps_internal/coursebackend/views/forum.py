# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, UpdateView, DeleteView, FormView

from braces.views import FormValidMessageMixin

from apps_data.courseevent.models.forum import Forum, Thread, Post
from apps_data.courseevent.models.courseevent import CourseEvent

from ..forms.forum import ForumForm
from .mixins.base import CourseMenuMixin, FormCourseEventKwargsMixin


class ForumListView(
    CourseMenuMixin,
    TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(ForumListView, self).get_context_data(**kwargs)

        context['nodes'] = Forum.objects.forums_for_courseevent_without_root(
            courseevent=context['courseevent'])

        return context


class ForumDetailView(
    CourseMenuMixin,
    TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(ForumDetailView, self).get_context_data(**kwargs)

        forum = get_object_or_404(Forum, pk=self.kwargs['pk'])

        context['forum'] = forum
        context['breadcrumbs'] = forum.get_breadcrumbs_with_self
        context['nodes'] = forum.get_descendants()
        if forum.can_have_threads:
            context['threads'] = Thread.objects.filter(forum=forum)

        return context


class ForumContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ForumContextMixin, self).get_context_data(**kwargs)

        if not 'forum' in context:
            forum = get_object_or_404(Forum, pk=self.kwargs['pk'])

        context['breadcrumbs'] = context['forum'].get_breadcrumbs_with_self
        return context


class ForumRedirectListMixin(object):
    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:forum:list',
                           kwargs={'slug': self.kwargs['slug'],
                                   'course_slug':self.kwargs['course_slug']})


class ForumRedirectDetailMixin(object):
    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:forum:list',
                           kwargs={'slug': self.kwargs['slug'],
                                   'course_slug':self.kwargs['course_slug']})


class ForumUpdateView(
    ForumContextMixin,
    FormValidMessageMixin,
    ForumRedirectListMixin,
    FormCourseEventKwargsMixin,
    CourseMenuMixin,
    UpdateView):
    """
    Forum Update
    """
    form_class = ForumForm
    model = Forum
    context_object_name ='forum'
    form_valid_message = "Das Forum wurde geändert!"


class ForumDeleteView(
    ForumContextMixin,
    FormValidMessageMixin,
    ForumRedirectListMixin,
    CourseMenuMixin,
    DeleteView):
    """
    Forum Delete
    """
    model = Forum
    context_object_name ='forum'
    form_valid_message = "Das Forum wurde gelöscht!"

    def get_context_data(self, **kwargs):
        context = super(ForumDeleteView, self).get_context_data(**kwargs)
        context['nodes'] = context['object'].get_descendants(include_self=True)
        return context


class ForumCreateView(
    FormCourseEventKwargsMixin,
    FormValidMessageMixin,
    ForumRedirectListMixin,
    CourseMenuMixin,
    FormView):
    """
    Forum Create
    """
    model = Forum
    form_class = ForumForm
    form_valid_message = "Das Forum wurde angelegt!"

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['course_slug'])
        self.object = Forum.objects.create(
            courseevent=courseevent,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            can_have_threads=form.cleaned_data['can_have_threads'],
            parent=form.cleaned_data['parent'],
            display_nr=form.cleaned_data['display_nr']
        )
        return super(ForumCreateView, self).form_valid(form)


class ThreadDetailView(
    CourseMenuMixin,
    TemplateView):
    """
    Lists a thread with posts underneath and provides a form to create a new post
    """
    def get_context_data(self, **kwargs):

        context = super(ThreadDetailView, self).get_context_data(**kwargs)

        thread = get_object_or_404(Thread, pk=self.kwargs['pk'])
        forum = get_object_or_404(Forum, pk=thread.forum_id)

        context['thread'] = thread
        context['breadcrumbs'] = forum.get_breadcrumbs_with_self
        context['posts'] = Post.objects.filter(thread_id=self.kwargs['pk'])

        return context

