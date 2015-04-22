import logging
from braces.views import LoginRequiredMixin
from braces.views import MessageMixin
from apps.core.mixins import MatchMixin
from .cache import get_courseeventdata, get_participantdata
from apps.courseevent.models import CourseeventUnitPublish
from apps.course.models import CourseUnit, CourseMaterialUnit, CourseBlock


logger = logging.getLogger(__name__)


class ClassroomMixin(LoginRequiredMixin, MessageMixin, MatchMixin):

    def get_context_data(self, **kwargs):
        context = super(ClassroomMixin, self).get_context_data(**kwargs)
        logger.debug("---------- in ClassroomMixin")
        try:
            courseeventdata = get_courseeventdata(self.kwargs['slug'])
            participantdata = get_participantdata(user=self.request.user,
                                              courseevent_id=courseeventdata['courseevent_id'],
                                              course_id=courseeventdata['course_id'])
            context['courseevent'] = courseeventdata
            context['participant'] = participantdata
            courseevent_id = context['courseevent']['courseevent_id']
            course_id = context['courseevent']['course_id']
            published_unit_list = CourseeventUnitPublish.objects.filter(
                courseevent_id=courseevent_id,
                ).values_list('unit_id', flat=True)
            published_units = CourseUnit.objects.select_related('block').\
                filter(id__in=published_unit_list).order_by('block__display_nr')
            published_blocks_list = []
            current_block_id = None
            for unit in published_units:
                if current_block_id != unit.block_id:
                    if current_block_id != None:
                        published_blocks_list.append({
                            'block': current_block,
                            'unit_list' : current_unit_list
                        })
                    current_block_id = unit.block_id
                    current_block = unit.block
                    current_unit_list = []
                current_unit_list.append(unit)
            published_blocks_list.append({
                            'block': current_block,
                            'unit_list' : current_unit_list
                        })
            context['published_block_list'] = published_blocks_list
        except:
            pass
        return context
