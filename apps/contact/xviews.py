from django.views.generic import CreateView, FormView, TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.template import Context
from apps.courseevent.models import CourseEvent



from .forms import ApplicationForm, ContactForm



class ContactView(SuccessMessageMixin, FormView):
    """
    Frage kann gestellt und abgeschickt werden. Es gibt dann einerseits ein Redirect
    auf die Bewerbungsseite mit Erfolgsmeldung. Andererseits wird die Frage per email
    an netTeachers geschickt.
    """
    template_name = 'question.html'
    form_class = ContactForm
    success_message = u'Wir haben Ihre Frage erhalten.  \
                      Sie h\u00f6ren von uns.' \

    def form_valid(self, form):
        email = form.cleaned_data['email']
        name = form.cleaned_data['name']
        question = form.cleaned_data['question']

        # send email to requesting email
        subject = "Ihre Frage zu netTeachers"
        to = [email]
        from_mail = 'info@netteachers.de'
        context = {
            'name': name,
            'email': email,
            'question': question,
            'betreff': "Ihre Frage",
        }
        message = get_template('email/question_outgoing.html').render(Context(context))
        msg = EmailMessage(subject, message, to=to, from_email=from_mail)
        msg.content_subtype = 'html'

        msg.send()


        # send email to self
        subject = "Beantworten: Frage zu netTeachers"
        to = ['info@netteachers.de']
        from_mail = email
        context = {
            'name': name,
            'email': email,
            'question': question,
            'betreff': "Frage zu netTeachers",
        }
        message = get_template('email/question_internal.html').render(Context(context))
        msg = EmailMessage(subject, message, to=to, from_email=from_mail)
        msg.content_subtype = 'html'

        msg.send()


        return super(ContactView, self).form_valid(form)

    def get_success_url(self):
        return reverse('contact:answer')

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        print "hallo"
        return self.initial.copy()

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        print "in form invalid"
        return self.render_to_response(self.get_context_data(form=form))


class ApplicationView(SuccessMessageMixin, FormView):

    template_name = 'contact/application.html'
    form_class = ApplicationForm
    success_message = u'Danke wir haben Ihre Bewerbung erhalten. Sie h\u00f6ren von uns.'
    def get_context_data(self, **kwargs):
        context = super(ApplicationView, self).get_context_data(**kwargs)
        context['courseevent'] = CourseEvent.objects.get(slug="starterkurs")
        return context



    def form_valid(self, form):

        email = form.cleaned_data['email']
        name = form.cleaned_data['name']
        projecttitle = form.cleaned_data['projecttitle']
        projectdescription = form.cleaned_data['projectdescription']
        projectmotivation = form.cleaned_data['projectmotivation']
        projectqualification = form.cleaned_data['projectqualification']
        experienceoffline = form.cleaned_data['experienceoffline']
        experienceonline = form.cleaned_data['experienceonline']
        experiencetechnical = form.cleaned_data['experiencetechnical']
        comment = form.cleaned_data['comment']

        # send email to requesting email
        subject = "Ihre Bewerbung bei netTeachers"
        to = [email]
        from_mail = 'info@netteachers.de'
        context = {
            'name': name,
            'email': email,
            'projecttitle':projecttitle,
            'projectdescription':projectdescription,
            'projectmotivation':projectmotivation,
            'projectqualification':projectqualification,
            'experienceoffline':experienceoffline,
            'experienceonline':experienceonline,
            'experiencetechnical':experiencetechnical,
            'comment':comment,
            'betreff': "Ihre Bewerbung",
        }
        message = get_template('email/application_outgoing.html').render(Context(context))
        msg = EmailMessage(subject, message, to=to, from_email=from_mail)
        msg.content_subtype = 'html'
        msg.send()

        # send email to self
        subject = "Beantworten: Bewerbung fuer den netTeachers Starterkurs"
        to = ['info@netteachers.de']
        from_mail = email
        context = {
            'name': name,
            'email': email,
            'projecttitle':projecttitle,
            'projectdescription':projectdescription,
            'projectmotivation':projectmotivation,
            'projectqualification':projectqualification,
            'experienceoffline':experienceoffline,
            'experienceonline':experienceonline,
            'experiencetechnical':experiencetechnical,
            'comment':comment,
            'betreff': "Ihre Bewerbung",
        }
        message = get_template('email/application_internal.html').render(Context(context))
        msg = EmailMessage(subject, message, to=to, from_email=from_mail)
        msg.content_subtype = 'html'
        msg.send()

        return super(ApplicationView, self).form_valid(form)

    def get_success_url(self):
        return reverse('contact:answer')


class AnswerView(TemplateView):

    template_name = 'contact/answer.html'



"""
class ApplicationCreateView(SuccessMessageMixin, FormView):
    template_name = 'application/anmeldung.html'
    form_class = ApplicationForm
    success_message = u'Danke wir haben Ihre Bewerbung erhalten. Sie h\u00f6ren von uns'

    def get_success_url(self):
        pass

        try:
            application = Application.objects.get(id=self.object.id)
        except:
            return reverse('application:failed')
        else:
            mail.send(
                 application.email,
                 'info@netteachers.de',
                 template='OUT_application_confirmation',
                 context={'name': application.name,
                          'email':application.email,
                          'contact':application.contact,
                          'projecttitle':application.projecttitle,
                          'projectdescription':application.projectdescription,
                          'projectmotivation':application.projectmotivation,
                          'projectqualification':application.projectqualification,
                          'experienceoffline':application.experienceoffline,
                          'experienceonline':application.experienceonline,
                          'experiencetechnical':application.experiencetechnical,
                          'comment':application.comment,
                 },
                 priority='now',
            )
            mail.send(
                 'info@netteachers.de',
                 application.email,
                 template='IN_application_received',
                 context={'name': application.name,
                          'email':application.email,
                          'contact':application.contact,
                          'projecttitle':application.projecttitle,
                          'projectdescription':application.projectdescription,
                          'projectmotivation':application.projectmotivation,
                          'projectqualification':application.projectqualification,
                          'experienceoffline':application.experienceoffline,
                          'experienceonline':application.experienceonline,
                          'experiencetechnical':application.experiencetechnical,
                          'comment':application.comment,
                 },
                 priority='now',
            )
        return reverse('info:bewerbung')


def cancel(request):
    messages.warning(request,  "Ihre Bewerbung wurde abgebrochen. Die Daten sind nicht gespeichert.")
    return HttpResponseRedirect(reverse('info:bewerbung'))

def failed(request):
    messages.warning(request,  "Bei Ihrer Bewerbung ist ein Fehler aufgetreten. Enstchuldigen Sie, aber Ihre Daten wurden nicht gespeichert.")
    return HttpResponseRedirect(reverse('info:bewerbung'))

class ApplicationPrePageView(TemplateView):
    template_name = "application/anmeldung_vorblatt.html"

"""
