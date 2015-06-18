# import from python
import logging
# import from django
from django.views.generic import TemplateView
# from other apps
from apps.courseevent.models import CourseEventParticipation, CourseEvent
# import from this app
from .mixins import CourseBuildMixin


# logging
logger = logging.getLogger(__name__)


class CourseParticipantsListView(CourseBuildMixin, TemplateView):
    """
    Owners of the course are listed
    """
    template_name = 'participant/participantslist.html'

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CoursedParticipantsListView")
        context = super(CourseParticipantsListView, self).get_context_data(**kwargs)
        courseevent = CourseEvent.objects.get(slug=kwargs['slug'])
        context['courseevent'] = courseevent
        # course owners are selected together with their user data
        participants = CourseEventParticipation.objects.select_related('user').filter(courseevent_id=courseevent.id)
        # the context are the owners informations
        context['participants'] = participants
        try:
            # get courseevent from slug
            courseevent = CourseEvent.objects.get(slug=kwargs['slug'])
            context['courseevent'] = courseevent
            # course owners are selected together with their user data
            participants = CourseEventParticipation.objects.select_related('user').filter(courseevent_id=courseevent.id)
            # the context are the owners informations
            context['participants'] = participants
        except:
            pass
        print context['participants']
        print context['courseevent']
        return context

