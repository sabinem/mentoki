# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.views.generic import RedirectView

from braces.views import MessageMixin, LoginRequiredMixin

from accounts.models import User


import logging
logger = logging.getLogger('activity.users')


class DeskRedirectView(
    LoginRequiredMixin,
    MessageMixin,
    RedirectView):
    """
    The view redirects after a user has logged in.
    If there was a checkout in progress it redirects to that checkout
    otherwise it redirects to the area where the user is active.
    """
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        """
        redirects to where the user is active and checks session first
        for an unfinished checkout
        :return: redirect url
        """
        # was there an unfinished checkout?
        user = User.objects.get(id=self.request.user.id)
        logger.info('[%s] kommt auf seinen Schreibtisch mit Wunsch: [%s]'
                                % (user, user.checkout_product_pk))

        if self.request.user.checkout_product_pk:
            user = User.objects.get(id=self.request.user.id)
            pk = user.checkout_product_pk
            user.checkout_product_pk = None
            user.save()
            kwargs['pk'] = pk
            logger.info('[%s] wird weitergeleitet zu Buchung [%s]'
                        % (self.request.user, pk))

            url = reverse('checkout:payment', kwargs=kwargs)
            return url

        else:
            logger.info('[%s] wird weitergeleitet zu seinen Lern-Kursen auf '
                        'dem Schreibtisch'
                        % self.request.user)
            return reverse('desk:learn')
