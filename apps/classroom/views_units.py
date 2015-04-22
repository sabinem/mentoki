# coding: utf-8
from __future__ import unicode_literals, absolute_import
# import from django
import logging
# import from django
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, TemplateView
from django.core.urlresolvers import reverse
# import from own app
from .mixins import ClassroomMixin
from apps.course.models import CourseUnit, CourseMaterialUnit, CourseBlock


logger = logging.getLogger(__name__)


class UnitMixin(ClassroomMixin):

    def get_context_data(self, **kwargs):
        context = super(UnitMixin, self).get_context_data(**kwargs)
        logger.debug("---------- in UnitMixin")
        try:
            unit = CourseUnit.objects.get(id=self.kwargs['unit'])
            block = CourseBlock.objects.get(id=unit.block_id)
            materials = CourseMaterialUnit.objects.filter(unit_id=unit.id).order_by('display_nr')
            context['courseblock'] = block
            context['unit'] = unit
            context['materials'] = materials
        except:
            pass
        return context


class LessonDetailView(UnitMixin, TemplateView):
    model = CourseUnit
    template_name = 'classroom_lessons/lessondetail.html'

    def get_context_data(self, **kwargs):
        logger.debug("---------- in LessonDetailView")
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        # the tab in the page is set to the course part that the user is changing
        return context


class LessonMaterialView(UnitMixin, TemplateView):

    template_name = 'classroom_lessons/lessonmaterial.html'

    def get_context_data(self, **kwargs):
        context = super(LessonMaterialView, self).get_context_data(**kwargs)
        logger.debug("---------- in LessonMaterialView get_context_data")
        coursematerial = CourseMaterialUnit.objects.select_related('unit').get(id=kwargs['material'])
        relatedmaterial = CourseMaterialUnit.objects.filter(unit_id=kwargs['unit'])
        for item in relatedmaterial:
            if item.display_nr == coursematerial.display_nr - 1:
                context['previous'] = item
            elif item.display_nr == coursematerial.display_nr + 1:
                context['next'] = item
        context['material'] = coursematerial
        return context