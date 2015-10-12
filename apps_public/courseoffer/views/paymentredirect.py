# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from apps_data.courseevent.models.menu import ClassroomMenuItem

from allauth.account.decorators import verified_email_required

@verified_email_required
def paymentmanger(self, slug, pk):
    """
    redirects to the start-item in the menu when entering the classroom
    """
    return HttpResponseRedirect(reverse('courseoffer:paymentmethod',
                                        kwargs={'slug':slug,
                                                'pk':pk}))