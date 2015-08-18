# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import FormView

from apps_data.courseevent.models.forum import Post, CourseEvent, Thread, Forum
from apps_data.courseevent.models.courseevent import CourseEvent

from ..forms.post import StudentPostForm
from .mixins.base import ClassroomMenuMixin


class PostCreateView(
    ClassroomMenuMixin,
    FormView):
    """
    Lists a thread with posts underneath and provides a form to create a new post
    """
    form_class = StudentPostForm

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        thread = get_object_or_404(Thread, pk=self.kwargs['pk'])
        Post.objects.create_new_post(courseevent=courseevent, thread=thread,
                                     text=form.cleaned_data['text'],
                                     title=form.cleaned_data['title'],
                                     author=self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):

        context = super(PostCreateView, self).get_context_data(**kwargs)

        thread = get_object_or_404(Thread, pk=self.kwargs['pk'])
        forum = get_object_or_404(Forum, pk=thread.forum_id)

        context['thread'] = thread
        context['breadcrumbs'] = forum.get_ancestors(include_self=True)
        context['posts'] = Post.objects.filter(thread_id=self.kwargs['pk'])

        return context

    def get_success_url(self):
       return reverse_lazy('classroom:forum:thread',
                           kwargs={'slug': self.kwargs['slug'], 'pk': self.kwargs['pk']})