# -*- coding: utf-8 -*-

"""
Views for internally viewing and editing courses. These views are only
accessible by teachers. Access is tested by CourseMenuMixin.


"""

from __future__ import unicode_literals

from django.conf import settings
from django.forms.widgets import TextInput
from django.views.generic import DetailView, UpdateView, TemplateView
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from braces.views import FormValidMessageMixin

from froala_editor.widgets import FroalaEditor

from apps_productdata.mentoki_product.models.courseproductgroup \
    import CourseProductGroup
from apps_accountdata.userprofiles.models.mentor import MentorsProfile
from apps_pagedata.textchunks.models import PublicTextChunks


class AdminListView(
    LoginRequiredMixin,
    StaffuserRequiredMixin,
    TemplateView):
    """
    List everything a teacher may update
    """
    def get_context_data(self, **kwargs):
        pass


class CourseProductGroupUpdateView(
    LoginRequiredMixin,
    StaffuserRequiredMixin,
    UpdateView):
    """
    List everything a teacher may update
    """
    model = CourseProductGroup


class MentorsProfileUpdateView(
    LoginRequiredMixin,
    StaffuserRequiredMixin,
    UpdateView):
    """
    Update the course one field at a time
    """
    model = MentorsProfile


class PublicTextChunksUpdateView(
    LoginRequiredMixin,
    StaffuserRequiredMixin,
    UpdateView):
    """
    Update the course one field at a time
    """
    model = PublicTextChunks
