# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect

from vanilla import TemplateView, DetailView, UpdateView, FormView, DeleteView

from apps_data.course.models.course import Course, CourseOwner

from .mixins.base import CourseMenuMixin
from ..forms.courseowner import TeachersCourseProfileForm


class CourseOwnerListView(CourseMenuMixin, TemplateView):
    """
    Courseowner List
    """
    def get_context_data(self, **kwargs):
        context = super(CourseOwnerListView, self).get_context_data(**kwargs)

        context['courseowners'] = CourseOwner.objects.teachers_courseinfo_all(course=context['course'])

        return context


class CourseOwnerDetailView(CourseMenuMixin, DetailView):
    """
    Courseowner List
    """
    model = CourseOwner
    context_object_name = 'courseowner'



class CourseOwnerUpdateView(CourseMenuMixin, UpdateView):
    """
    Courseowner Update
    """
    model = CourseOwner
    context_object_name = 'courseowner'
    form_class = TeachersCourseProfileForm

    def post(self, request, *args, **kwargs):
        print "----------- in post"
        self.object = self.get_object()
        form = self.get_form(data=request.POST, files=request.FILES, instance=self.object)
        print form.is_valid
        if form.is_valid():
            return self.form_valid(form)
            print "yes valid"
        return self.form_invalid(form)

    def form_valid(self, form):
        print "----------- in valid"
        print form.is_valid
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print "----------- in invalid"
        print form.is_valid
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy('coursebackend:courseowner:list',
                            kwargs={"course_slug": self.kwargs['course_slug'],})



