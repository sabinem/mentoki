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

import floppyforms.__future__ as forms

from braces.views import FormValidMessageMixin

from froala_editor.widgets import FroalaEditor

from apps_productdata.mentoki_product.models.courseproductgroup \
    import CourseProductGroup
from apps_accountdata.userprofiles.models.mentor import MentorsProfile
from apps_pagedata.textchunks.models import PublicTextChunks


class CourseProductGroupForm(forms.ModelForm):
    """
    used update CourseProductGroup
    """
    class Meta:
        model = CourseProductGroup
        fields = ('about', 'mentors', 'conditions', )


class MentorsProfileForm(forms.ModelForm):
    """
    used update CourseProductGroup
    """
    class Meta:
        model = MentorsProfile
        fields = ('text', )


class CourseProductGroupUpdateView(
    LoginRequiredMixin,
    #StaffuserRequiredMixin,
    UpdateView):
    """
    List everything a teacher may update
    """
    model = CourseProductGroup
    form_class = CourseProductGroupForm
    template_name = 'adminproducts/updategroup.html'
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
    template_name = 'adminproducts/updatementor.html'
    success_url = reverse_lazy('desk:profile')


class PublicTextChunksUpdateView(
    LoginRequiredMixin,
    StaffuserRequiredMixin,
    UpdateView):
    """
    Update the course one field at a time
    """
    model = PublicTextChunks
