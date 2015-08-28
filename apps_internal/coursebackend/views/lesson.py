# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy

from django.views.generic import DetailView, TemplateView, UpdateView, DeleteView, FormView

from braces.views import FormValidMessageMixin

from ..forms.lesson import LessonBlockForm, LessonForm, LessonStepForm

from apps_data.lesson.models.lesson import Lesson
from apps_data.course.models.course import Course

from .mixins.base import CourseMenuMixin, FormCourseKwargsMixin


class LessonStartView(
    CourseMenuMixin,
    TemplateView):
    """
    List everything for a course: get the complete tree with material
    :param course_slug: slug of course
    :return: nodes: all complete trees for course
    """
    def get_context_data(self, **kwargs):
        context = super(LessonStartView, self).get_context_data(**kwargs)

        context['nodes'] = Lesson.objects.start_tree_for_course(course=context['course'])

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

        context['next_node'] = lessonblock.get_next_sibling()
        context['previous_node'] = lessonblock.get_previous_sibling()
        context['breadcrumbs'] = lessonblock.get_breadcrumbs_with_self
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

        context['next_node'] = lessonstep.get_next_sibling()
        context['previous_node'] = lessonstep.get_previous_sibling()
        context['breadcrumbs'] = lessonstep.get_breadcrumbs_with_self

        return context


class LessonRedirectMixin(object):
    """
    redirect after successful database operation
    """
    def get_success_url(self):
       print self.context_object_name
       if self.context_object_name == 'lessonblock':
           return reverse_lazy('coursebackend:lesson:block',
                               kwargs={'course_slug': self.kwargs['course_slug'],
                                       'pk': self.object.pk})
       elif self.context_object_name == 'lesson':
           return reverse_lazy('coursebackend:lesson:lesson',
                               kwargs={'course_slug': self.kwargs['course_slug'],
                                       'pk': self.object.pk})
       elif self.context_object_name == 'lessonstep':
           return reverse_lazy('coursebackend:lesson:step',
                               kwargs={'course_slug': self.kwargs['course_slug'],
                                       'pk': self.object.pk})

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
    LessonRedirectMixin,
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
    LessonRedirectMixin,
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
    LessonRedirectMixin,
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
    LessonRedirectMixin,
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


class BlockCreateView(
    CourseMenuMixin,
    LessonRedirectMixin,
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
        self.object = Lesson.objects.create(
            course=course,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text']
        )
        return super(BlockCreateView, self).form_valid(form)


class LessonCreateView(
    CourseMenuMixin,
    FormCourseKwargsMixin,
    LessonRedirectMixin,
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
        self.object = Lesson.objects.create(
            course=course,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            parent=form.cleaned_data['parent']
        )
        return super(LessonCreateView, self).form_valid(form)


class LessonStepCreateView(
    CourseMenuMixin,
    FormCourseKwargsMixin,
    LessonRedirectMixin,
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
            parent=form.cleaned_data['parent']
        )
        return super(LessonStepCreateView, self).form_valid(form)