# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from mentoki.settings import LOGIN_REDIRECT_URL

from braces.views import LoginRequiredMixin, MessageMixin, UserPassesTestMixin

from apps_data.courseevent.models.courseevent import CourseEvent

from apps_data.course.models.course import Course


class AuthMixin(LoginRequiredMixin, UserPassesTestMixin, MessageMixin):
    """
    this Mixin builds the menu in the side-bar and the top of the page.
    """
    raise_exception = False
    login_url = LOGIN_REDIRECT_URL
    redirect_field_name = LOGIN_REDIRECT_URL

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

        if not 'courseevents' in context:
            context['courseevents'] = CourseEvent.objects.courseevents_for_course(course=context['course'])

        if 'slug' in self.kwargs:
            if not 'courseevent' in context:
                context['courseevent'] = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])

        return context