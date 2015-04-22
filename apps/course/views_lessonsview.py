# coding: utf-8
from __future__ import unicode_literals, absolute_import
# import from python
import logging
# import from django
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, TemplateView
from django.core.urlresolvers import reverse
# import from own app
from .mixins import CourseBuildMixin
from .models import CourseUnit, CourseMaterialUnit, CourseBlock


#logging
logger = logging.getLogger(__name__)


class LessonsView(CourseBuildMixin, TemplateView):
    template_name = 'lessonsview/start.html'

    def get_context_data(self, **kwargs):
        """
        A list of the complete material for a block is build in a way where the units are
        paired with their material
        """
        context = super(LessonsView, self).get_context_data(**kwargs)
        blocks = CourseBlock.objects.filter(course_id=context['course'].id).order_by('display_nr')
        block_list = []
        unit_dict = {}
        for block in blocks:
            units = CourseUnit.objects.filter(block_id=block.id).order_by('display_nr')
            block_list.append({'block':block, 'units':units})

        context['block_list'] = block_list
        logger.debug("---------- in BlockDetailView")
        return context


class BlockDetailView(CourseBuildMixin, TemplateView):
    template_name = 'lessonsview/blockdetail.html'

    def get_context_data(self, **kwargs):
        """
        A list of the complete material for a block is build in a way where the units are
        paired with their material
        """
        context = super(BlockDetailView, self).get_context_data(**kwargs)
        block = CourseBlock.objects.get(id=kwargs['block'])
        context['courseblock'] = block
        units = CourseUnit.objects.filter(block_id=self.kwargs['block']).\
            order_by('display_nr')
        unit_list = []
        for unit in units:
            materials = CourseMaterialUnit.objects.filter(unit_id=unit.id).\
                order_by('display_nr')
            unit_list.append({'unit':unit, 'materials':materials})
        context['unit_list'] = unit_list
        logger.debug("---------- in BlockDetailView")
        return context


class UnitDetailView(CourseBuildMixin, TemplateView):
    template_name = 'lessonsview/unitdetail.html'

    def get_context_data(self, **kwargs):
        """
        A list of the complete material for a block is build in a way where the units are
        paired with their material
        """
        context = super(UnitDetailView, self).get_context_data(**kwargs)
        unit = CourseUnit.objects.get(id=self.kwargs['unit'])
        context['courseblock'] = CourseBlock.objects.get(id=unit.block_id)
        context['unit'] = unit
        materials = CourseMaterialUnit.objects.filter(unit_id=unit.id).order_by('display_nr')
        context['materials'] = materials
        logger.debug("---------- in UnitDetailView")
        return context


class MaterialDetailView(CourseBuildMixin, TemplateView):
    template_name = 'lessonsview/materialdetail.html'

    def get_context_data(self, **kwargs):
        """
        A list of the complete material for a block is build in a way where the units are
        paired with their material
        """
        context = super(MaterialDetailView, self).get_context_data(**kwargs)
        material = CourseMaterialUnit.objects.get(id=self.kwargs['material'])
        unit = CourseUnit.objects.get(id=material.unit_id)
        context['unit'] = unit
        context['courseblock'] = CourseBlock.objects.get(id=unit.block_id)
        context['material'] = material
        logger.debug("---------- in MaterialDetailView")
        return context
