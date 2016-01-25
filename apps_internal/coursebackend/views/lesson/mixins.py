# coding: utf-8

"""
Mixins for Lessons
"""

from __future__ import unicode_literals, absolute_import

from django.http import HttpResponseRedirect

from ..mixins.base import CourseMenuMixin


class LessonSuccessUpdateUrlMixin(object):
    def form_valid(self, form):
        last_url = self.request.session['last_url']
        self.object = form.save()
        return HttpResponseRedirect(last_url)


class LessonContextMixin(CourseMenuMixin):
    """
    add breadcrumbs to context in case of update or delete operations
    """
    def get_context_data(self, **kwargs):
        context = super(LessonContextMixin, self).get_context_data(**kwargs)
        if 'object' in context:
            context['breadcrumbs'] = context['object'].get_breadcrumbs_with_self
        return context

