# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms.models import modelform_factory

from vanilla import TemplateView

from apps_data.course.models import Course

from ..mixins.base import ClassroomMenuMixin


class ClassroomStartView(ClassroomMenuMixin, TemplateView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    model = Course
    template_name = 'classroom/start/start.html'


