# coding: utf-8

from __future__ import unicode_literals, absolute_import
import floppyforms.__future__ as forms

from django.core.urlresolvers import reverse_lazy

from django.views.generic import DetailView, TemplateView, UpdateView, DeleteView, FormView
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import ValidationError

from braces.views import FormValidMessageMixin

from ..forms.lesson import LessonBlockForm, LessonForm, LessonStepForm

from apps_data.course.models.course import Course

from django.shortcuts import get_object_or_404

from apps_data.lesson.models.lesson import Lesson
from apps_data.lesson.utils.lessontoblockcopy import copy_lesson_to_block

from .mixins.base import CourseMenuMixin, FormCourseKwargsMixin


class BlockListView(
    CourseMenuMixin,
    TemplateView):
    """
    List everything for a course: get the complete tree with material
    :param course_slug: slug of course
    :return: nodes: all complete trees for course
    """

    def get_context_data(self, **kwargs):
        context = super(BlockListView, self).get_context_data(**kwargs)
        context['nodes'] = Lesson.objects.start_tree_for_course(course=context['course'])
        context['blocks'] = Lesson.objects.blocks_for_course(course=context['course'])
        self.request.session['last_url'] = self.request.path
        return context


class BlockLessonsView(
    CourseMenuMixin,
    TemplateView):
    """
    List everything for a course: get the complete tree with material
    :param course_slug: slug of course
    :return: nodes: all complete trees for course
    """

    def get_context_data(self, **kwargs):
        context = super(BlockLessonsView, self).get_context_data(**kwargs)

        context['nodes'] = Lesson.objects.start_tree_for_course(course=context['course'])
        self.request.session['last_url'] = self.request.path
        return context



class HomeworkListView(
    CourseMenuMixin,
    TemplateView):
    """
    List everything for a course: get the complete tree with material
    :param course_slug: slug of course
    :return: nodes: all complete trees for course
    """

    def get_context_data(self, **kwargs):
        context = super(HomeworkListView, self).get_context_data(**kwargs)
        self.request.session['last_url'] = self.request.path
        context['homeworks'] = Lesson.objects.homeworks(course=context['course'])
        return context


class BlockDetailView(
    CourseMenuMixin,
    DetailView):
    """
    gets tree underneath a block, get neighbouring blocks within the course and get breadcrumbs
    :param pk: of lessonblock
    :param course_slug: slug of course
    :return: lessonblock: block instance
    :return: previous_node: previous block within course
    :return: next_node: next block within course
    :return: breadcrumbs: ancestors including block instance
    :return: nodes: tree underneath of block instance without material
    """
    model = Lesson
    context_object_name ='lessonblock'

    def get_context_data(self, **kwargs):
        context = super(BlockDetailView, self).get_context_data(**kwargs)
        lessonblock = context['lessonblock']
        self.request.session['last_url'] = self.request.path
        context['next_node'] = lessonblock.get_next_sibling()
        context['previous_node'] = lessonblock.get_previous_sibling()
        context['breadcrumbs'] = lessonblock.get_breadcrumbs_with_self()
        context['nodes'] = lessonblock.get_tree_without_self_without_material
        return context


class LessonDetailView(
    CourseMenuMixin,
    DetailView):
    """
    Detail Lesson with Lessonsteps underneath
    :param pk: of lesson
    :param course_slug: slug of course
    :return: lesson: lesson instance
    :return: previous_node: previous lesson within block
    :return: next_node: next lesson within block
    :return: breadcrumbs: ancestors including lesson instance
    :return: nodes: tree underneath of lesson instance with material
    """
    model = Lesson
    context_object_name ='lesson'

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)

        lesson = context['lesson']
        self.request.session['last_url'] = self.request.path
        context['next_node'] = lesson.get_next_sibling()
        context['previous_node'] = lesson.get_previous_sibling()
        context['breadcrumbs'] = lesson.get_breadcrumbs_with_self
        context['nodes'] = lesson.get_tree_without_self_with_material
        return context


