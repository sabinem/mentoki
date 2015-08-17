# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, UpdateView, TemplateView, FormView, DeleteView

from braces.views import FormValidMessageMixin

from apps_data.material.models.material import Material
from apps_data.courseevent.models.courseevent import Course

from .mixins.base import CourseMenuMixin
from ..forms.material import MaterialForm


class CourseFormMixin(CourseMenuMixin):

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        kwargs = super(CourseFormMixin, self).get_form_kwargs()
        kwargs['course_slug'] = course_slug
        return kwargs

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        form.instance.course = context['course']
        return super(CourseFormMixin, self).form_valid(form)


class MaterialRedirectMixin(object):
    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:material:list',
                           kwargs={'course_slug': self.kwargs['course_slug']})


class MaterialListView(
    CourseMenuMixin,
    TemplateView):
    """
    list materials
    """
    def get_context_data(self, **kwargs):
        context = super(MaterialListView, self).get_context_data(**kwargs)

        context['materials'] = Material.objects.materials_for_course(course=context['course'])
        return context


class MaterialDetailView(
    CourseMenuMixin,
    DetailView):
    """
    Material Detail
    """
    model = Material
    context_object_name ='material'


class MaterialUpdateView(
    CourseMenuMixin,
    MaterialRedirectMixin,
    UpdateView):
    """
    Update Material
    """
    form_class = MaterialForm
    model = Material
    context_object_name ='material'
    form_valid_message = "Das Material wurde geändert!"


class MaterialDeleteView(
    CourseMenuMixin,
    MaterialRedirectMixin,
    DeleteView):
    """
    Delete Material
    """
    model=Material
    context_object_name ='material'
    form_valid_message = "Das Material wurde gelöscht!"


class MaterialCreateView(
    CourseMenuMixin,
    MaterialRedirectMixin,
    FormView):
    """
    Create Material
    """
    form_class = MaterialForm
    model = Material
    context_object_name ='material'
    form_valid_message = "Das Material wurde angelegt!"

    def form_valid(self, form):

        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])
        material = Material.objects.create(
            course=course,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            document_type=form.cleaned_data['document_type'],
            pdf_link=form.cleaned_data['pdf_link'],
            pdf_download_link=form.cleaned_data['pdf_download_link'],
            pdf_viewer=form.cleaned_data['pdf_viewer'],
            file=self.request.FILES['file']
        )

        return super(MaterialCreateView, self).form_valid(form)

