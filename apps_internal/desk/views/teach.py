# coding: utf-8

"""
Entrypoint from the users role as a teacher
"""

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin


class DeskTeachView(
    LoginRequiredMixin,
    TemplateView):
    """
    This View shows all the classes where the user is a teacher and
    serves as entry point for backend to these courses, where the
    teacher prepares his lessons
    """
    template_name = 'desk/pages/teach.html'

    def get_context_data(self, **kwargs):
        """
        gets all the courses, that the user teaches
        :param kwargs: -
        :return: queryset of all courses where th user is a owner
        """
        context = super(DeskTeachView, self).get_context_data(**kwargs)
        context['teach_courses'] = self.request.user.teaching()

        return context





