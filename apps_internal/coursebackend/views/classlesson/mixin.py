# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

import logging
logger = logging.getLogger(__name__)


class ClassLessonBreadcrumbMixin(object):
    """
    get breadcrumbs for object
    """
    def get_context_data(self, **kwargs):
        context = super(ClassLessonBreadcrumbMixin, self).get_context_data(
            **kwargs)
        if 'object' in context:
            context['breadcrumbs'] = context[
                'object'].get_breadcrumbs_with_self
        return context


class ClassLessonSuccessUpdateUrlMixin(object):
    def form_valid(self, form):
        last_url = self.request.session['last_url']
        self.object = form.save()
        return HttpResponseRedirect(last_url)