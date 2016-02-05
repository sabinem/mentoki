# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import floppyforms.__future__ as forms

from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from froala_editor.widgets import FroalaEditor

from apps_data.lesson.models.classlesson import ClassLesson, Question
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import ClassroomMenuMixin, AuthClassroomAccessMixin, \
    ParticipationFormKwargsMixin, ParticipationCheckHiddenFormMixin
from .classlessonstep import LessonStepContextMixin


class QuestionForm(
    ParticipationCheckHiddenFormMixin,
    forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Question
        fields = ('title', 'text')

class QuestionsView(
    AuthClassroomAccessMixin,
    ParticipationFormKwargsMixin,
    ClassroomMenuMixin,
    LessonStepContextMixin,
    FormView):
    """
    provides a form for the rest of the class and the teacher to comment on a students work
    """
    form_class = QuestionForm

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        classlessonstep = get_object_or_404(ClassLesson, pk=self.kwargs['pk'])
        Question.objects.create_question(courseevent=courseevent,
                               text=form.cleaned_data['text'],
                               title=form.cleaned_data['title'],
                               classlessonstep=classlessonstep,
                               author=self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(QuestionsView, self).get_context_data(**kwargs)
        classlessonstep = context['lessonstep']
        context['questions'] = \
            Question.objects.question_to_lessonstep(classlessonstep=classlessonstep)
        return context

    def get_success_url(self):
       return reverse_lazy('classroom:classlesson:step',
                           kwargs={'slug': self.kwargs['slug'], 'pk':self.kwargs['pk'],
                                   })

