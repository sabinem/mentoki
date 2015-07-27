import logging
from braces.views import LoginRequiredMixin
from braces.views import MessageMixin
from apps.core.mixins import MatchMixin
from .cache import get_courseeventdata, get_participantdata
from apps_data.courseevent.models import CourseeventUnitPublish
from apps_data.course.models import CourseUnit, CourseMaterialUnit, CourseBlock


logger = logging.getLogger(__name__)


class ClassroomMixin(LoginRequiredMixin, MessageMixin, MatchMixin):

    def get_context_data(self, **kwargs):
        context = super(ClassroomMixin, self).get_context_data(**kwargs)
        logger.debug("---------- in ClassroomMixin")
        try:
            #courseeventdata are fetched
            courseeventdata = get_courseeventdata(self.kwargs['slug'])
            context['courseevent'] = courseeventdata
            courseevent_id = context['courseevent']['courseevent_id']
            course_id = context['courseevent']['course_id']

            #participantdata are fetched
            participantdata = get_participantdata(user=self.request.user,
                                              courseevent_id=courseeventdata['courseevent_id'],
                                              course_id=courseeventdata['course_id'])
            context['participant'] = participantdata
            print "hello"
            #unit-ids of units that have been published in that class are fetched in a flat list
            published_unit_list = CourseeventUnitPublish.objects.filter(
                courseevent_id=courseevent_id,
                ).values_list('unit_id', flat=True)
            #now the units are fetched by block_display_nr
            blocks = CourseBlock.objects.filter(course_id=course_id).order_by('display_nr')

            published_blocks_list = []
            for block in blocks:
                published_units = CourseUnit.objects.\
                    filter(id__in=published_unit_list, block_id=block.id).order_by('display_nr')
                if published_units:
                    published_blocks_list.append({
                        'block': block,
                        'unit_list' : published_units
                    })
            context['published_block_list'] = published_blocks_list
        except:
            pass
        return context
