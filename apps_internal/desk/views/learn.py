# coding: utf-8

"""
Entrypoint from the users role as a learner
"""

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin

from apps_data.notification.models.classroomnotification import ClassroomNotification

import logging
logger = logging.getLogger('activity.users')


class DeskLearnView(
    LoginRequiredMixin,
    TemplateView):
    """
    This View shows all the classes where the user is enrolled and
    serves as entry point for these classes
    """
    template_name = 'desk/pages/learn.html'

    def get_context_data(self, **kwargs):
        """
        gets all the courses, which the user studies
        :param kwargs: None
        :return: context: queryset of courseevents, where the user is enrolled
        """
        logger.info('[%s] sieht sich seine Kurse an, in denen er lernt'
                    % self.request.user)
        context = super(DeskLearnView, self).get_context_data(**kwargs)
        context['study_courseevents'] = self.request.user.studying()
        context['notifications'] = ClassroomNotification.objects.notification_by_user(
            user = self.request.user,

        )

        return context


class DeskStartView(
    LoginRequiredMixin,
    TemplateView):
    """
    This View shows all the classes where the user is enrolled and
    serves as entry point for these classes
    """
    template_name = 'desk/pages/start.html'
