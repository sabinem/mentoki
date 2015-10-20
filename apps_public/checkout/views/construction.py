# coding: utf-8

"""
Braintree Integration Payment Form
"""

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView


class ConstructionView(
    TemplateView):
    """
    This view is called if the payment has been successful.
    """
    template_name = 'under-construction.html'