class StepDetailView(CourseMenuMixin, DetailView):
    """
    Detail Lessonstep
    :param pk: of lessonstep
    :param course_slug: slug of course
    :return: lessonstep: lessonstep instance
    :return: previous_node: previous lessonstep within lesson
    :return: next_node: next lesson within lesson
    :return: breadcrumbs: ancestors including lessonstep instance
    """
    model = Lesson
    context_object_name ='lessonstep'

    def get_context_data(self, **kwargs):
        context = super(StepDetailView, self).get_context_data(**kwargs)

        lessonstep = context['lessonstep']
        self.request.session['last_url'] = self.request.path
        context['next_node'] = lessonstep.get_next_sibling()
        context['previous_node'] = lessonstep.get_previous_sibling()
        context['breadcrumbs'] = lessonstep.get_breadcrumbs_with_self

        return context


class LessonSuccessUrlMixin(object):
    def form_valid(self, form):
        last_url = self.request.session['last_url']
        self.object = form.save()
        return HttpResponseRedirect(last_url)


class LessonContextMixin(CourseMenuMixin):
    """
    add breadcrumbs to context in case of update or delete operations
    """
    def get_context_data(self, **kwargs):
        context = super(LessonContextMixin, self).get_context_data(**kwargs)
        if 'object' in context:
            context['breadcrumbs'] = context['object'].get_breadcrumbs_with_self
        return context


class BlockUpdateView(
    LessonContextMixin,
    LessonSuccessUrlMixin,
    FormValidMessageMixin,
    UpdateView):
    """
    lesson block update
    """
    form_class = LessonBlockForm
    model = Lesson
    context_object_name ='lessonblock'
    form_valid_message = "Der Block wurde geändert!"


class LessonUpdateView(
    LessonContextMixin,
    FormCourseKwargsMixin,
    LessonSuccessUrlMixin,
    FormValidMessageMixin,
    UpdateView):
    """
    lesson update
    """
    form_class = LessonForm
    model = Lesson
    context_object_name ='lesson'
    form_valid_message = "Die Lektion wurde geändert!"


class LessonStepUpdateView(
    LessonContextMixin,
    LessonSuccessUrlMixin,
    FormCourseKwargsMixin,
    FormValidMessageMixin,
    UpdateView):
    """
    lesson step update
    """
    form_class = LessonStepForm
    model = Lesson
    context_object_name ='lessonstep'
    form_valid_message = "Der Lernabschnitt wurde geändert!"


class LessonDeleteView(
    LessonContextMixin,
    FormValidMessageMixin,
    DeleteView):
    """
    delete lesson
    """
    model=Lesson
    context_object_name = 'lesson'
    form_valid_message = "Der Lektionsbaum wurde gelöscht!"

    def get_context_data(self, **kwargs):
        context = super(LessonDeleteView, self).get_context_data(**kwargs)
        context['nodes'] = context['object'].get_delete_tree
        return context

    def get_success_url(self):
        return reverse_lazy('coursebackend:lessontest:blockswithlessons',
                           kwargs={'course_slug': self.kwargs['course_slug'],
                                   })


class BlockCreateView(
    CourseMenuMixin,
    FormValidMessageMixin,
    FormView):
    """
    create lesson block
    """
    form_class = LessonBlockForm
    model = Lesson
    context_object_name ='lessonblock'
    form_valid_message = "Der Block wurde angelegt!"

    def form_valid(self, form):
        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])
        self.object = Lesson.objects.create_block(
            course=course,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            nr=form.cleaned_data['nr'],
        )
        last_url = self.request.session['last_url']
        return HttpResponseRedirect(last_url)


class LessonCreateView(
    CourseMenuMixin,
    FormCourseKwargsMixin,
    LessonSuccessUrlMixin,
    FormValidMessageMixin,
    FormView):
    """
    create lesson
    """
    form_class = LessonForm
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



class LessonStepCreateView(
    CourseMenuMixin,
    FormCourseKwargsMixin,
    FormValidMessageMixin,
    FormView):
    """
    create lesson step, special: add materials if requested
    """
    form_class = LessonStepForm
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
        )
        last_url = self.request.session['last_url']
        return HttpResponseRedirect(last_url)

