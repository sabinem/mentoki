# coding: utf-8

from __future__ import unicode_literals, absolute_import
import floppyforms.__future__ as forms

from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import ValidationError
from django.shortcuts import get_object_or_404

from braces.views import FormValidMessageMixin

from apps_data.lesson.models.lesson import Lesson
from apps_data.lesson.utils.lessontoblockcopy import copy_lesson_to_block

from ..mixins.base import CourseMenuMixin


class CopyLessonForm(forms.Form):
    lessonblock_to = forms.ModelChoiceField(queryset=None,
                                            label='Zielblock',
                                            help_text='Block, in den die Lektion kopiert werden soll')

    def __init__(self, *args, **kwargs):
        self.lesson_pk = kwargs.pop('lesson_pk', None)
        self.lesson = get_object_or_404(Lesson, pk=self.lesson_pk)
        super(CopyLessonForm, self).__init__(*args, **kwargs)

        self.fields['lessonblock_to'].empty_label = None
        self.fields['lessonblock_to'].queryset = \
            Lesson.objects.blocks_for_course(course=self.lesson.course).\
                exclude(pk=self.lesson.parent_id)


class LessonCopyView(
    CourseMenuMixin,
    FormValidMessageMixin,
    FormView):
    """
    create lesson step, special: add materials if requested
    """
    form_class = CopyLessonForm
    form_valid_message = "Die Lektion wurde kopiert!"

    def get_context_data(self, **kwargs):
        context = super(LessonCopyView, self).get_context_data(**kwargs)
        lesson = Lesson.objects.get(pk=self.kwargs['pk'])
        context['nodes'] = lesson.get_delete_tree()
        context['breadcrumbs'] = lesson.get_breadcrumbs_with_self
        return context

    def form_valid(self, form):
        try:
            lesson = Lesson.objects.get(pk=self.kwargs['pk'])
        except ObjectDoesNotExist:
            raise ValidationError('Lektion existiert nicht.')
        self.object = copy_lesson_to_block(
            lesson_pk=lesson.pk,
            block=form.cleaned_data['lessonblock_to']
        )
        return super(LessonCopyView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('coursebackend:lessontest:block',
                           kwargs={'course_slug': self.kwargs['course_slug'],
                                   'pk': self.object.parent_id})

    def get_form_kwargs(self):
        pk = self.kwargs['pk']
        kwargs = super(LessonCopyView, self).get_form_kwargs()
        kwargs['lesson_pk']= pk
        return kwargs

