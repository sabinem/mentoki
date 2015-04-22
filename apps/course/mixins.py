# import from python
import logging
# import from django
from apps.core.mixins import MatchMixin
from django.core.urlresolvers import reverse
# import from 3rd party apps
from braces.views import LoginRequiredMixin, MessageMixin, UserPassesTestMixin
# import from other apps
from apps.courseevent.models import CourseEvent, CourseEventPubicInformation
# import from this app
from .models import Course, CourseOwner, CourseBlock


# logging
logger = logging.getLogger(__name__)


class CourseBaseMixin(LoginRequiredMixin, UserPassesTestMixin, MessageMixin, MatchMixin):
    """
    this Mixin builds the menu in the side-bar and the top of the page.
    """
    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseBaseMixin get_context_data")
        context = super(CourseBaseMixin, self).get_context_data(**kwargs)
        try:
            # The course is needed to get the course id
            course = Course.objects.get(slug=self.kwargs['slug'])
            context['course'] = course
            # The courseevents are needed for the menu
            context['courseevents'] = CourseEvent.objects.filter(course_id=course.id)
            try:
                # The blocks are needed for the menu
                context['courseblocks'] = CourseBlock.objects.filter(course_id=course.id)
                # it is checked whether the courseowners description is ready
                courseowners = CourseOwner.objects.filter(course_id=course.id)
                context['courseowners']=courseowners
                status_owners_ready = True
                for owner in courseowners:
                    if owner.status == owner.STATUS_DRAFT:
                        status_owners_ready = False
                context['status_owners_ready']=status_owners_ready
            except:
                pass
        except:
            pass
        return context

    def test_func(self, user):
        """
        This function belongs to the Braces Mixin UserPasesTest only the superuser and owner
        of this course are allowed in this section of the website, where the course is build.
        :param user:
        :return: True is user is allowed, else None is returned.
        """
        logger.debug("---------- in CourseBaseMixin test_func")
        if user.is_superuser:
            return True
        try:
            # The course id is needed
            course = Course.objects.get(slug=self.kwargs['slug'])
            # if there is an entry in owners for this user and the course id, the user is owner of this course.
            owners = CourseOwner.objects.filter(course_id=course.id).values_list('user_id', flat=True)
            print owners
            if user.id in owners:
                return True
        except:
            return None



class CourseBuildMixin(CourseBaseMixin):
    """
    this Mixin builds the menu in the side-bar and the top of the page.
    """

    def get_success_url(self):
        logger.debug("---------- in CourseBuildMixin get_success_url")
        self.messages.success("Die Kursvorlage wurde geaendert.")
        return reverse('course:start', kwargs={"slug": self.kwargs['slug'],})

    def get_initial(self):
        """
        initial value for create forms is established
        """
        logger.debug("---------- in CourseBuildMixin get_initial")
        initials = super(CourseBuildMixin, self).get_initial()
        try:
            course = Course.objects.get(slug=self.kwargs['slug'])
            initials['course_id'] = course.id
        except:
            pass
        return initials

    def form_valid(self, form, **kwargs):
        """
        The course id is a hidden attribute in any course part, that has to be set.
        """
        context = self.get_context_data(**kwargs)
        try:
            form.instance.course = context['course']
        except:
            pass
        return super(CourseBuildMixin, self).form_valid(form)


class CourseEventBuildMixin(CourseBaseMixin):
    """
    this Mixin builds the menu in the side-bar and the top of the page.
    """
    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseEventBuildMixin get_context_data")
        context = super(CourseEventBuildMixin, self).get_context_data(**kwargs)
        try:
            context['courseevent'] = CourseEvent.objects.get(slug=self.kwargs['ce_slug'])
        except:
            pass
        return context

    def get_success_url(self):
        logger.debug("---------- in CourseBuildMixin get_success_url")
        self.messages.success("Die Kursvorlage wurde geaendert.")
        return reverse('course:courseevent', kwargs={
            "slug": self.kwargs['slug'],
            "ce_slug": self.kwargs['ce_slug']
            })


    def form_valid(self, form, **kwargs):
        """
        The course id is a hidden attribute in any course part, that has to be set.
        """
        context = self.get_context_data(**kwargs)
        try:
            form.instance.course = context['course']
        except:
            pass
        return super(CourseEventBuildMixin, self).form_valid(form)

    def get_object(self, queryset=None):
        """
        Course and Course owner are fetched along with the user information.
        """
        courseevent = CourseEvent.objects.get(slug=self.kwargs['ce_slug'])
        courseeventinfo = CourseEventPubicInformation.objects.get(courseevent_id=courseevent.id)
        return courseevent
