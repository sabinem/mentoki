# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, FormView, DetailView
from django.http import HttpResponseRedirect

from apps_data.courseevent.models.homework import StudentsWork,Comment
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.lesson.models.classlesson import ClassLesson, Questions


from .mixins.base import ClassroomMenuMixin
from ..forms.studentswork import StudentWorkCommentForm


class QuestionsView(
    ClassroomMenuMixin,
    FormView):
    """
    provides a form for the rest of the class and the teacher to comment on a students work
    """
    form_class = StudentWorkCommentForm

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        classlessonstep = get_object_or_404(ClassLesson, pk=self.kwargs['work_pk'])
        Questions.objects.create_comment(courseevent=courseevent,
                               text=form.cleaned_data['text'],
                               title=form.cleaned_data['title'],
                               classlessonstep=classlessonstep,
                               author=self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(QuestionsView, self).get_context_data(**kwargs)
        context['classlessonstep'] = get_object_or_404(ClassLesson, pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
       return reverse_lazy('classroom:lessonstep:detail',
                           kwargs={'slug': self.kwargs['slug'], 'pk':self.kwargs['pk'],
                                   })

