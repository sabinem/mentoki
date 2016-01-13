# coding: utf-8

"""
Contact Form and Answer Page
"""

from __future__ import unicode_literals

from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse

from braces.views import MessageMixin

from apps_core.core.mixins import TemplateMixin

from .forms import ContactForm

class ContactView(TemplateMixin, MessageMixin, FormView):
    form_class = ContactForm

    def form_valid(self, form):
        """
        An email is send to mentoki and to the visitor
        """
        form.send_email_visitor()
        form.send_email_self()

        self.request.session['name'] = form.cleaned_data['name']
        return super(ContactView, self).form_valid(form)

    def get_success_url(self):
        """
        an answer page is shown
        """
        return reverse(
            'contact:answer'
        )


class AnswerView(TemplateMixin, TemplateView):
    """
    Answer Page
    """
    pass
