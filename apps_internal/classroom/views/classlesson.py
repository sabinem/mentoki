# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, FormView, DetailView
from django.http import HttpResponseRedirect

from apps_data.courseevent.models.homework import StudentsWork,Comment
from apps_data.courseevent.models.menu import ClassroomMenuItem
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.lesson.models.classlesson import ClassLesson
from apps_core.email.utils.comment import send_work_comment_notification

from .mixins.base import ClassroomMenuMixin
from ..forms.studentswork import StudentWorkCommentForm


class ClassLessonStartView(
    ClassroomMenuMixin,
    TemplateView):
    """
    Shows all classlessons that are published in the class (have a menu entry in the classroom menu)
    """
    def get_context_data(self, **kwargs):
        context = super(ClassLessonStartView, self).get_context_data(**kwargs)

        context['lesson_items'] = \
            ClassroomMenuItem.objects.lessons_for_courseevent(
                courseevent=context['courseevent'])

        return context


class ClassLessonDetailView(
    ClassroomMenuMixin,
    TemplateView):
    """
    Show classlesson in Detail
    List all classlesson-steps of a lesson (they are all published along with the lesson)
    """
    def get_context_data(self, **kwargs):
        context = super(ClassLessonDetailView, self).get_context_data(**kwargs)

        lesson = get_object_or_404(ClassLesson, pk=self.kwargs['pk'])

        context['lesson'] = lesson
        context['breadcrumbs'] = lesson.get_published_breadcrumbs_with_self
        context['next_node'] = lesson.get_next_sibling_published
        context['previous_node'] = lesson.get_previous_sibling_published
        context['lessonsteps'] = lesson.get_children()

        return context


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


class StudentsWorkDetailView(
    ClassroomMenuMixin,
    LessonStepContextMixin,
    DetailView):
    """
    shows detail of a students work, that is published in the homework section
    """
    model = StudentsWork
    pk_url_kwarg = 'work_pk'
    context_object_name ='studentswork'

    def get_context_data(self, **kwargs):
        context = super(StudentsWorkDetailView, self).get_context_data(**kwargs)
        context['comments'] = \
            Comment.objects.comment_to_studentswork(studentswork=context['studentswork'])

        return context


class StudentsWorkCommentView(
    ClassroomMenuMixin,
    LessonStepContextMixin,
    FormView):
    """
    provides a form for the rest of the class and the teacher to comment on a students work
    """
    form_class = StudentWorkCommentForm

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        studentswork = get_object_or_404(StudentsWork, pk=self.kwargs['work_pk'])
        comment = Comment.objects.create_comment(courseevent=courseevent,
                               text=form.cleaned_data['text'],
                               title=form.cleaned_data['title'],
                               studentswork=studentswork,
                               author=self.request.user)
        # make email to all people participating
        mail_distributor = send_work_comment_notification(
                studentswork = comment.studentswork,
                courseevent=comment.courseevent,
                comment = comment,
                module=self.__module__,
            )
        print "------------"
        print "sending mail %s" % (mail_distributor)
        print "_______________"
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):

        context = super(StudentsWorkCommentView, self).get_context_data(**kwargs)
        studentswork = get_object_or_404(StudentsWork, pk=self.kwargs['work_pk'])
        context['studentswork'] = studentswork

        return context

    def get_success_url(self):
       return reverse_lazy('classroom:classlesson:studentswork',
                           kwargs={'slug': self.kwargs['slug'], 'pk':self.kwargs['pk'],
                                   'work_pk':self.kwargs['work_pk']})

