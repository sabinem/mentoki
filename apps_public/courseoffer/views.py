# import from python
import logging
# import from django
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# import from 3rd party apps
from braces.views import LoginRequiredMixin, UserPassesTestMixin
# import from other apps
from apps_internal.classroom.cache import get_courseeventdata
from apps_data.course.models import Course, CourseOwner
# import from this app
from apps_data.courseevent.models import CourseEvent, CourseEventParticipation, CourseEventPubicInformation


class CourseOfferListView(TemplateView):
    template_name = 'courseoffer/list/courseevent_list.html'

    def get_context_data(self, **kwargs):
        """
        Events that are open for booking are shown. Also previews are shown as coming soon
        """
        context = super(CourseOfferListView, self).get_context_data()

        # build list of course events
        context['courseevents_now'] = CourseEvent.public_ready_for_booking.all()
        context['courseevents_preview'] = CourseEvent.public_ready_for_preview.all()

        return context


class CourseOfferDetailView(TemplateView):
    """
    This View shows the details of a courseevents. From here you can book them, if they are
    available for booking yet.
    """
    template_name = "courseoffer/detail/courseevent_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CourseOfferDetailView, self).get_context_data()

        context['courseevent'] = CourseEvent.objects.get_courseevent_or_404_from_slug(slug=kwargs['slug'])
        context['teachersinfo'] = CourseOwner.objects.teachers_courseinfo(course=context['courseevent'].course)

        return context