# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404

from apps.course.models import Material

from ..mixins import LessonsMenuMixin, CourseFormMixin, MaterialMixin
from ..forms import MaterialForm


class MaterialListView(LessonsMenuMixin, TemplateView):
    template_name = 'coursebackend/material/list.html'

    def get_context_data(self, **kwargs):
        context = super(MaterialListView, self).get_context_data(**kwargs)

        context['materials'] = Material.objects.filter(course=context['course'])
        return context


class MaterialDetailView(LessonsMenuMixin, CourseFormMixin, MaterialMixin, DetailView):
    template_name = 'coursebackend/material/detail.html'
    model = Material


class MaterialUpdateView(LessonsMenuMixin, CourseFormMixin, MaterialMixin, UpdateView):
    template_name = 'coursebackend/material/update.html'
    form_class = MaterialForm


class MaterialCreateView(LessonsMenuMixin, CourseFormMixin, MaterialMixin, CreateView):
    template_name = 'coursebackend/material/create.html'
    form_class = MaterialForm


class MaterialDeleteView(LessonsMenuMixin, MaterialMixin, DeleteView):
    model=Material
    template_name = 'coursebackend/material/delete.html'
