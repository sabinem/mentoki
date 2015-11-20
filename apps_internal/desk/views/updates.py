# -*- coding: utf-8 -*-

"""
Views for internally viewing and editing courses. These views are only
accessible by teachers. Access is tested by CourseMenuMixin.


"""

from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.forms.widgets import TextInput
from django.views.generic import DetailView, UpdateView, TemplateView
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from accounts.models import User

import floppyforms.__future__ as forms

from braces.views import FormValidMessageMixin

from froala_editor.widgets import FroalaEditor

from apps_productdata.mentoki_product.models.courseproductgroup \
    import CourseProductGroup
from apps_accountdata.userprofiles.models.mentor import MentorsProfile
from apps_pagedata.public.models import StaticPublicPages

class CourseProductGroupForm(forms.ModelForm):
    """
    used update CourseProductGroup
    """
    class Meta:
        model = CourseProductGroup
        fields = ('about', 'mentors', 'conditions', 'in_one_sentence', 'foto' )


class MentorsProfileForm(forms.ModelForm):
    """
    used update CourseProductGroup
    """
    class Meta:
        model = MentorsProfile
        fields = ('text', 'foto', 'special_power', 'at_mentoki')


class UserProfileUpdateForm(forms.ModelForm):
    """
    used update CourseProductGroup
    """
    class Meta:
        model = User
        fields = ('username', 'profile_image', )


class PageForm(forms.ModelForm):
    """
    used update CourseProductGroup
    """
    class Meta:
        model = StaticPublicPages
        fields = ('text', 'title', 'banner')


class CourseProductGroupUpdateView(
    LoginRequiredMixin,
    #StaffuserRequiredMixin,
    UpdateView):
    """
    List everything a teacher may update
    """
    model = CourseProductGroup
    form_class = CourseProductGroupForm
    template_name = 'desk/pages/updategroup.html'
    success_url = reverse_lazy('desk:profile')


class MentorsProfileUpdateView(
    LoginRequiredMixin,
    #StaffuserRequiredMixin,
    UpdateView):
    """
    Update the course one field at a time
    """
    model = MentorsProfile
    form_class = MentorsProfileForm
    template_name = 'desk/pages/updatementor.html'
    success_url = reverse_lazy('desk:userprofile')


class PublicPagesUpdateView(
    LoginRequiredMixin,
    StaffuserRequiredMixin,
    UpdateView):
    """
    Update the course one field at a time
    """
    model = StaticPublicPages
    form_class = PageForm
    context_object_name = 'page'
    template_name = 'desk/pages/updatepage.html'
    success_url = reverse_lazy('desk:pageadmin')



class UserProfileUpdateView(
    LoginRequiredMixin,
    #StaffuserRequiredMixin,
    UpdateView):
    """
    Update the course one field at a time
    """
    model = User
    form_class = UserProfileUpdateForm
    template_name = 'desk/pages/updateprofile.html'
    success_url = reverse_lazy('desk:userprofile')