# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from django.views.generic import FormView

from apps_data.courseevent.models.forum import Thread, Forum
from apps_data.courseevent.models.courseevent import CourseEvent

from ..forms.thread import StudentThreadForm
from .mixins.base import ClassroomMenuMixin


class ThreadCreateView(ClassroomMenuMixin, FormView):
    """
    List all lesson blocks with lessons underneath
    """
    form_class = StudentThreadForm

    def get_context_data(self, **kwargs):
        context = super(ThreadCreateView, self).get_context_data(**kwargs)

        forum = get_object_or_404(Forum, pk=self.kwargs['pk'])

        context['forum'] = forum
        context['breadcrumbs'] = forum.get_ancestors()

        return context

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        forum = get_object_or_404(Forum, pk=self.kwargs['pk'])

        Thread.objects.create_new_thread(courseevent=courseevent, forum=forum,
                                     text=form.cleaned_data['text'],
                                     title=form.cleaned_data['title'],
                                     author=self.request.user)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
       return reverse_lazy('classroom:forum:detail',
                           kwargs={'slug': self.kwargs['slug'], 'pk': self.kwargs['pk']})