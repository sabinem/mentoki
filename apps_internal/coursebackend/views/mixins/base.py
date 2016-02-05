# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from braces.views import LoginRequiredMixin, UserPassesTestMixin

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.course.models.course import Course
from apps_core.core.mixins import TemplateMixin


class AuthMixin(LoginRequiredMixin, UserPassesTestMixin, TemplateMixin):
    """
    this Mixin builds the menu in the side-bar and the top of the page.
    """
    raise_exception = False
    login_url = settings.LOGIN_REDIRECT_URL
    redirect_field_name = settings.LOGIN_REDIRECT_URL

    def test_func(self, user):
        """
        This function belongs to the Braces Mixin UserPasesTest: test for using the course backend.
        Only the Superuser and the owner of the course are allowed
        """
        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])
        if user.is_superuser:
            self.request.session['workon_course_id'] = course.id
            return True
        else:
            if course.is_owner(user):
                self.request.session['workon_course_id'] = course.id
                return True
        self.messages.warning(_('You are not allowed to change this data since you are not a teacher of this course.'))
        return None


class CourseMenuMixin(AuthMixin):
    def get_context_data(self, **kwargs):
        context = super(CourseMenuMixin, self).get_context_data(**kwargs)
        if not 'course' in context:
            context['course'] = get_object_or_404(Course, slug=self.kwargs['course_slug'])
        context['cs'] = context['course'].slug
        if not 'courseevents' in context:
            context['courseevents'] = \
                CourseEvent.objects.active_courseevents_for_course(
                    course=context['course']
                )
        if 'slug' in self.kwargs:
            if not 'courseevent' in context:
                context['courseevent'] = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
            context['es'] = context['courseevent'].slug
        context['url_name'] = self.request.resolver_match.url_name
        return context


class FormCourseKwargsMixin(object):
    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        kwargs = super(FormCourseKwargsMixin, self).get_form_kwargs()
        kwargs['course_slug']=course_slug
        return kwargs


class FormCourseEventKwargsMixin(object):
    def get_form_kwargs(self):
        courseevent_slug = self.kwargs['slug']
        kwargs = super(FormCourseEventKwargsMixin, self).get_form_kwargs()
        kwargs['courseevent_slug']=courseevent_slug
        return kwargs