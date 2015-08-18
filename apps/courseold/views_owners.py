# coding: utf-8
# import from python
import logging
# import from django
from django.views.generic import TemplateView, UpdateView
from django.core.urlresolvers import reverse
# import from this app
from .forms_owner import CourseOwnerUpdateForm
from .models import Course, CourseOwner
from .mixins import CourseBuildMixin


# logging
logger = logging.getLogger(__name__)


class CourseOwnersListView(CourseBuildMixin, TemplateView):
    """
    Owners of the course are listed
    """
    template_name = 'owner/ownerslist.html'

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CoursedOwnersListView")
        context = super(CourseOwnersListView, self).get_context_data(**kwargs)
        # course owners are selected together with their user data
        owners = CourseOwner.objects.select_related('user').filter(course_id=context['course'].id).order_by('display_nr')
        # the context are the owners informations
        context['owners'] = owners
        return context


class CourseOwnerUpdateView(CourseBuildMixin, UpdateView):
    """
    Information of the user in relation to the course can be updated here.
    """
    model = CourseOwner
    form_class = CourseOwnerUpdateForm
    template_name = 'owner/ownerupdate.html'
    context_object_name = 'owner'

    def get_success_url(self):
        """
        The user return to the courseowner list after editing the course owner information
        """
        logger.debug("---------- in CourseUpdateUpdateView get_success_url")
        return reverse(
            'course:ownerslist',
            kwargs={"slug": self.kwargs['slug'],
        })

    def get_object(self, queryset=None):
        """
        Course and Course owner are fetched along with the user information.
        """
        logger.debug("---------- in CourseUpdateUpdateView get_object")
        course = Course.objects.get(slug=self.kwargs['slug'])
        owner = CourseOwner.objects.select_related('user').get(course_id=course.id, user=self.kwargs['user'])
        return owner
