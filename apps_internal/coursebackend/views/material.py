# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy

from vanilla import FormView, UpdateView, DetailView, TemplateView, DeleteView

from apps_data.course.models.material import Material

from .mixins.base import CourseMenuMixin
from .mixins.lesson import CourseFormMixin
from .mixins.material import MaterialMixin
from ..forms.material import MaterialForm


class MaterialMixin(CourseMenuMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:material:list',
                           kwargs={'course_slug': self.kwargs['course_slug']})

class MaterialListView(CourseMenuMixin, TemplateView):

    def get_context_data(self, **kwargs):
        context = super(MaterialListView, self).get_context_data(**kwargs)

        context['materials'] = Material.objects.materials_for_course(course=context['course'])
        return context


class MaterialDetailView(CourseFormMixin, MaterialMixin, DetailView):
    model = Material
    lookup_field = 'pk'
    context_object_name ='material'


class MaterialUpdateView(MaterialMixin, UpdateView):
    form_class = MaterialForm
    model = Material
    lookup_field = 'pk'
    context_object_name ='material'


class MaterialDeleteView(MaterialMixin, DeleteView):
    model=Material
    model = Material
    lookup_field = 'pk'
    context_object_name ='material'


class MaterialCreateView(MaterialMixin, FormView):
    form_class = MaterialForm
    model = Material
    lookup_field = 'pk'
    context_object_name ='material'