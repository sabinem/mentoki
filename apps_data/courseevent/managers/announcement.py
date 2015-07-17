# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models.query import QuerySet


class AnnouncementQuerySet(QuerySet):

    def list_published(self, courseevent):
        return self.filter(courseevent=courseevent, published=True).order_by('published_at_date')

    def list_all(self, courseevent):
        return self.filter(courseevent=courseevent).order_by('published_at_date', 'created')
