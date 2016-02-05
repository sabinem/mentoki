# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView

from apps_data.courseevent.models.homework import StudentsWork,Comment
from apps_data.lesson.models.classlesson import Question
from apps_data.lesson.models.classlesson import ClassLesson

from .mixins.base import ClassroomMenuMixin, AuthClassroomAccessMixin


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
    AuthClassroomAccessMixin,
    ClassroomMenuMixin,
    LessonStepContextMixin,
    TemplateView):
    """
    Shows one classlesson-step
    """
    def get_context_data(self, **kwargs):
        context = super(ClassLessonStepDetailView, self).get_context_data(**kwargs)
        lessonstep = context['lessonstep']
        if lessonstep.is_homework:
            context['studentsworks'] = \
                StudentsWork.objects.turnedin_homework(homework=lessonstep)
        if lessonstep.allow_questions:
            context['questions'] = \
                Question.objects.question_to_lessonstep(classlessonstep=lessonstep)
        return context


class StudentsWorkPublicListView(
    AuthClassroomAccessMixin,
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
    AuthClassroomAccessMixin,
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
    AuthClassroomAccessMixin,
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


