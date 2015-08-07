# -*- coding: utf-8 -*-

class TemplateMixin(object):

    def get_template_names(self):
       template =  self.kwargs['template']
       return [template]
