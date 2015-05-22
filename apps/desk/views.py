# import from python
import logging
# import from django
from django.views.generic import TemplateView
# import from 3rd party apps
from braces.views import LoginRequiredMixin
# import from other apps
from apps.courseevent.models import CourseEvent
from apps.courseevent.models import CourseEventParticipation
from apps.course.models import Course, CourseOwner
from apps.core.mixins import MatchMixin


logger = logging.getLogger(__name__)


class DeskStartView(LoginRequiredMixin, MatchMixin, TemplateView):
    """
    This View is the desk. It is the main entry point for every authenticated user.
    """
    template_name = 'desk.html'

    def get_context_data(self, **kwargs):
        """
        1. all the courseevents are fetched that the user studies.
        2. all courses are fetched that the user teaches.
        3. superuser has access to everything
        """
        context = super(DeskStartView, self).get_context_data(**kwargs)
        current_user = self.request.user

        if current_user.is_superuser:
            # superuser has access to everything
            context['study_courseevents'] = CourseEvent.objects.select_related('course').\
                all().order_by('start_date')
            context['teach_courses'] = Course.objects.all()
            context['user_is_editor'] = True
        else:
            # getting the ids of the courseevent that the user paricipates in
            study_courseevent_ids = \
                CourseEventParticipation.objects.filter(user=self.request.user).\
                values_list('courseevent_id', flat=True)

            # getting courseevents and corresponding courses
            courseevents = CourseEvent.objects.select_related('course').\
                filter(id__in=study_courseevent_ids).order_by('start_date')
            context['study_courseevents'] = courseevents

            # getting the ids of the courses that the user teaches
            teach_course_ids = CourseOwner.objects.filter(user=self.request.user.id).\
                values_list('course_id', flat=True)

            #getting the courses
            courses = Course.objects.filter(id__in=teach_course_ids)
            context['teach_courses'] = courses

            if self.request.user.id in [1,2,4]:
                context['user_is_editor'] = True
            else:
                context['user_is_editor'] = False
        return context