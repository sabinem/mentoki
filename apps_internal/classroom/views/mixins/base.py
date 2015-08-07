# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from mentoki.settings import LOGIN_REDIRECT_URL

from braces.views import LoginRequiredMixin, MessageMixin, UserPassesTestMixin

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.courseevent.models.menu import ClassroomMenuItem
from apps_core.core.mixins import TemplateMixin


class AuthMixin(LoginRequiredMixin, UserPassesTestMixin, MessageMixin, TemplateMixin):
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
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])

        if user.is_superuser:
            self.request.session['workon_courseevent_id'] = courseevent.id
            return True

        else:

            if courseevent.is_student(user):
                self.request.session['workon_courseevent_id'] = courseevent.id
                return True
            elif user in courseevent.teachers:
                self.request.session['workon_courseevent_id'] = courseevent.id
                return True

        self.messages.warning(_('You are not allowed to change this data since you are not a teacher of this course.'))

        return None


class ClassroomMenuMixin(AuthMixin):

    def get_context_data(self, **kwargs):
        context = super(ClassroomMenuMixin, self).get_context_data(**kwargs)

        if not 'courseevent' in context:

            context['courseevent'] = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
            context['course'] = context['courseevent'].course

        if not 'menu' in context:
            context['menu_items'] = ClassroomMenuItem.objects.published(courseevent=context['courseevent'])

        return context
