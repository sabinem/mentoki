from __future__ import unicode_literals
import re
# from python
import logging
from itertools import chain
from operator import attrgetter
# import from django
from django.views.generic import TemplateView
# from other apps
from apps.classroom.mixins import ClassroomMixin
from apps.forum.models import Thread, SubForum, Forum, Post
from apps.forum.cache import get_forum_structure, get_thread_data
from apps.forum.cache import get_subforum_change
from apps.forum.helpers_subforums import calc_subforum_enriched_list
import re


logger = logging.getLogger(__name__)


class ForumMixin(ClassroomMixin):

    def get_context_data(self, **kwargs):
        context = super(ForumMixin, self).get_context_data(**kwargs)
        logger.debug("---------- in ForumMixin get_context_data")

        #get forum id form context
        forum_id = context['courseevent']['forum_id']
        forum = Forum.objects.get(id=forum_id)
        context['forum'] = forum

        # now the cache is used or calculated if it is not there yet
        # what comes back is forumtree, path_lists and subforum_dict
        forumdata = get_forum_structure(forum_id)

        # get last modifications for all threads in the forum
        threaddata = get_thread_data(forum_id)

        # get last modifications for all subforums in the forum
        subforumchangedata = get_subforum_change(forum_id)

        context['threaddata'] = threaddata
        context['subforumchangedata'] = subforumchangedata
        context['subforumdict'] = forumdata['subforum_dict']
        context['forumtree'] = forumdata['forumtree']
        context['path_lists'] = forumdata['path_lists']
        return context


class ForumListView(ForumMixin, TemplateView):
    template_name = 'classroom/forum/forum.html'

    def get_context_data(self, **kwargs):
        context = super(ForumListView, self).get_context_data(**kwargs)
        logger.debug("---------- in ForumListView get_context_data")
        context['output_list'] = subforums_output_list(context, None)
        return context


class ForumRecentListView(ForumMixin, TemplateView):
    template_name = 'classroom/forum/forumrecent.html'

    def get_context_data(self, **kwargs):
        context = super(ForumRecentListView, self).get_context_data(**kwargs)
        logger.debug("---------- in ForumListView get_context_data")
        threads = Thread.objects.select_related('author').\
            filter(forum_id=context['courseevent']['forum_id']).\
            order_by('-modified')[0:50]
        posts = Post.objects.filter(forum_id=context['courseevent']['forum_id']).\
            select_related('thread','author').order_by('-modified')[0:50]
        result_list = sorted(
            chain(threads, posts),
            key=attrgetter('modified'))
        context['result_list']=result_list[::-1]
        return context


class SubForumListView(ForumMixin, TemplateView):
    template_name = 'classroom/forum/subforum.html'

    def get_context_data(self, **kwargs):
        context = super(SubForumListView, self).get_context_data(**kwargs)
        logger.debug("---------- in ForumListView get_context_data")
        # subforums data
        subforum = SubForum.objects.get(id=self.kwargs['subforum'])
        context['subforum'] = subforum

        context['subforum_threadcount'] = context['subforumchangedata'][subforum.id]['thread_count']

        context['output_list'] = subforums_output_list(context, subforum)

        # get ancestors
        ancestor_list = context['subforumdict'][subforum.id]['ancestors']
        context['ancestors'] = calc_subforum_enriched_list(ancestor_list, context['subforumdict'])

        # thread data
        print "here"
        threads = Thread.objects.filter(subforum_id=subforum.id).select_related('author')
        print threads
        threads_list = []
        for thread in threads:
            ancestor_list = context['subforumdict'][thread.subforum_id]['ancestors']
            ancestor_enriched_list = calc_subforum_enriched_list(ancestor_list, context['subforumdict'])
            print thread
            print ancestor_enriched_list
            output_dict = {
                'thread':thread,
                'last_author': context['threaddata'][thread.id]['last_author'],
                'last_author_id': context['threaddata'][thread.id]['last_author_id'],
                'last_changed': context['threaddata'][thread.id]['last_changed'],
                'author': thread.author,
                'postcount' : context['threaddata'][thread.id]['post_count'],
                'subforum_title': context['subforumdict'][thread.subforum_id]['title'],
                'ancestors': ancestor_enriched_list
            }
            print output_dict
            threads_list.append(output_dict)
        context['threads'] = threads_list
        print context['threads']
        return context


def subforums_output_list(context, subforum):

        output_list = []

        subforums = SubForum.objects.filter(forum=context['courseevent']['forum_id'],
                                                       parentforum=subforum).order_by('display_nr')
        for subforum in subforums:
            decendants_list = []
            real_decendants = context['subforumdict'][subforum.id]['decendants']
            real_decendants.remove(subforum.id)
            level_2_output_list = []
            for decendant_id in real_decendants:
                threadcount = context['subforumchangedata'][decendant_id]['thread_count']
                level_2_output_list.append({
                   'subforum_id':decendant_id,
                   'subforum_title':context['subforumdict'][decendant_id]['title'],
                   'subforum_threadcount': threadcount,
                })
            threadcount = context['subforumchangedata'][subforum.id]['thread_count']
            output_list.append({
                'subforum_id':subforum.id,
                'subforum_title':subforum.title,
                'subforum_description':subforum.text,
                'subforum_threadcount': threadcount,
                'level_2_output_list': level_2_output_list
            })
        return output_list


