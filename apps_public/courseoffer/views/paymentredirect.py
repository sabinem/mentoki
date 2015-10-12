# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.generic import RedirectView

from apps_data.courseevent.models.menu import ClassroomMenuItem


class PaymentRedirectView(
    RedirectView):
    """
    redirects to the start-item in the menu when entering the classroom
    """
    permanent = False

    def get_redirect_url(self, *args, **kwargs):

        user = self.request.user

        if not user.is_authenticated():

            return reverse('courseoffer:registration',
                           args=args,
                           kwargs=kwargs)
        else:

            print "ELSE CASE"
            if user.customer:
                print "customer"
            else:
                print "no customer"        
            return reverse('courseoffer:paymentmethod',
                           args=args,
                           kwargs=kwargs)