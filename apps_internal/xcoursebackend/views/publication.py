import datetime
import pytz
import logging
# import from django
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse
from apps.courseevent.models import CourseeventUnitPublish, CourseEvent
from apps.course.models import CourseUnit
from apps.core.validators import get_current_time
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from .mixins import CourseEventBuildMixin
from .models import CourseBlock


logger = logging.getLogger(__name__)


class LessonsPublishView(CourseEventBuildMixin, TemplateView):
    template_name = 'lessonspublish/publishlessons.html'

    def get_context_data(self, **kwargs):
        context = super(LessonsPublishView, self).get_context_data(**kwargs)
        logger.debug("---------- in LessonsListView")
        published_id_list = CourseeventUnitPublish.objects.filter(
           courseevent_id=context['courseevent'].id,
           ).values_list('unit_id', flat=True)

        blocks = CourseBlock.objects.filter(course_id=context['course'].id).order_by('display_nr')
        block_list = []
        for block in blocks:
            print block
            units = CourseUnit.objects.filter(block_id=block.id).select_related('block')
            unit_list = []
            for unit in units:
                if unit.id in published_id_list:
                    publication = CourseeventUnitPublish.objects.get(
                       courseevent_id=context['courseevent'].id,
                       unit_id = unit.id,
                    )
                    unit_list.append({
                        'unit': unit,
                        'publication': publication,
                        'published': True
                    })
                else:
                    unit_list.append({
                        'unit': unit,
                        'publication': None,
                        'published': False
                    })
            print unit_list
            block_list.append({'block':block, 'units':unit_list})
        for item in block_list:
            print item['block']
            for x in item['units']:
                print x
        context['blocks'] = block_list
        return context

def create_publication(request, ce_slug, slug, unit):
    try:
        courseevent = CourseEvent.objects.get(slug=ce_slug)
        unit = CourseUnit.objects.get(id=unit)
        CourseeventUnitPublish.objects.create(unit=unit, courseevent=courseevent)
        messages.success(request, "Die Lektion wurde freigeschaltet.")
        return HttpResponseRedirect(reverse('course:publishlessons',
                                            kwargs={'ce_slug':ce_slug, 'slug':slug}))
    except CourseEvent.DoesNotExist:
        raise Http404

def delete_publication(request, ce_slug, slug, unit):
    try:
        publication = CourseeventUnitPublish.objects.get(unit_id=unit)
        courseevent = CourseEvent.objects.get(slug=ce_slug)
        publication.delete()
        messages.success(request, "Die Lektion wurde gesperrt.")
        return HttpResponseRedirect(reverse('course:publishlessons',
                                            kwargs={'ce_slug':ce_slug, 'slug': slug}))
    except CourseEvent.DoesNotExist:
        raise Http404








