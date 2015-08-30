# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy

from django.views.generic import DetailView, TemplateView, UpdateView, \
    DeleteView, FormView
from django.core.validators import ValidationError

from braces.views import FormValidMessageMixin

from ..forms.classlesson import ClassLessonForm, ClassLessonStepForm
from ..forms.lessoncopy import LessonCopyForm

from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.lesson.models.lesson import Lesson

from apps_data.lesson.utils.lessoncopy import copy_lesson_selected

from .mixins.base import CourseMenuMixin, FormCourseKwargsMixin


class CopyLessonListView(
    CourseMenuMixin,
    TemplateView):
    """
    Lists all lessons and provide the option to copy them as classlessons
    for a courseevent
    :param slug: of courseevent
    :param course_slug: slug of course
    :return: lessons: all lessons of the course
             copied_lesson_ids: ids of all lessons of the course that have
             already been copied
    """

    def get_context_data(self, **kwargs):
        context = super(CopyLessonListView, self).get_context_data(**kwargs)

        context['copied_lesson_ids'] = \
            ClassLesson.objects.copied_lesson_ids(
                courseevent=context['courseevent'])
        context['lessons'] = \
            Lesson.objects.lessons_for_course(course=context['course'])

        return context


class ClassLessonStartView(
    CourseMenuMixin,
    TemplateView):
    """
    complete tree for courseevent:
    :param slug: of courseevent
    :param course_slug: slug of course
    :return: nodes: complete tree for the courseevent including blocks and material
    """

    def get_context_data(self, **kwargs):
        context = super(ClassLessonStartView, self).get_context_data(**kwargs)

        context['nodes'] = \
            ClassLesson.objects.complete_tree_for_courseevent(
                courseevent=context['courseevent'])

        return context


class ClassBlockDetailView(
    CourseMenuMixin,
    DetailView):
    """
    detail block for classlessons:
    :param slug: of courseevent
    :param course_slug: slug of course
    :param pk: of lessonblock
    :return: lessonblock: classlesson block instance
    :return: previous_node: previous classblock within courseevent
    :return: next_node: next classblock within courseevent
    :return: breadcrumbs: ancestors including self instance
    :return: nodes: tree underneath of block instance without material
    """
    model = ClassLesson
    context_object_name = 'classlessonblock'

    def get_context_data(self, **kwargs):
        context = super(ClassBlockDetailView, self).get_context_data(**kwargs)

        lessonblock = context['lessonblock']

        context['next_node'] = lessonblock.get_next_sibling_in_courseevent
        context[
            'previous_node'] = lessonblock.get_previous_sibling_in_courseevent
        context['breadcrumbs'] = lessonblock.get_breadcrumbs_with_self

        context['nodes'] = lessonblock.get_tree_without_self_without_material

        return context


class ClassLessonDetailView(
    CourseMenuMixin,
    DetailView):
    """
    detail for classlesson
    :param slug: of courseevent
    :param course_slug: slug of course
    :param pk: of classlesson
    :return: lesson: classlesson instance
    :return: previous_node: previous classlesson within courseevent
    :return: next_node: next classlesson within courseevent
    :return: breadcrumbs: ancestors including self instance
    :return: nodes: tree underneath of lesson instance with material
    """
    model = ClassLesson
    context_object_name = 'classlesson'

    def get_context_data(self, **kwargs):
        context = super(ClassLessonDetailView, self).get_context_data(**kwargs)

        classlesson = context['classlesson']

        context['next_node'] = classlesson.get_next_sibling_in_courseevent
        context[
            'previous_node'] = classlesson.get_previous_sibling_in_courseevent
        context['breadcrumbs'] = classlesson.get_breadcrumbs_with_self

        context['nodes'] = classlesson.get_tree_without_self_with_material
        print context
        return context


