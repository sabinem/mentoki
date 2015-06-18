# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import TemplateView, UpdateView, ListView
from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from apps.courseevent.models import CourseeventUnitPublish

from ..mixins import AuthMenuMixin
from ..models import CourseUnit, CourseMaterialUnit, CourseBlock


class LessonsListView(AuthMenuMixin, TemplateView):
    template_name = 'course/lessons/start.html'

    def get_context_data(self, **kwargs):
        context = super(LessonsListView, self).get_context_data(**kwargs)

        published_unit_list = CourseeventUnitPublish.objects.published_unit_ids_for_course(context['course'])

        blocks = CourseBlock.objects.filter(course_id=context['course'].id).order_by('display_nr')
        block_list = []
        unit_dict = {}
        for block in blocks:
            units = CourseUnit.objects.filter(block_id=block.id).order_by('display_nr')
            unit_list =[]
            for unit in units:
                if unit.id in published_unit_list:
                    published = True
                else:
                    published = False
                unit_list.append({'unit':unit, 'published': published})
            block_list.append({'block':block, 'units':unit_list})

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
