# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404

from apps_data.courseevent.models.forum import Forum, Thread, Post

from .base import ClassroomMenuMixin


class ForumMixin(ClassroomMenuMixin):

    def get_context_data(self, **kwargs):
        context = super(ForumMixin, self).get_context_data(**kwargs)

        if 'pk' in self.kwargs:
            start_forum = get_object_or_404(Forum, pk=self.kwargs['pk'])

            context['start_forum'] = start_forum

            context['breadcrumbs'] = start_forum.get_ancestors()

            context['nodes'] = start_forum.get_descendants()

            if start_forum.can_have_threads:

                context['threads'] = Thread.objects.filter(forum=start_forum)

        else:

            context['nodes'] = \
                Forum.objects.forums_published_in_courseevent(courseevent=context['courseevent'])
            print "*********************"
            print context['nodes']
            print "********************"

        return context


class ThreadMixin(ClassroomMenuMixin):

    def get_context_data(self, **kwargs):
        context = super(ThreadMixin, self).get_context_data(**kwargs)

        thread = get_object_or_404(Thread, pk=self.kwargs['pk'])
        print thread

        context['thread'] = thread

        start_forum = get_object_or_404(Forum, pk=thread.forum_id)

        print start_forum

        context['breadcrumbs'] = start_forum.get_ancestors(include_self=True)

        context['posts'] = Post.objects.filter(thread_id=self.kwargs['pk'])

        print "========================in thread======="
        print context['thread']
        print context['breadcrumbs']
        print context['posts']

        return context