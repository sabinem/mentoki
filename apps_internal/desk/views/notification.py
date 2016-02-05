# coding: utf-8

"""
Entrypoint for updtaing and viewing the users profile
"""
#TODO: update possiblity is missing so far

from __future__ import unicode_literals, absolute_import
import floppyforms.__future__ as forms

from django.views.generic import TemplateView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from apps_data.courseevent.models.courseevent import CourseEventParticipation
from apps_data.courseevent.constants import NotificationSettings

import logging
logger = logging.getLogger('activity.users')


class NotificationView(
    LoginRequiredMixin,
    TemplateView):
    """
    This view shows the users profile with his different roles
    as mentor and as customer
    """
    template_name = 'desk/pages/notification.html'

    def get_context_data(self, **kwargs):
        """
        gets the users profile as mentor and customer
        """
        logger.info('[%s] sieht sich sein Notifikations-Eistellungen auf dem Schreibtisch an'
                    % self.request.user)
        context = super(NotificationView, self).get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        # get mentor_profile
        try:
            participations = CourseEventParticipation.objects.active_learning(user=user)
            context['participations'] = participations
        except ObjectDoesNotExist:
            pass
        context['NotificationSettings'] = NotificationSettings
        print NotificationSettings.ALL
        return context


class NotificationUpdateForm(forms.ModelForm):

    class Meta:
        model = CourseEventParticipation
        fields = ('notification_forum', 'notification_work')


class NotificationUpdateView(
    LoginRequiredMixin,
    UpdateView):
    """
    In this View the whole menu can be updated at once, but only the
    fields display_title and display_nr can be changed here.
    """
    model = CourseEventParticipation
    template_name = 'desk/pages/notificationupdate.html'
    form_class = NotificationUpdateForm
    notifications_settings = NotificationSettings

    def get_context_data(self, **kwargs):
        """
        gets the users profile as mentor and customer
        """
        logger.info('[%s] ändert seine Notifikations-Eistellungen'
                    % self.request.user)
        context = super(NotificationUpdateView, self).get_context_data(**kwargs)
        context['NotificationSettings'] = NotificationSettings
        return context

    def get_success_url(self):
       return reverse_lazy('desk:notifications')

