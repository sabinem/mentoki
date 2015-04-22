# coding: utf-8
from __future__ import unicode_literals, absolute_import
# import from python
import logging
# import from django
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse
# import from own app
from .mixins import CourseBuildMixin
from .models import CourseUnit, CourseMaterialUnit, CourseBlock
from .forms_lessons import BlockForm, UnitForm, MaterialForm


#logging
logger = logging.getLogger(__name__)


class LessonUpdateMixin(CourseBuildMixin, UpdateView):

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        form.instance.course = context['course']
        return super(LessonUpdateMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            'course:lessons',
            kwargs={"slug": self.kwargs['slug']}
        )


class BlockUpdateView(LessonUpdateMixin):
    model = CourseBlock
    form_class = BlockForm
    template_name = 'lessonsupdate/blockupdate.html'
    context_object_name = 'courseblock'

    def get_object(self, queryset=None):
        logger.debug("---------- in BlockUpdateView")
        try:
            unit = CourseBlock.objects.get(id=self.kwargs['block'])
            return unit
        except:
            pass


class UnitUpdateView(LessonUpdateMixin):
    model = CourseUnit
    form_class = UnitForm
    template_name = 'lessonsupdate/unitupdate.html'
    context_object_name = 'unit'

    def get_object(self, queryset=None):
        logger.debug("---------- in UnitUpdateView")
        try:
            unit = CourseUnit.objects.get(id=self.kwargs['unit'])
            return unit
        except:
            pass

    def get_context_data(self, **kwargs):
        logger.debug("---------- in MaterialUpdateView")
        context = super(UnitUpdateView, self).get_context_data(**kwargs)
        print "*********"
        print context['unit']
        block = CourseBlock.objects.get(id=context['unit'].block_id)
        context['courseblock'] = block
        print context['courseblock']
        return context

    def get_success_url(self):
        return reverse(
            'course:blockdetail',
            kwargs={"slug": self.kwargs['slug'], 'block': self.object.block_id}
        )


class MaterialUpdateView(LessonUpdateMixin):
    model = CourseMaterialUnit
    form_class = MaterialForm
    template_name = 'lessonsupdate/materialupdate.html'
    context_object_name = 'material'

    def get_object(self, queryset=None):
        logger.debug("---------- in MaterialUpdateView")
        try:
            unit = CourseMaterialUnit.objects.get(id=self.kwargs['material'])
            return unit
        except:
            pass

    def get_context_data(self, **kwargs):
        logger.debug("---------- in MaterialUpdateView")
        context = super(MaterialUpdateView, self).get_context_data(**kwargs)
        unit = CourseUnit.objects.get(id=context['material'].unit_id)
        context['unit'] = unit
        block = CourseBlock.objects.get(id=unit.block_id)
        context['block'] = block
        return context

    def get_success_url(self):
        return reverse(
            'course:unitdetail',
            kwargs={"slug": self.kwargs['slug'], 'unit': self.object.unit_id}
        )