# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

class TemplateMixin(object):
    """
    Provides the template name form the url files instead of taking it from the view.
    This overwrites a method for django.views.generic.
    """
    def get_template_names(self):
       template =  self.kwargs['template']
       return [template]
