# coding: utf-8
from __future__ import unicode_literals
from .forms_contact import  ContactForm, PrebookForm, ApplicationForm, NewsletterForm, WebinarForm
from django.views.generic import FormView, TemplateView, CreateView
from django.core.urlresolvers import reverse
from .models import Contact
from apps.courseevent.models import CourseEvent
from braces.views import MessageMixin
from django.utils.safestring import mark_safe

class ContactView(CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email_visitor()
        form.send_email_self()
        form.instance.contacttype = Contact.CONTACT_GENERAL
        name = form.cleaned_data['name']
        message = mark_safe("""<h1>Hallo %s! </h1><p>Danke für Dein Interesse an Mentoki.</p><p>
                  Du hörst von uns innerhalb der nächsten 48 Stunden.</p>""") % name
        self.messages.info(message)
        return super(ContactView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            'contact:answer'
        )


class PrebookView(CreateView):
    template_name = 'contact/prebook.html'
    form_class = PrebookForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email_visitor()
        form.send_email_self()
        form.instance.contacttype = Contact.CONTACT_STUDENT
        name = form.cleaned_data['name']
        courseevent = form.cleaned_data['courseevent']
        message = mark_safe("""<h1>Hallo %s! </h1><p>Danke für Dein Interesse am Kurs %s.</p><p>
                  Du hörst von uns sobald die Anmeldung für diesen Kurs freigeschaltet ist.</p>""") % (name, courseevent)
        self.messages.info(message)
        return super(PrebookView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            'contact:answer', kwargs={'slug': self.object.courseevent.slug}
        )


class ApplicationView(CreateView, MessageMixin):
    template_name = 'contact/application.html'
    form_class = ApplicationForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email_visitor()
        form.send_email_self()
        form.instance.contacttype = Contact.CONTACT_TEACHER
        name = form.cleaned_data['name']
        message = mark_safe("""<h1>Hallo %s! </h1><p>Danke für Dein Interesse am Mentoki Starterkurs.</p><p>
                  Du hörst von uns innerhalb der nächsten 48 Stunden.</p>""") % name
        self.messages.info(message)
        return super(ApplicationView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            'contact:answer'
        )


class WebinarView(CreateView, MessageMixin):
    template_name = 'contact/webinar.html'
    form_class = WebinarForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email_visitor()
        form.send_email_self()
        form.instance.contacttype = Contact.CONTACT_TEACHER
        name = form.cleaned_data['name']
        message = mark_safe("""<h1>Hallo %s! </h1><p>Danke für Dein Interesse am Webinar "Warum Du jetzt in den Online-Unterricht einsteigen solltest".</p><p>
                  Du hörst von uns sobald wir einen neuen Termin dafür planen.</p>""") % name
        self.messages.info(message)
        return super(WebinarView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            'contact:answer'
        )


class NewsletterView(CreateView, MessageMixin):
    template_name = 'contact/newsletter.html'
    form_class = NewsletterForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email_visitor()
        form.send_email_self()
        form.instance.contacttype = Contact.CONTACT_TEACHER
        name = form.cleaned_data['name']
        message = mark_safe("""<h1>Hallo %s! </h1><p>Danke für Abbonieren des Mentoki Newsletters.</p><p>
                  Du erhältst die nächste Ausgabe, sobald sie erscheint.</p>""") % name
        self.messages.info(message)
        return super(NewsletterView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            'contact:answer'
        )



class AnswerView(TemplateView):

    template_name = 'contact_answer/answer.html'
