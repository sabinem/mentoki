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

        if self.request.user.checkout_product_slug:
            user = User.objects.get(id=self.request.user.id)
            slug = user.checkout_product_slug
            user.checkout_product_slug = None
            user.save()
            kwargs['slug'] = slug
            logger.info('[%s] wird weitergeleitet zu Buchung [%s]'
                        % self.request.user, slug)
            url = reverse('checkout:payment', kwargs=kwargs)
            return url

        # is the user registered as a courseowner?
        elif self.request.user.teaching != []:
            logger.info('[%s] wird weitergeleitet zu seinem Unterricht auf '
                        'dem Schreibtisch'
                        % self.request.user)
            return reverse('desk:teach')

        elif self.request.user.studying() != []:
            logger.info('[%s] wird weitergeleitet zu seinen Lern-Kursen auf '
                        'dem Schreibtisch'
                        % self.request.user)
            return reverse('desk:learn')

        else:
            logger.info('[%s] wird weitergeleitet zu seinen Profildaten '
                        'dem Schreibtisch'
                        % self.request.user)
            return reverse('desk:profile')
