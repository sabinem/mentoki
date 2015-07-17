# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin, MessageMixin, UserPassesTestMixin

from apps_data.courseevent.models import CourseEvent

from apps_data.course.models import Course


class AuthMixin(LoginRequiredMixin, UserPassesTestMixin, MessageMixin):
    """
    this Mixin builds the menu in the side-bar and the top of the page.
    """
    def get_context_data(self, **kwargs):
        context = super(AuthMixin, self).get_context_data(**kwargs)

        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])

        context['course'] = course

        return context

    def test_func(self, user):
        """
        This function belongs to the Braces Mixin UserPasesTest: test for using the course backend.
        Only the Superuser and the owner of the course are allowed
        """
        if user.is_superuser:
            return True
        else:
            try:
                course = get_object_or_404(Course, slug=self.kwargs['course_slug'])
                if user in course.teachers:
                    return True
            except:
                pass
        return None


class CourseMenuMixin(AuthMixin):

    def get_context_data(self, **kwargs):
        context = super(CourseMenuMixin, self).get_context_data(**kwargs)

        courseevents = CourseEvent.objects.courseevents_for_course(course=context['course'])

        context['courseevents'] = courseevents

        return context