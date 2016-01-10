# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import FormView, UpdateView, DeleteView

from apps_data.courseevent.models.forum import Thread, Forum
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_core.email.utils.thread import send_thread_notification,\
    send_thread_delete_notification

from ..forms.thread import StudentThreadForm
from .mixins.base import ClassroomMenuMixin


class ThreadCreateView(
    ClassroomMenuMixin,
    FormView):
    """
    provides a form to create a thread
    """
    form_class = StudentThreadForm

    def get_context_data(self, **kwargs):
        context = super(ThreadCreateView, self).get_context_data(**kwargs)

        forum = get_object_or_404(Forum, pk=self.kwargs['pk'])

        context['forum'] = forum
        context['breadcrumbs'] = forum.get_published_breadcrumbs_with_self

        return context

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        forum = get_object_or_404(Forum, pk=self.kwargs['pk'])

        thread = Thread.objects.create_new_thread(courseevent=courseevent, forum=forum,
                                     text=form.cleaned_data['text'],
                                     title=form.cleaned_data['title'],
                                     author=self.request.user)

        # make email to all people participating in the thread
        mail_distributor = send_thread_notification(
                author = thread.author,
                thread=thread,
                forum=thread.forum,
                module=self.__module__,
                courseevent=thread.courseevent
            )


        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
       return reverse_lazy('classroom:forum:detail',
                           kwargs={'slug': self.kwargs['slug'], 'pk': self.kwargs['pk']})


class ThreadUpdateView(
    ClassroomMenuMixin,
    UpdateView):
    """
    provides a form to create a thread
    """
    form_class = StudentThreadForm
    model = Thread

    def get_context_data(self, **kwargs):
        context = super(ThreadUpdateView, self).get_context_data(**kwargs)

        forum = get_object_or_404(Forum, pk=context['thread'].forum_id)

        context['forum'] = forum
        context['breadcrumbs'] = forum.get_published_breadcrumbs_with_self

        return context

    def get_success_url(self):
       return reverse_lazy('classroom:forum:detail',
                           kwargs={'slug': self.kwargs['slug'], 'pk': self.object.forum_id})


class ThreadDeleteView(
    ClassroomMenuMixin,
    DeleteView):
    """
    provides a form to create a thread
    """
    form_class = StudentThreadForm
    model = Thread

    def get_context_data(self, **kwargs):
        context = super(ThreadDeleteView, self).get_context_data(**kwargs)

        forum = get_object_or_404(Forum, pk=context['thread'].forum_id)

        context['forum'] = forum
        context['breadcrumbs'] = forum.get_published_breadcrumbs_with_self

        return context

    def get_success_url(self):
        thread = self.object

        # make email to all people participating in the thread
        mail_distributor = send_thread_delete_notification(
                author = thread.author,
                thread=thread,
                forum=thread.forum,
                module=self.__module__,
                courseevent=thread.courseevent)

        return reverse_lazy('classroom:forum:detail',
                           kwargs={'slug': self.kwargs['slug'], 'pk': thread.forum_id})

