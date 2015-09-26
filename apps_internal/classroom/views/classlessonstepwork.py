# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView, UpdateView, \
    FormView, DeleteView
from django.http import HttpResponseRedirect

from apps_data.courseevent.models.homework import StudentsWork, Comment
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.lesson.models.classlesson import ClassLesson
from apps_core.email.utils.comment import send_work_comment_notification
from apps_core.email.utils.homework import send_work_published_notification

from .mixins.base import ClassroomMenuMixin
from .classlessonstep import LessonStepContextMixin, StudentsWorkContextMixin
from ..forms.studentswork import StudentWorkCommentForm
from apps_internal.coursebackend.views.mixins.base import \
    FormCourseEventKwargsMixin

from ..forms.studentswork import StudentWorkCreateForm, \
    StudentWorkAddTeamForm, StudentWorkUpdatePublicForm, \
    StudentWorkUpdatePrivateForm


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


class StudentsWorkRedirectMixin(
    object):
    """
    redirects after successful form submit
    """
    def get_success_url(self):
       if self.object.published:
               return reverse_lazy('classroom:classlesson:publiclist',
                                       kwargs={'slug': self.kwargs['slug'],
                                               'pk': self.object.homework.id
                                               })
       else:
            return reverse_lazy('classroom:classlesson:privatelist',
                                       kwargs={'slug': self.kwargs['slug'],
                                               'pk': self.object.homework.id})

class StudentsWorkUpdatePublicView(
    ClassroomMenuMixin,
    LessonStepContextMixin,
    StudentsWorkContextMixin,
    StudentsWorkRedirectMixin,
    UpdateView):
    """
    updates a students work object
    """
    model = StudentsWork
    form_class = StudentWorkUpdatePublicForm
    context_object_name ='studentswork'
    pk_url_kwarg = 'work_pk'

    def form_valid(self, form):
        if form.cleaned_data['republish']:
            # make email to all people participating in the work
            form.instance.publish_count += 1
            mail_distributor = send_work_published_notification(
                    studentswork = form.instance,
                    courseevent=form.instance.courseevent,
                    module=self.__module__,
                )
            print mail_distributor
        return super(StudentsWorkUpdatePublicView, self).form_valid(form)


class StudentsWorkUpdatePrivateView(
    ClassroomMenuMixin,
    LessonStepContextMixin,
    StudentsWorkRedirectMixin,
    UpdateView):
    """
    updates a students work object
    """
    model = StudentsWork
    form_class = StudentWorkUpdatePrivateForm
    context_object_name ='studentswork'
    pk_url_kwarg = 'work_pk'

    def form_valid(self, form):
        if form.cleaned_data['published']:
            form.instance.publish_count += 1
            # make email to all people participating in the work
            mail_distributor = send_work_published_notification(
                    studentswork = form.instance,
                    courseevent=form.instance.courseevent,
                    module=self.__module__,
                )
        return super(StudentsWorkUpdatePrivateView, self).form_valid(form)


class StudentsWorkDeleteView(
    ClassroomMenuMixin,
    LessonStepContextMixin,
    StudentsWorkRedirectMixin,
    DeleteView):
    """
    deletes a students work object
    """
    model = StudentsWork
    context_object_name ='studentswork'
    pk_url_kwarg = 'work_pk'


class StudentsWorkCreateView(
    ClassroomMenuMixin,
    LessonStepContextMixin,
    StudentsWorkRedirectMixin,
    FormView):
    """
    creates a students work object
    """
    model = StudentsWork
    form_class = StudentWorkUpdatePrivateForm
    context_object_name ='studentswork'

    def form_valid(self, form):
        step = get_object_or_404(ClassLesson, pk=self.kwargs['pk'])
        if form.cleaned_data['published']:
            publish_count = 1
        else:
            publish_count = 0
        self.object = StudentsWork.objects.create(
            courseevent=step.courseevent,
            homework=step,
            published=form.cleaned_data['published'],
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            publish_count=publish_count,
            user=self.request.user)
        if form.cleaned_data['published']:
            # make email to all people participating in the work
            mail_distributor = send_work_published_notification(
                    studentswork = form.instance,
                    courseevent=form.instance.courseevent,
                    module=self.__module__,
                )
        return HttpResponseRedirect(self.get_success_url())


class StudentsWorkAddTeamView(
    ClassroomMenuMixin,
    LessonStepContextMixin,
    FormCourseEventKwargsMixin,
    StudentsWorkRedirectMixin,
    UpdateView):
    """
    adds new team members to students work object
    """
    model = StudentsWork
    form_class = StudentWorkAddTeamForm
    context_object_name = 'studentswork'
    pk_url_kwarg = 'work_pk'