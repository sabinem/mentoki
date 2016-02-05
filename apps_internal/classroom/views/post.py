# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.core.validators import ValidationError

import floppyforms.__future__ as forms
from froala_editor.widgets import FroalaEditor

from apps_data.courseevent.models.forum import Thread, \
    Forum
from apps_core.email.utils.post import send_post_notification
from apps_data.courseevent.models.courseevent import CourseEvent, \
    CourseEventParticipation
from apps_data.courseevent.models.forum import Post

from .mixins.base import ClassroomMenuMixin, AuthClassroomAccessMixin, \
    ParticipationFormKwargsMixin, ParticipationCheckHiddenFormMixin

class StudentPostForm(
    ParticipationCheckHiddenFormMixin,
    forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Post
        fields = ('title', 'text')


class PostCreateView(
    AuthClassroomAccessMixin,
    ParticipationFormKwargsMixin,
    ClassroomMenuMixin,
    FormView):
    """
    Lists a thread with posts underneath and provides a form to create a new post
    """
    form_class = StudentPostForm

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        thread = get_object_or_404(Thread, pk=self.kwargs['pk'])
        post = Post.objects.create_new_post(courseevent=courseevent, thread=thread,
                                     text=form.cleaned_data['text'],
                                     title=form.cleaned_data['title'],
                                     author=self.request.user)

        # make email to all people participating in the thread
        mail_distributor = send_post_notification(
                post=post,
                thread=thread,
                module=self.__module__,
                courseevent=courseevent
            )

        return HttpResponseRedirect(self.get_success_url())


    def get_context_data(self, **kwargs):

        context = super(PostCreateView, self).get_context_data(**kwargs)

        thread = get_object_or_404(Thread, pk=self.kwargs['pk'])
        forum = get_object_or_404(Forum, pk=thread.forum_id)

        context['thread'] = thread
        context['breadcrumbs'] = forum.get_published_breadcrumbs_with_self
        context['posts'] = Post.objects.filter(thread_id=self.kwargs['pk'])

        return context

    def get_success_url(self):
       return reverse_lazy('classroom:forum:thread',
                           kwargs={'slug': self.kwargs['slug'], 'pk': self.kwargs['pk']})