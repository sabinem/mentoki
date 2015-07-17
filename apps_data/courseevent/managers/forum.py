# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models.query import QuerySet


class ThreadQuerySet(QuerySet):

    def threads_for_courseevent(self, courseevent):
        return self.filter(forumcourseevent=courseevent)


class PostQuerySet(QuerySet):

    def posts_for_thread(self, thread):
        return self.filter(thread=thread).order_by('created')

    def posts_all(self, courseevent):
        return self.filter(courseevent=courseevent).select_related('all')
