# coding: utf-8

from __future__ import unicode_literals, absolute_import
import floppyforms.__future__ as forms

from django.views.generic import UpdateView, FormView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from braces.views import FormValidMessageMixin
from froala_editor.widgets import FroalaEditor

from apps_data.course.models.course import Course
from apps_data.lesson.models.lesson import Lesson
from apps_data.lesson.constants import LessonType

from ..mixins.base import CourseMenuMixin, FormCourseKwargsMixin
from .mixins import LessonContextMixin, LessonSuccessUpdateUrlMixin


class LessonUpdateForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = Lesson
        fields = ('parent', 'nr', 'show_number', 'title', 'description', 'text' )

    def __init__(self, *args, **kwargs):
        course_slug = kwargs.pop('course_slug', None)
        self.course = get_object_or_404(Course, slug=course_slug)

        super(LessonUpdateForm, self).__init__(*args, **kwargs)

        self.fields['parent'].empty_label = None
        self.fields["parent"].queryset = \
            Lesson.objects.blocks_for_course(course=self.course)


class LessonUpdateView(
    LessonContextMixin,
    FormCourseKwargsMixin,
    LessonSuccessUpdateUrlMixin,
    FormValidMessageMixin,
    UpdateView):
    """
    lesson update
    """
    form_class = LessonUpdateForm
    model = Lesson
    context_object_name ='lesson'
    form_valid_message = "Die Lektion wurde geändert!"


class LessonCreateForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = Lesson
        fields = ('parent', 'nr', 'show_number', 'title', 'description', 'text' )

    def __init__(self, *args, **kwargs):
        course_slug = kwargs.pop('course_slug', None)
        block_pk = kwargs.pop('block_pk', None)
        self.course = get_object_or_404(Course, slug=course_slug)
        try:
            self.lessonblock = Lesson.objects.get(pk=block_pk)
        except ObjectDoesNotExist:
            self.lessonblock = None

        super(LessonCreateForm, self).__init__(*args, **kwargs)

        self.fields['parent'].empty_label = None
        if self.lessonblock:
            self.fields['parent'].initial = self.lessonblock
        self.fields["parent"].queryset = \
            Lesson.objects.blocks_for_course(course=self.course)


class LessonCreateView(
    CourseMenuMixin,
    FormValidMessageMixin,
    FormView):
    """
    create lesson
    """
    form_class = LessonCreateForm
    model = Lesson
    context_object_name ='lesson'
    form_valid_message = "Die Lektion wurde angelegt!"

    def form_valid(self, form):
        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])
        self.object = Lesson.objects.create_lesson(
            course=course,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            parent=form.cleaned_data['parent'],
            nr=form.cleaned_data['nr'],
            show_number = form.cleaned_data['show_number'],
        )
        last_url = self.request.session['last_url']
        return HttpResponseRedirect(last_url)

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        block_pk = None
        if self.request.session['last_lesson_type'] ==  LessonType.BLOCK:
            block_pk = self.request.session['last_lesson_pk']
        kwargs = super(LessonCreateView, self).get_form_kwargs()
        kwargs['course_slug'] = course_slug
        kwargs['block_pk'] = block_pk
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        try:
            if self.request.session['last_lesson_type'] ==  LessonType.BLOCK:
                lessonblock = Lesson.objects.get(pk=self.request.session['last_lesson_pk'])
                context['breadcrumbs'] = lessonblock.get_breadcrumbs_with_self
        except ObjectDoesNotExist:
            pass
        return context


