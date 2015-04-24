# import from python
import logging
# import from django
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# import from 3rd party apps
from braces.views import LoginRequiredMixin, UserPassesTestMixin
# import from other apps
from apps.classroom.cache import get_courseeventdata
from apps.course.models import Course, CourseOwner
# import from this app
from .models import CourseEvent, CourseEventParticipation, CourseEventPubicInformation


# logging
logger = logging.getLogger(__name__)


class CourseEventListView(TemplateView):
    """
    All public courseevents are shown in order for the user to book.
    !!! This function uses the cache of courseevent teachers.
    """
    template_name = 'public/courseevent_list.html'

    def get_context_data(self, **kwargs):
        """
        Events that are open for booking are shown. Also previews are shown as coming soon
        """
        context = super(CourseEventListView, self).get_context_data()
        # get all courseevents that are open for booking or preview
        # the course data is also fetched
        courseevent_extevent = [CourseEvent.EXTEVENT_OPEN_FOR_BOOKING, CourseEvent.EXTEVENT_PREVIEW]
        courseevents = CourseEvent.objects.filter(status_external__in=courseevent_extevent).\
            select_related('course')

        # build list of course events
        courseevent_list_now = []
        courseevent_list_preview = []
        for courseevent in courseevents:

            # get courseevent teachers from cache
            courseeventdata = get_courseeventdata(courseevent.slug)
            courseevent_dict = {'courseevent': courseevent,
                                'courseevent_teachers': courseeventdata['courseevent_teachers'],
            }
            if courseevent.status_external == CourseEvent.EXTEVENT_OPEN_FOR_BOOKING:
                courseevent_list_now.append(courseevent_dict)
            elif courseevent.status_external == CourseEvent.EXTEVENT_PREVIEW:
                courseevent_list_preview.append(courseevent_dict)
        context['courseevent_list_now'] = courseevent_list_now
        context['courseevent_list_preview'] = courseevent_list_preview

        return context


class CourseEventDetailView(TemplateView):
    """
    This View shows the details of a courseevents. From here you can book them, if they are
    available for booking yet.
    """
    template_name = "public/courseevent_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CourseEventDetailView, self).get_context_data()
        # the coursevent is determind by the given url
        try:
            courseevent = CourseEvent.objects.get(slug=kwargs['slug'])
            courseevent_info = CourseEventPubicInformation.objects.get(courseevent_id=courseevent.id)
            context['courseevent_info'] = courseevent_info
            context['courseevent'] = courseevent
            # get course
            course = Course.objects.get(id=courseevent.course_id)
            context['course'] = course
            # get teachers
            courseowners = CourseOwner.objects.filter(course_id=courseevent.course_id)
            context['courseowners'] = courseowners.order_by('display_nr')
        except:
            # fail silently
            pass
        return context