class ClassStepDetailView(
    CourseMenuMixin,
    DetailView):
    """
    Detail ClassLessonstep
    :param pk: of class lessonstep
    :param course_slug: slug of course
    :return: lessonstep: class lessonstep instance
    :return: previous_node: previous class lessonstep within classlesson
    :return: next_node: next classlessonstep within classlesson
    :return: breadcrumbs: ancestors including lessonstep instance
    """
    model = ClassLesson
    context_object_name = 'classlessonstep'

    def get_context_data(self, **kwargs):
        context = super(ClassStepDetailView, self).get_context_data(**kwargs)

        classlessonstep = context['classlessonstep']

        context['next_node'] = classlessonstep.get_next_sibling()
        context['previous_node'] = classlessonstep.get_previous_sibling()
        context['breadcrumbs'] = classlessonstep.get_breadcrumbs_with_self

        return context


class ClassLessonRedirectDetailMixin(object):
    def get_success_url(self):
       if self.context_object_name == 'classlesson':
           return reverse_lazy('coursebackend:classlesson:lesson',
                               kwargs={'course_slug': self.kwargs['course_slug'],
                                       'slug': self.kwargs['slug'],
                                       'pk': self.object.pk})
       elif self.context_object_name == 'classlessonstep':
           return reverse_lazy('coursebackend:classlesson:step',
                               kwargs={'course_slug': self.kwargs['course_slug'],
                                       'slug': self.kwargs['slug'],
                                       'pk': self.object.pk})


class ClassLessonRedirectListMixin(object):
    def get_success_url(self):
        return reverse_lazy('coursebackend:classlesson:start',
                            kwargs={'course_slug': self.kwargs['course_slug'],
                                    'slug': self.kwargs['slug']})


class ClassLessonBreadcrumbMixin(object):
    """
    get breadcrumbs for object
    """

    def get_context_data(self, **kwargs):
        context = super(ClassLessonBreadcrumbMixin, self).get_context_data(
            **kwargs)
        if 'object' in context:
            context['breadcrumbs'] = context[
                'object'].get_breadcrumbs_with_self
        return context


class ClassLessonUpdateView(
    CourseMenuMixin,
    ClassLessonBreadcrumbMixin,
    FormValidMessageMixin,
    ClassLessonRedirectDetailMixin,
    UpdateView):
    """
    Update a classlesson
    """
    form_class = ClassLessonForm
    model = ClassLesson
    context_object_name = 'classlesson'
    form_valid_message = "Die Lektion wurde geändert!"


class ClassLessonStepUpdateView(
    CourseMenuMixin,
    ClassLessonBreadcrumbMixin,
    FormValidMessageMixin,
    FormCourseKwargsMixin,
    ClassLessonRedirectDetailMixin,
    UpdateView):
    """
    Update a classlesson step
    """
    form_class = ClassLessonStepForm
    model = ClassLesson
    context_object_name = 'classlessonstep'
    form_valid_message = "Der Lernabschnitt wurde geändert!"


class ClassLessonDeleteView(
    CourseMenuMixin,
    FormValidMessageMixin,
    ClassLessonRedirectListMixin,
    DeleteView):
    """
    Delete a classlesson
    """
    model = ClassLesson
    context_object_name = 'classlesson'
    form_valid_message = "Der Unterricht wurde gelöscht!"

    def get_context_data(self, **kwargs):
        context = super(ClassLessonDeleteView, self).get_context_data(**kwargs)
        context['nodes'] = context['object'].get_delete_tree
        return context


class CopyLessonView(
    CourseMenuMixin,
    FormValidMessageMixin,
    ClassLessonRedirectListMixin,
    FormView):
    """
    Copy (and update or create) parts of a lesson into the class as classlesson
    """
    form_class = LessonCopyForm
    form_valid_message = "Die Lektion wurde wie gewünscht kopiert!"

    def get_form_kwargs(self):
        lesson_pk = self.kwargs['pk']
        kwargs = super(CopyLessonView, self).get_form_kwargs()
        kwargs['lesson_pk'] = lesson_pk
        return kwargs

    def form_valid(self, form):
        copied = copy_lesson_selected(self,
                                      lesson=form.lesson,
                                      lessonsteps=form.cleaned_data[
                                          'copy_lessonsteps'],
                                      copy_lesson=form.cleaned_data[
                                          'copy_lesson']
                                      )

        return super(CopyLessonView, self).form_valid(form)
