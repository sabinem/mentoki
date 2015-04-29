from django.views.generic import ListView, DetailView, TemplateView
from .models import CourseEvent, CourseEventParticipation
from apps.course.models import Course, CourseOwner
from apps.core.mixins import MatchMixin
from apps.classroom.cache import get_courseeventdata
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.
class CourseEventListView(MatchMixin, TemplateView):
    """
    This View is the homepage. It offers a simple search form, where the user can search
    for courses by title. He is then redirected to the searchpage with that input.
    """

    template_name = 'public/courseevent_list.html'

    def get_context_data(self, **kwargs):
        context = super(CourseEventListView, self).get_context_data()
        courseevents = CourseEvent.objects.filter(status_external=CourseEvent.EVENT_OPEN_FOR_BOOKING)
        courseevent_list = []
        for courseevent in courseevents:
            courseeventdata = get_courseeventdata(courseevent.slug)

            courseevent_list.append({'courseevent': courseevent,
                                     'courseevent_teachers': courseeventdata['courseevent_teachers'],
                                     })
        context['courseevent_list'] = courseevent_list
        return context


class CourseEventDetailView(MatchMixin, TemplateView):
    """
    This View shows the details for a courseevents
    """

    template_name = "public/courseevent_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CourseEventDetailView, self).get_context_data()
        courseevent = CourseEvent.objects.get(slug=kwargs['slug'])
        course = Course.objects.get(id=courseevent.course_id)
        courseowners = CourseOwner.objects.filter(course_id=course.id)
        context['courseevent'] = courseevent
        context['course']=course
        context['courseowners'] = courseowners
        print (context)
        return context


# Create your views here.
class CourseEventInternalListView(MatchMixin, TemplateView):
    """
    This View is the homepage. It offers a simple search form, where the user can search
    for courses by title. He is then redirected to the searchpage with that input.
    """

    template_name = 'internal/courseevent_list.html'

    def get_context_data(self, **kwargs):
        context = super(CourseEventInternalListView, self).get_context_data()
        courseevents = CourseEvent.objects.exclude(slug="starterkurs").filter(status_external=CourseEvent.EVENT_UNPUBLISHED)
        participation = CourseEventParticipation.objects.filter(user=self.request.user).values_list('courseevent_id', flat=True)
        participation_list = list(set(participation))
        courseowner = CourseOwner.objects.filter(user=self.request.user).values_list('course_id', flat=True)
        courseowner_list = list(set(courseowner))

        courseevent_list = []
        for courseevent in courseevents:
            courseeventdata = get_courseeventdata(courseevent.slug)
            is_participant = False
            is_owner = False
            if courseevent.course_id in courseowner_list:
                is_owner = True
            if courseevent.id in participation_list:
                is_participant = True

            courseevent_dict = {'courseevent': courseevent,
                                     'courseevent_teachers': courseeventdata['courseevent_teachers'],
                                     'is_participant': is_participant,
                                     'is_owner': is_owner,
                                     }

            courseevent_list.append(courseevent_dict)

        context['courseevent_list'] = courseevent_list
        return context




class CourseEventInternalDetailView(MatchMixin, TemplateView):
    """
    This View shows the details for a courseevents.
    """

    template_name = "internal/courseevent_detail.html"

    def get_context_data(self, **kwargs):

        context = super(CourseEventInternalDetailView, self).get_context_data()

        courseevent = CourseEvent.objects.get(slug=kwargs['slug'])
        is_participant = True
        is_owner = True


        try:

            participation = CourseEventParticipation.objects.get(user=self.request.user, courseevent=courseevent)

        except:
            is_participant = False
        try:
            owner = CourseOwner.objects.get(user=self.request.user, course=courseevent.course)
        except:
            is_owner = False

        course = Course.objects.get(id=courseevent.course_id)
        courseowners = CourseOwner.objects.filter(course_id=course.id)
        context['courseevent'] = courseevent
        context['course']=course
        context['courseowners'] = courseowners
        context['is_owner'] = is_owner
        context['is_participant'] = is_participant

        print (context)
        return context


def bookcourse(request, slug):
    courseevent = CourseEvent.objects.get(slug=slug)
    user = request.user
    try:
        CourseEventParticipation.objects.get(user=user,courseevent=courseevent)
    except:
        CourseEventParticipation(user=user,courseevent=courseevent).save()

    return HttpResponseRedirect(reverse('desk:start'))

