# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import RedirectView



class PaymentStartView(
    RedirectView):
    """
    redirects to the start-item in the menu when entering the classroom
    """
    permanent = False

    def get_redirect_url(self, *args, **kwargs):

        user = self.request.user
        if not user.is_authenticated():
            return reverse('checkout:braintree_anomymous', args=args, kwargs=kwargs)
        else:
            pass

