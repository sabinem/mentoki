# coding: utf-8

from __future__ import unicode_literals, absolute_import
import floppyforms.__future__ as forms

from django.views.generic import UpdateView, FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from braces.views import FormValidMessageMixin

from froala_editor.widgets import FroalaEditor

from apps_data.course.models.course import Course
from apps_data.lesson.models.lesson import Lesson

from ..mixins.base import CourseMenuMixin
from .mixins import LessonSuccessUpdateUrlMixin, LessonContextMixin


class LessonBlockForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Lesson
        fields = ('title', 'description', 'text', 'nr')

    def __init__(self, *args, **kwargs):
        super(LessonBlockForm, self).__init__(*args, **kwargs)
        self.fields['text'].required = False


class BlockUpdateView(
    LessonContextMixin,
    LessonSuccessUpdateUrlMixin,
    FormValidMessageMixin,
    UpdateView):
    """
    lesson block update
    """
    form_class = LessonBlockForm
    model = Lesson
    context_object_name ='lessonblock'
    form_valid_message = "Der Block wurde geändert!"


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
        print "==== HELLO ====="
        self.object = Lesson.objects.create_block(
            course=course,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            nr=form.cleaned_data['nr'],
        )
        list_url = reverse('coursebackend:lessontest:blockswithlessons',
                           kwargs={'course_slug': self.kwargs['course_slug'],})
        return HttpResponseRedirect(list_url)
