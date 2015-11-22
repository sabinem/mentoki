# -*- coding: utf-8 -*-

"""
Listing of CourseProductGroups corresponding to Course

CourseProductGroup is the collection of all products that
belong to one Course
"""

from __future__ import unicode_literals

from django.views.generic import DetailView, CreateView

from apps_customerdata.customer.models.contact import Prebooking

from django.core.urlresolvers import reverse_lazy


import floppyforms.__future__ as forms

from braces.views import MessageMixin



import logging
logger = logging.getLogger('public.offerpages')


class PrebookingForm(forms.ModelForm):
    """
    used update CourseProductGroup
    """
    class Meta:
        model = Prebooking
        fields = ('interested_in_learning', 'name', 'email',
                  'message')

class ProductPrebookView(
    MessageMixin,
    CreateView):
    """
    Update the course one field at a time
    """
    model = Prebooking
    form_class = PrebookingForm
    template_name = 'storefront/pages/prebook.html'

    def get_success_url(self):
        return reverse_lazy(
            'storefront:prebooking_sucess',
            kwargs = {'pk': self.object.pk }
        )


class AnswerView(DetailView):
    template_name = 'storefront/pages/answer.html'
    model = Prebooking
