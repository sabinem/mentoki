from .forms_contact import  ContactForm, PrebookForm, ApplicationForm
from django.views.generic import FormView, TemplateView, CreateView
from django.core.urlresolvers import reverse
from .models import Contact
from apps.courseevent.models import CourseEvent

class ContactView(CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email_visitor()
        form.send_email_self()
        form.instance.contacttype = Contact.CONTACT_GENERAL
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
        return super(PrebookView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            'contact:answerprebook', kwargs={'slug': self.object.courseevent.slug}
        )


class ApplicationView(CreateView):
    template_name = 'contact/application.html'
    form_class = ApplicationForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email_visitor()
        form.send_email_self()
        form.instance.contacttype = Contact.CONTACT_TEACHER
        return super(ApplicationView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            'contact:answerapplication'
        )


class AnswerPrebookView(TemplateView):

    template_name = 'contact_answer/answerprebook.html'

    def get_context_data(self, **kwargs):
        """
        A list of the complete material for a block is build in a way where the units are
        paired with their material
        """
        context = super(AnswerPrebookView, self).get_context_data(**kwargs)
        try:
            courseevent = CourseEvent.objects.get(slug=kwargs['slug'])
        except:
            pass
        context['courseevent'] = courseevent
        return context


class AnswerView(TemplateView):

    template_name = 'contact_answer/answer.html'


class AnswerApplicationView(TemplateView):

    template_name = 'contact_answer/answerapplication.html'