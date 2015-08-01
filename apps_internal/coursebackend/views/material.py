# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404

from apps_data.course.models.material import Material

from .mixins.base import CourseMenuMixin
from .mixins.lesson import CourseFormMixin
from .mixins.material import MaterialMixin
from ..forms.material import MaterialForm


class MaterialListView(CourseMenuMixin, TemplateView):
    template_name = 'coursebackend/material/list.html'

    def get_context_data(self, **kwargs):
        context = super(MaterialListView, self).get_context_data(**kwargs)

        context['materials'] = Material.objects.filter(course=context['course'])
        return context


class MaterialDetailView(CourseFormMixin, MaterialMixin, DetailView):
    template_name = 'coursebackend/material/detail.html'
    model = Material


class MaterialUpdateView(CourseFormMixin, MaterialMixin, UpdateView):
    template_name = 'coursebackend/material/update.html'
    form_class = MaterialForm


class MaterialCreateView(CourseFormMixin, MaterialMixin, CreateView):
    template_name = 'coursebackend/material/create.html'
    form_class = MaterialForm


class MaterialDeleteView(MaterialMixin, DeleteView):
    model=Material
    template_name = 'coursebackend/material/delete.html'
