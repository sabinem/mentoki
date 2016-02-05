# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import ValidationError

from braces.views import LoginRequiredMixin, MessageMixin, UserPassesTestMixin

from apps_data.courseevent.models.courseevent import CourseEvent, \
    CourseEventParticipation
from apps_data.courseevent.models.menu import ClassroomMenuItem
from apps_core.core.mixins import TemplateMixin


class AuthClassroomAccessMixin(
    LoginRequiredMixin,
    UserPassesTestMixin,
    MessageMixin,
    TemplateMixin):
    """
    this Mixin builds the menu in the side-bar and the top of the page.
    """
    raise_exception = False
    login_url = settings.LOGIN_REDIRECT_URL
    redirect_field_name = settings.LOGIN_REDIRECT_URL

    def test_func(self, user):
        """
        This function belongs to the Braces Mixin UserPasesTest:
        it tests whether the user is allowed to view the classroom.
        Only the Superuser and the owner of the course and the participants are allowed to view
        the classroom.
        """
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        if user.is_superuser:
            self.request.session['workon_courseevent_id'] = courseevent.id
            return True
        if user in courseevent.teachers:
            self.request.session['workon_courseevent_id'] = courseevent.id
            return True
        try:
            participation = CourseEventParticipation.objects.get(
                user=user,
                courseevent=courseevent
            )
            self.request.session['workon_courseevent_id'] = courseevent.id
            return True
        except ObjectDoesNotExist:
            self.messages.warning(_('Du bist nicht berechtigt für dieses '
                                    'Klassenzimmer.'))
            return None


class ClassroomMenuMixin(object):
    """
    Mixin for providing the classroom context
    """
    def get_context_data(self, **kwargs):
        """
        gets the context for the classroom menu
        """
        context = super(ClassroomMenuMixin, self).get_context_data(**kwargs)
        if not 'courseevent' in context:
            context['courseevent'] = \
                get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
            context['course'] = context['courseevent'].course
            context['es'] = context['courseevent'].slug
            context['cs'] = context['course'].slug
        if not 'menu_items' in context:
            context['menu_items'] = \
                ClassroomMenuItem.objects.\
                    all_for_courseevent(courseevent=context['courseevent'])
            context['menu_items_shortlinks'] = \
                ClassroomMenuItem.objects.\
                    shortlinks_for_courseevent(
                        courseevent=context['courseevent'])
        context['url_name'] = self.request.resolver_match.url_name
        return context


class ParticipationFormKwargsMixin(object):

    def get_form_kwargs(self):
        courseevent_slug = self.kwargs['slug']
        user = self.request.user
        kwargs = super(ParticipationFormKwargsMixin, self).get_form_kwargs()
        kwargs['user']=user
        kwargs['courseevent_slug']=courseevent_slug
        return kwargs


class ParticipationCheckHiddenFormMixin(object):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        courseevent_slug = kwargs.pop('courseevent_slug', None)
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)
        self.user = user
        super(ParticipationCheckHiddenFormMixin, self).__init__(*args, **kwargs)

    def clean(self):
        if not self.user in self.courseevent.teachers:
            participation = CourseEventParticipation.objects.get(
                            user=self.user,
                            courseevent=self.courseevent)
            if participation.hidden:
                raise ValidationError(
                    'Du bist als %s eingeloggt und nicht '
                    'aktiver Teilnehmer im Kurs' % self.user.username)