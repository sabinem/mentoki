# coding: utf-8
from __future__ import unicode_literals
from .forms_contact import  ContactForm
from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email_visitor()
        form.send_email_self()
        return super(ContactView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            'contact:answer'
        )


class AnswerView(TemplateView):

    template_name = 'contact_answer/answer.html'
