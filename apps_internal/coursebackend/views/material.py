# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, UpdateView, TemplateView, FormView, DeleteView

from braces.views import MessageMixin

from apps_data.course.models.material import Material
from apps_data.courseevent.models.courseevent import Course

from .mixins.base import CourseMenuMixin
from .mixins.lesson import CourseFormMixin
from .mixins.material import MaterialMixin
from ..forms.material import MaterialForm


class MaterialMixin(CourseMenuMixin, MessageMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       self.messages.info(self.success_msg)
       return reverse_lazy('coursebackend:material:list',
                           kwargs={'course_slug': self.kwargs['course_slug']})


class MaterialListView(CourseMenuMixin, TemplateView):

    def get_context_data(self, **kwargs):
        context = super(MaterialListView, self).get_context_data(**kwargs)

        context['materials'] = Material.objects.materials_for_course(course=context['course'])
        return context


class MaterialDetailView(CourseFormMixin, DetailView):
    model = Material
    context_object_name ='material'


class MaterialUpdateView(MaterialMixin, UpdateView):
    form_class = MaterialForm
    model = Material
    context_object_name ='material'
    success_msg = "Das Material wurde geändert!"


class MaterialDeleteView(MaterialMixin, DeleteView):
    model=Material
    context_object_name ='material'
    success_msg = "Das Material wurde gelöscht!"


class MaterialCreateView(MaterialMixin, FormView):
    form_class = MaterialForm
    model = Material
    context_object_name ='material'
    success_msg = "Das Material wurde angelegt!"

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

