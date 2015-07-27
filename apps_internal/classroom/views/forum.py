# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy

from vanilla import TemplateView, CreateView

from .mixins.forum import ForumMixin, ThreadMixin

from apps_data.courseevent.models.forum import Post


class ForumStartView(ForumMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    template_name = 'classroom/forum/start.html'


class ForumDetailView(ForumMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    template_name = 'classroom/forum/forum.html'


class ForumNewPostsView(ForumMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    template_name = 'classroom/forum/newposts.html'


class ForumThreadView(ThreadMixin, CreateView):
    """
    List all lesson blocks with lessons underneath
    """
    template_name = 'classroom/forum/thread.html'
    model = Post
    context_object_name = 'post'
    fields = ['text']

    def get_success_url(self):
       return reverse_lazy('classroom:forum:thread',
                           kwargs={'slug': self.kwargs['slug'], 'pk': self.kwargs['pk']})