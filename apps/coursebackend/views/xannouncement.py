import datetime
import pytz
from apps.core.validators import get_current_time
import logging
# import from django
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse
# import from own app
from ..forms import AnnouncementCreateForm, AnnouncementUpdateForm
from apps.classroom.models import Announcement
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.template import Context
from apps.courseevent.models import CourseEventParticipation
from apps.course.models import CourseOwner
from .mixins import CourseEventBuildMixin


logger = logging.getLogger(__name__)


class AnnouncementMixin(CourseEventBuildMixin):

    def get_success_url(self):
        logger.debug("---------- in AnnouncementMixin get_success_url")
        return reverse(
            'course:listannouncements',
            kwargs={"slug": self.kwargs['slug'],
                    "ce_slug": self.kwargs['ce_slug']}
        )

    def get_object(self, queryset=None):
        logger.debug("---------- in AnnouncementMixin get_object")
        announcement = Announcement.objects.get(id=self.kwargs['announcement'])
        return announcement

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        form.instance.courseevent = context['courseevent']
        if form.instance.published == True:

            form.instance.published_at_date = datetime.datetime.now()

            participants = CourseEventParticipation.objects.filter(courseevent=context['courseevent'].id).select_related('user')
            owners = CourseOwner.objects.filter(course=context['course'].id).select_related('user')

            # send email to requesting email
            subject = "Neue Nachricht von Mentoki %s" % context['courseevent'].title
            to_list = []
            for participant in participants:
                to_list.append(participant.user.email)
            for owner in owners:
                to_list.append(owner.user.email)
            to = to_list
            from_mail = context['course'].email

            context = {
                'courseevent': context['courseevent'],
                'title': form.cleaned_data['title'],
                'text': form.cleaned_data['text'],
                'owners': owners,
                'betreff': subject,
            }
            message = get_template('email/announcement.html').render(Context(context))
            msg = EmailMessage(subject, message, to=to, from_email=from_mail)
            msg.content_subtype = 'html'
            msg.send()
            self.messages.success(u"Die Ank\u00fcndigung wurde an die Teilnehmer %s verschickt." % to )
        else:
            self.messages.success(u"Die Ank\u00fcndigung wurde als Entwurf gespeichert." )

        return super(AnnouncementMixin, self).form_valid(form)



class AnnouncementsListView(AnnouncementMixin, TemplateView):
    template_name = 'announcements/announcements.html'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementsListView, self).get_context_data(**kwargs)
        logger.debug("---------- in AnnouncementsListView get_context_data")
        announcements_unpublished = Announcement.objects.filter(
            courseevent = context['courseevent'].id,
            published=False,
        )
        announcements_published = Announcement.objects.filter(
            courseevent = context['courseevent'].id, published=True)\
            .order_by('-published_at_date')
        context ['announcements_published'] = announcements_published
        context ['announcements_unpublished'] = announcements_unpublished

        return context


class AnnouncementCreateView(AnnouncementMixin, CreateView):
    form_class = AnnouncementCreateForm
    template_name = 'announcements/announcementcreate.html'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementCreateView, self).get_context_data(**kwargs)
        return context



class AnnouncementUpdateView(AnnouncementMixin, UpdateView):
    model = Announcement
    form_class = AnnouncementUpdateForm
    template_name = 'announcements/announcementupdate.html'



class AnnouncementDeleteView(AnnouncementMixin, DeleteView):
    model = Announcement
    template_name = 'announcements/announcementdelete.html'

    def get_success_url(self):
        self.messages.success("Die Ankuendigung wurde geloescht.")
        return super(AnnouncementDeleteView, self).get_success_url()

