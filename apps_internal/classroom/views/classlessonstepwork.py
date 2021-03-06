# coding: utf-8

from __future__ import unicode_literals, absolute_import
import floppyforms.__future__ as forms

from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView, \
    FormView, DeleteView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from froala_editor.widgets import FroalaEditor

from apps_data.lesson.models.classlesson import ClassLesson
from apps_core.email.utils.comment import send_work_comment_notification
from apps_core.email.utils.homework import send_work_published_notification
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.courseevent.models.homework import StudentsWork, Comment

from .mixins.base import ClassroomMenuMixin, AuthClassroomAccessMixin, \
    ParticipationFormKwargsMixin, ParticipationCheckHiddenFormMixin
from .classlessonstep import LessonStepContextMixin, StudentsWorkContextMixin

from apps_internal.coursebackend.views.mixins.base import \
    FormCourseEventKwargsMixin


import logging
logger = logging.getLogger(__name__)


class StudentWorkCommentForm(
    ParticipationCheckHiddenFormMixin,
    forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Comment
        fields = ('title', 'text')


class StudentsWorkCommentView(
    AuthClassroomAccessMixin,
    ParticipationFormKwargsMixin,
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
        logger.info("[%s] Kommentar zu %s von %s"
                    % (courseevent, comment , self.request.user))
        mail_distributor = send_work_comment_notification(
                studentswork = comment.studentswork,
                courseevent=comment.courseevent,
                comment = comment,
                module=self.__module__,
            )
        logger.info("[%s] Email gesendet an %s" % (courseevent, mail_distributor))

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):

        context = super(StudentsWorkCommentView, self).get_context_data(**kwargs)
        studentswork = get_object_or_404(StudentsWork, pk=self.kwargs['work_pk'])
        context['studentswork'] = studentswork
        context['comments'] = \
            Comment.objects.comment_to_studentswork(studentswork=context['studentswork'])

        return context

    def get_success_url(self):
       return reverse_lazy('classroom:classlesson:publicstudentswork',
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


class StudentWorkUpdatePublicForm(
    ParticipationCheckHiddenFormMixin,
    forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)
    republish = forms.BooleanField(required=False)

    class Meta:
        model = StudentsWork
        fields = ('title', 'text')


class StudentsWorkUpdatePublicView(
    AuthClassroomAccessMixin,
    ParticipationFormKwargsMixin,
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


class StudentWorkUpdatePrivateForm(
    ParticipationCheckHiddenFormMixin,
    forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = StudentsWork
        fields = ('title', 'text', 'published')


class StudentsWorkUpdatePrivateView(
    AuthClassroomAccessMixin,
    ParticipationFormKwargsMixin,
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
    AuthClassroomAccessMixin,
    ParticipationFormKwargsMixin,
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
    AuthClassroomAccessMixin,
    ParticipationFormKwargsMixin,
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
                    studentswork = self.object,
                    courseevent=self.object.courseevent,
                    module=self.__module__,
                )
        return HttpResponseRedirect(self.get_success_url())


class StudentWorkAddTeamForm(
    ParticipationCheckHiddenFormMixin,
    forms.ModelForm):

    class Meta:
        model = StudentsWork
        fields = ('workers',)
        widgets = {'workers': forms.CheckboxSelectMultiple}

    def __init__(self, *args, **kwargs):
        courseevent_slug = kwargs.pop('courseevent_slug', None)
        print courseevent_slug
        print "____________"
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)
        print self.courseevent
        super(StudentWorkAddTeamForm, self).__init__(*args, **kwargs)
        print "I am here"
        self.fields['workers'].queryset = self.courseevent.workers()
        print "now load"


class StudentsWorkAddTeamView(
    AuthClassroomAccessMixin,
    ParticipationFormKwargsMixin,
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