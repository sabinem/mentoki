# coding: utf-8
# import from python
import logging
# import from django
from django.views.generic import TemplateView, UpdateView
# import from this app
from .forms_course import CourseUpdateProjectForm, CourseUpdateTextForm, CourseUpdateStructureForm, \
    CourseUpdateTargetgroupForm, CourseUpdateExcerptForm, CourseUpdatePrerequisitesForm
from .models import Course, CourseOwner
from .mixins import CourseBuildMixin
# import from python
import logging
# import from django
from django.views.generic import TemplateView, UpdateView
# import from this app
from .forms_courseevents import CourseEventUpdateExcerptForm, CourseEventUpdateWorkloadForm, \
    CourseEventUpdateFormatForm, CourseEventUpdateProjectForm, CourseEventUpdateTextForm, \
    CourseEventUpdatePrerequisitesForm, CourseEventUpdateStructureForm, CourseEventUpdateTargetgroupForm
from apps.courseevent.models import CourseEvent, CourseEventPubicInformation
from .mixins import CourseEventBuildMixin
from . models import Course


# logging
logger = logging.getLogger(__name__)


class CourseDetailView(CourseBuildMixin, TemplateView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    template_name = 'coursedescription/coursedetail.html'


class CourseUpdateTextView(CourseBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course general description
    """
    model = Course
    template_name = 'course/courseupdate.html'
    form_class = CourseUpdateTextForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseUpdateTextView")
        context = super(CourseUpdateTextView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        return context


class CourseUpdateProjectView(CourseBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course project
    """
    model = Course
    template_name = 'course/courseupdate.html'
    form_class= CourseUpdateProjectForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseUpdateTakeawayView")
        context = super(CourseUpdateProjectView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['tab'] = "Teilnehmerprojekt"
        print context
        return context


class CourseUpdateExcerptView(CourseBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course excerpt
    """
    model = Course
    template_name = 'course/courseupdate.html'
    form_class= CourseUpdateExcerptForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseUpdateExcerptView")
        context = super(CourseUpdateExcerptView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['tab'] = "Abstrakt"
        print context
        return context


class CourseUpdateStructureView(CourseBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course excerpt
    """
    model = Course
    template_name = 'course/courseupdate.html'
    form_class= CourseUpdateStructureForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseUpdateExcerptView")
        context = super(CourseUpdateStructureView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['tab'] = "Gliederung"
        print context
        return context



class CourseUpdateTargetgroupView(CourseBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course targetgroup
    """
    model = Course
    template_name = 'course/courseupdate.html'
    form_class= CourseUpdateTargetgroupForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseUpdateTargetgroupView")
        context = super(CourseUpdateTargetgroupView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['tab'] = "Zielgruppe"
        print context
        return context


class CourseUpdatePrerequisitesView(CourseBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course prerequisites
    """
    model = Course
    template_name = 'course/courseupdate.html'
    form_class= CourseUpdatePrerequisitesForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseUpdatePrerequisitesView")
        context = super(CourseUpdatePrerequisitesView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['tab'] = "Voraussetzungen"
        print context
        return context


class CourseEventDetailView(CourseEventBuildMixin, TemplateView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    template_name = 'coursedescription/courseeventdetail.html'


class CourseEventUpdateTextView(CourseEventBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course general description
    """
    model = CourseEventPubicInformation
    template_name = 'courseevent/courseeventupdate.html'
    form_class = CourseEventUpdateTextForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseEventUpdateTextView")
        context = super(CourseEventUpdateTextView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['exampletext'] = context['course'].text
        context['tab'] = "Beschreibung"
        return context

class CourseEventUpdateStructureView(CourseEventBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course general description
    """
    model = CourseEventPubicInformation
    template_name = 'courseevent/courseeventupdate.html'
    form_class = CourseEventUpdateStructureForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseEventUpdateTextView")
        context = super(CourseEventUpdateStructureView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['exampletext'] = context['course'].structure
        context['tab'] = "Gliederung"
        return context


class CourseEventUpdateProjectView(CourseEventBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course project
    """
    model = CourseEventPubicInformation
    template_name = 'courseevent/courseeventupdate.html'
    form_class= CourseEventUpdateProjectForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseEventUpdateProjectView")
        context = super(CourseEventUpdateProjectView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['exampletext'] = context['course'].project
        context['tab'] = "Teilnehmerprojekt"
        return context


class CourseEventUpdateExcerptView(CourseEventBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course excerpt
    """
    model = CourseEventPubicInformation
    template_name = 'courseevent/courseeventupdate.html'
    form_class= CourseEventUpdateExcerptForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseEventUpdateExcerptView")
        context = super(CourseEventUpdateExcerptView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['exampletext'] = context['course'].excerpt
        context['tab'] = "Abstrakt"
        return context

    def get_object(self, queryset=None):
        courseevent = CourseEvent.objects.get(slug=self.kwargs['ce_slug'])
        return courseevent


class CourseEventUpdateFormatView(CourseEventBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course targetgroup
    """
    model = CourseEventPubicInformation
    template_name = 'courseevent/courseeventupdate.html'
    form_class= CourseEventUpdateFormatForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseEventUpdateFormatView")
        context = super(CourseEventUpdateFormatView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['exampletext'] = "Es gibt keine Vorlage dafür."
        context['tab'] = "Kursformat"
        return context


class CourseEventUpdateWorkloadView(CourseEventBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course prerequisites
    """
    model = CourseEventPubicInformation
    template_name = 'courseevent/courseeventupdate.html'
    form_class= CourseEventUpdateWorkloadForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseEventUpdatePrerequisitesView")
        context = super(CourseEventUpdateWorkloadView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['exampletext'] = "Es gibt keine Vorlage dafür."
        context['tab'] = "Arbeitsbelastung"
        return context


class CourseEventUpdateTargetgroupView(CourseEventBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course prerequisites
    """
    model = CourseEventPubicInformation
    template_name = 'courseevent/courseeventupdate.html'
    form_class= CourseEventUpdateTargetgroupForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseEventUpdateTargetgroupView")
        context = super(CourseEventUpdateTargetgroupView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['exampletext'] = context['course'].target_group
        context['tab'] = "Zielgruppe"
        return context


class CourseEventUpdatePrerequisitesView(CourseEventBuildMixin, UpdateView):
    """
    Here course owner can update the information on the course prerequisites
    """
    model = CourseEventPubicInformation
    template_name = 'courseevent/courseeventupdate.html'
    form_class= CourseEventUpdatePrerequisitesForm

    def get_context_data(self, **kwargs):
        logger.debug("---------- in CourseEventUpdatePrerequisitesView")
        context = super(CourseEventUpdatePrerequisitesView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        context['exampletext'] = context['course'].prerequisites
        context['tab'] = "Vorasusetzungen"
        return context

