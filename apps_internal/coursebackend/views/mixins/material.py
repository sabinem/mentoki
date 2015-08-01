# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from apps_data.course.models.material import Material

from ..mixins.base import CourseMenuMixin


class MaterialMixin(CourseMenuMixin):

    def get_success_url(self):
        return reverse('coursebackend:material:list', kwargs={"course_slug": self.kwargs['course_slug'],})

    def get_object(self, **kwargs):
        return get_object_or_404(Material, pk=self.kwargs['pk'])
