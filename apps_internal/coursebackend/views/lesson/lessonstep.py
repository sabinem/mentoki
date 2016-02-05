# coding: utf-8

from __future__ import unicode_literals, absolute_import
import floppyforms.__future__ as forms

from django.views.generic import UpdateView, FormView
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.core.validators import ValidationError

from braces.views import FormValidMessageMixin
from mptt.forms import TreeNodeChoiceField
from froala_editor.widgets import FroalaEditor

from apps_data.course.models.course import Course
from apps_data.lesson.models.lesson import Lesson
from apps_data.material.models.material import Material
from apps_data.lesson.constants import LessonType

from ..mixins.base import CourseMenuMixin, FormCourseKwargsMixin
from .mixins import LessonContextMixin, LessonSuccessUpdateUrlMixin


class LessonStepFormMixin(object):

    def clean(self):
        if self.cleaned_data['show_work_area'] and not self.cleaned_data['is_homework']:
            raise ValidationError('Der Arbeitsbereich kann nur angezeigt werden, wenn es um eine Aufgabe'
                                  ' geht.')
        if self.cleaned_data['allow_questions'] and self.cleaned_data['is_homework']:
            raise ValidationError('Es kann nur Aufgabe oder Fragen stellen ausgewählt werden. Nicht beides!'
                                 )


class LessonStepUpdateForm(
    LessonStepFormMixin,
    forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = Lesson
        fields = ('parent', 'nr', 'show_number', 'title', 'description',
                  'text', 'material', 'is_homework', 'show_work_area',
                  'allow_questions')

    def __init__(self, *args, **kwargs):
        course_slug = kwargs.pop('course_slug', None)
        self.course = get_object_or_404(Course, slug=course_slug)
        super(LessonStepUpdateForm, self).__init__(*args, **kwargs)
        self.fields['parent'] = TreeNodeChoiceField(
            queryset=Lesson.objects.lessons_for_course(course=self.course))
        self.fields['material'].queryset = Material.objects.materials_for_course(course=self.course)
        self.fields['parent'].empty_label = None


class LessonStepUpdateView(
    LessonContextMixin,
    LessonSuccessUpdateUrlMixin,
    FormCourseKwargsMixin,
    FormValidMessageMixin,
    UpdateView):
    """
    lesson step update
    """
    form_class = LessonStepUpdateForm
    model = Lesson
    context_object_name ='lessonstep'
    form_valid_message = "Der Lernabschnitt wurde geändert!"


class LessonStepCreateForm(
    LessonStepFormMixin,
    forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = Lesson
        fields = ('parent', 'nr', 'show_number', 'title',
                  'description', 'text', 'material', 'is_homework',
                  'show_work_area', 'allow_questions' )

    def __init__(self, *args, **kwargs):
        course_slug = kwargs.pop('course_slug', None)
        lesson_pk = kwargs.pop('lesson_pk', None)
        self.course = get_object_or_404(Course, slug=course_slug)
        try:
            self.lesson = Lesson.objects.get(pk=lesson_pk)
        except ObjectDoesNotExist:
            self.lesson = None
        super(LessonStepCreateForm, self).__init__(*args, **kwargs)
        self.fields['parent'] = TreeNodeChoiceField(
            queryset=Lesson.objects.lessons_for_course(course=self.course))
        if self.lesson:
            self.fields['parent'].initial = self.lesson
        self.fields['material'].queryset = Material.objects.materials_for_course(course=self.course)
        self.fields['parent'].empty_label = None



class LessonStepCreateView(
    CourseMenuMixin,
    FormCourseKwargsMixin,
    FormValidMessageMixin,
    FormView):
    """
    create lesson step, special: add materials if requested
    """
    form_class = LessonStepCreateForm
    model = Lesson
    context_object_name ='lessonstep'
    form_valid_message = "Der Lernabschnitt wurde angelegt!"

    def form_valid(self, form):
        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])

        self.object = Lesson.objects.create_step(
            course=course,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            material=form.cleaned_data['material'],
            nr=form.cleaned_data['nr'],
            parent=form.cleaned_data['parent'],
            is_homework = form.cleaned_data['is_homework'],
            show_number = form.cleaned_data['show_number'],
            show_work_area = form.cleaned_data['show_work_area'],
            allow_questions = form.cleaned_data['allow_questions'],
        )
        last_url = self.request.session['last_url']
        return HttpResponseRedirect(last_url)

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        lesson_pk = None
        if self.request.session['last_lesson_type'] ==  LessonType.LESSON:
            lesson_pk = self.request.session['last_lesson_pk']
        kwargs = super(LessonStepCreateView, self).get_form_kwargs()
        kwargs['course_slug'] = course_slug
        kwargs['lesson_pk'] = lesson_pk
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(LessonStepCreateView, self).get_context_data(**kwargs)
        try:
            if self.request.session['last_lesson_type'] ==  LessonType.LESSON:
                lesson = Lesson.objects.get(pk=self.request.session['last_lesson_pk'])
                context['breadcrumbs'] = lesson.get_breadcrumbs_with_self
        except ObjectDoesNotExist:
            pass
        return context