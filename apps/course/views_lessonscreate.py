# coding: utf-8
from __future__ import unicode_literals, absolute_import
# import from python
import logging
# import from django
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
# import from own app
from .mixins import CourseBuildMixin
from .models import CourseUnit, CourseMaterialUnit, CourseBlock
from .forms_lessons import BlockForm, UnitForm, MaterialForm


#logging
logger = logging.getLogger(__name__)


class LessonCreateMixin(CourseBuildMixin, CreateView):

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        form.instance.course = context['course']
        return super(LessonCreateMixin, self).form_valid(form)


class BlockCreateView(LessonCreateMixin):
    model = CourseBlock
    form_class = BlockForm
    template_name = 'lessonscreate/blockcreate.html'
    context_object_name = 'courseblock'

    def get_success_url(self):
        return reverse(
            'course:lessons',
            kwargs={"slug": self.kwargs['slug']}
        )


class UnitCreateView(LessonCreateMixin):
    model = CourseUnit
    form_class = UnitForm
    template_name = 'lessonscreate/unitcreate.html'
    context_object_name = 'unit'

    def get_success_url(self):
        return reverse(
            'course:blockdetail',
            kwargs={"slug": self.kwargs['slug'], 'block': self.object.block_id}
        )


class MaterialCreateView(LessonCreateMixin):
    model = CourseMaterialUnit
    form_class = MaterialForm
    template_name = 'lessonscreate/materialcreate.html'
    context_object_name = 'material'

    def get_success_url(self):
        return reverse(
            'course:unitdetail',
            kwargs={"slug": self.kwargs['slug'], 'unit': self.object.unit_id}
        )