# -*- coding: utf-8 -*-

"""
Listing of CourseProductGroups corresponding to Course

CourseProductGroup is the collection of all products that
belong to one Course
"""

from __future__ import unicode_literals

from django.views.generic import TemplateView, CreateView

from apps_customerdata.customer.models.contact import Prebooking

from .info import CourseGroupMixin
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

import logging
logger = logging.getLogger('public.offerpages')


class PrebookingForm(forms.ModelForm):
    """
    used update CourseProductGroup
    """
    class Meta:
        model = Prebooking
        fields = ('first_name', 'last_name', 'email', 'interested_in_learning',
                  'message')

class ProductPrebookView(
    CreateView):
    """
    Update the course one field at a time
    """
    model = Prebooking
    form_class = PrebookingForm
    template_name = 'desk/pages/prebook.html'
    success_url = reverse_lazy('desk:bookings')
