# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, UpdateView, DeleteView, FormView

from braces.views import FormValidMessageMixin

from apps_data.courseevent.models.forum import Forum
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

        context['nodes'] = Forum.objects.forums_for_courseevent(courseevent=context['courseevent'])
        print context['nodes']

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
        context['breadcrumbs'] = forum.get_ancestors()
        context['nodes'] = forum.get_descendants()

        return context


class ForumRedirectMixin(object):
    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:forum:list',
                           kwargs={'slug': self.kwargs['slug'],
                                   'course_slug':self.kwargs['course_slug']})


class ForumUpdateView(
    ForumRedirectMixin,
    FormValidMessageMixin,
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
    ForumRedirectMixin,
    FormValidMessageMixin,
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
    ForumRedirectMixin,
    FormCourseEventKwargsMixin,
    FormValidMessageMixin,
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
        forum = Forum.objects.create(
            courseevent=courseevent,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            can_have_threads=form.cleaned_data['can_have_threads'],
            parent=form.cleaned_data['parent'],
            display_nr=form.cleaned_data['display_nr']
        )
        return super(ForumCreateView, self).form_valid(form)