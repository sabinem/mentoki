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
from ..models import Course, CourseOwner, CourseBlock
from django.shortcuts import get_object_or_404
from apps.courseevent.models import CourseEvent


class CourseBaseMixin(LoginRequiredMixin, UserPassesTestMixin, MessageMixin, MatchMixin):
    """
    this Mixin builds the menu in the side-bar and the top of the page.
    """
    def get_context_data(self, **kwargs):
        context = super(CourseBaseMixin, self).get_context_data(**kwargs)
        course = get_object_or_404(Course, slug=self.kwargs['courseprefix'])

        context['course'] = course
        context['courseevents'] = CourseEvent.objects.courseevents_for_course(course)
        context['courseblocks'] = CourseBlock.objects.courseblocks_for_course(course)

        return context


    def test_func(self, user):
        """
        This function belongs to the Braces Mixin UserPasesTest
        """
        if user.is_superuser:
            return True
        else:
            try:
                course = get_object_or_404(Course, slug=self.kwargs['courseprefix'])
                if user in course.teachers:
                    return True
            except:
                pass
        return None


class CourseBuildMixin(CourseBaseMixin):
    """
    this Mixin builds the menu in the side-bar and the top of the page.
    """


    def get_initial(self):
        """
        initial value for create forms is established
        """
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
        context = super(CourseEventBuildMixin, self).get_context_data(**kwargs)
        try:
            context['courseevent'] = CourseEvent.objects.get(slug=self.kwargs['ce_slug'])
            context['courseeventinfo'] = CourseEventPubicInformation.objects.get(courseevent_id=context['courseevent'].id)
        except:
            pass
        return context

    def get_success_url(self):
        #self.messages.success("Die Kursvorlage wurde geaendert.")
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
        courseevent = CourseEvent.objects.get(slug=self.kwargs['ce_slug'])
        courseeventinfo = CourseEventPubicInformation.objects.get(courseevent_id=courseevent.id)
        return courseeventinfo