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


class InternalCourseEventBookingMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Mixin for internal courseevent bookings
    """

    def test_func(self, user):
        """
        This function belongs to the Braces Mixin UserPasesTest only the superuser and
        other courseowners are allowed for the internal booking of a course.
        """
        logger.debug("---------- in InternalCourseEventBookingMixin test_func")
        if user.is_superuser:
            return True
        try:
            # if the user is also a courseowner he may book a cour internally
            owner = CourseOwner.objects.filter(user=user)
            if owner:
                return True
        except:
            return None


class CourseEventInternalListView(InternalCourseEventBookingMixin, TemplateView):
    """
    This View shows all courseevents that are possible for internal booking
    !!! This function uses the cache of courseevent teachers.
    """
    template_name = 'internal/courseevent_list.html'

    def get_context_data(self, **kwargs):
        """
        Events that are open for internal booking are shown.
        Other teachers may book them in order to provide feedback.
        """
        context = super(CourseEventInternalListView, self).get_context_data()
        # get all courseevents that are open for internal booking
        # the course data are also fetched
        try:
            courseevents = CourseEvent.objects.filter(status_internal=CourseEvent.INTEVENT_OPEN,
                                                      slug=kwargs['slug']).\
                                                      select_related('course')
        except:
            courseevents = CourseEvent.objects.filter(status_internal=CourseEvent.INTEVENT_OPEN).\
                select_related('course')

        # build list of course events
        courseevent_list = []
        for courseevent in courseevents:

            # get courseevent teachers from cache
            courseeventdata = get_courseeventdata(courseevent.slug)
            courseevent_dict = {'courseevent': courseevent,
                                'courseevent_teachers': courseeventdata['courseevent_teachers'],
            }
            courseevent_list.append(courseevent_dict)
        context['courseevent_list'] = courseevent_list

        return context


class CourseEventInternalDetailView(InternalCourseEventBookingMixin, TemplateView):
    """
    This View shows the details for a courseevents.
    """
    template_name = "internal/courseevent_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CourseEventInternalDetailView, self).get_context_data()
        # the coursevent is determind by the given url
        try:
            courseevent = CourseEvent.objects.get(slug=kwargs['slug'])
            context['courseevent'] = courseevent
            courseevent_info = CourseEventPubicInformation.objects.get(courseevent_id=courseevent.id)
            context['courseevent_info'] = courseevent_info
            # get course
            course = Course.objects.get(id=courseevent.course_id)
            context['course'] = course
            # get teachers
            courseowners = CourseOwner.objects.filter(course_id=courseevent.course_id)
            context['courseowners'] = courseowners
        except:
            # fail silently
            pass

        # determine the role of the current user regarding the coursevent
        try:
            participation = \
                CourseEventParticipation.objects.get(user=self.request.user, courseevent=courseevent)
            user_is_participant = True
        except:
            user_is_participant = False
        context['user_is_participant'] = user_is_participant
        try:
            owner = CourseOwner.objects.get(user=self.request.user, course=courseevent.course)
            user_is_teacher = True
        except:
            user_is_teacher = False
        context['user_is_teacher'] = user_is_teacher

        return context


def bookcourse(request, slug):
    """
    makes an internal booking for a course: it creates a record in courseevent_participation
    it redirects to the desk, where the new record ist visible.
    """
    courseevent = CourseEvent.objects.get(slug=slug)
    user = request.user
    # if the record already exists nothing is done, otherwise a new participation record is created.
    try:
        CourseEventParticipation.objects.get(user=user,courseevent=courseevent)
    except:
        CourseEventParticipation(user=user,courseevent=courseevent).save()
    # next page is the desk, where the new course is visible.
    return HttpResponseRedirect(reverse('desk:start'))

