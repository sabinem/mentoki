# coding: utf-8
from __future__ import unicode_literals
from .forms_contact import  ContactForm
from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email_visitor()
        form.send_email_self()
        name = form.cleaned_data['name']
        message = mark_safe("""<h1>Hallo %s! </h1><p>Danke für Dein Interesse an Mentoki.</p><p>
                  Du hörst von uns innerhalb der nächsten 48 Stunden.</p>""") % name
        self.messages.info(message)
        return super(ContactView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            'contact:answer'
        )


class AnswerView(TemplateView):

    template_name = 'contact_answer/answer.html'
