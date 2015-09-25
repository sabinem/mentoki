# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, FormView, DetailView
from django.http import HttpResponseRedirect

from apps_data.courseevent.models.homework import StudentsWork,Comment
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.lesson.models.classlesson import ClassLesson
from apps_core.email.utils.comment import send_work_comment_notification

from .mixins.base import ClassroomMenuMixin
from ..forms.studentswork import StudentWorkCommentForm


class LessonStepContextMixin(object):
    """
    adds the homework to the context
    """
    def get_context_data(self, **kwargs):
        context = super(LessonStepContextMixin, self).get_context_data(**kwargs)

        lessonstep = get_object_or_404(ClassLesson, pk=self.kwargs['pk'])
        context['lessonstep'] = lessonstep
        context['breadcrumbs'] = lessonstep.get_published_breadcrumbs_with_self
        context['next_node'] = lessonstep.get_next_sibling()
        context['previous_node'] = lessonstep.get_previous_sibling()

        return context


class ClassLessonStepDetailView(
    ClassroomMenuMixin,
    LessonStepContextMixin,
    TemplateView):
    """
    Shows one classlesson-step
    """
    def get_context_data(self, **kwargs):
        context = super(ClassLessonStepDetailView, self).get_context_data(**kwargs)

        if context['lessonstep'].is_homework:
                context['studentsworks'] = \
                    StudentsWork.objects.turnedin_homework(homework=context['lessonstep'])

        return context


class StudentsWorkPublicListView(
    ClassroomMenuMixin,
    LessonStepContextMixin,
    TemplateView):
    """
    Shows published students works
    """
    def get_context_data(self, **kwargs):
        context = super(StudentsWorkPublicListView, self).get_context_data(**kwargs)

        if context['lessonstep'].is_homework:
                context['studentsworks'] = \
                    StudentsWork.objects.turnedin_homework(homework=context['lessonstep'])

        return context


class StudentsWorkPrivateListView(
    ClassroomMenuMixin,
    LessonStepContextMixin,
    TemplateView):
    """
    Shows private students works
    """
    def get_context_data(self, **kwargs):
        context = super(StudentsWorkPrivateListView, self).get_context_data(**kwargs)

        if context['lessonstep'].is_homework:
                context['studentsworks'] = \
                    StudentsWork.objects.unpublished_homework(homework=context['lessonstep'],
                                                              user=self.request.user)

        return context


class StudentsWorkContextMixin(object):
    """
    adds the homework to the context
    """
    def get_context_data(self, **kwargs):
        context = super(StudentsWorkContextMixin, self).get_context_data(**kwargs)

        context['comments'] = \
            Comment.objects.comment_to_studentswork(studentswork=context['studentswork'])

        return context


class StudentsWorkDetailView(
    ClassroomMenuMixin,
    LessonStepContextMixin,
    StudentsWorkContextMixin,
    DetailView):
    """
    shows detail of a students work, that is published in the homework section
    """
    model = StudentsWork
    pk_url_kwarg = 'work_pk'
    context_object_name ='studentswork'


