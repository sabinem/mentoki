import logging
from apps.course.models import Course, CourseOwner
from apps.courseevent.models import CourseEvent
from apps.courseevent.models import CourseEventParticipation
from apps.forum.models import Forum
from apps.core.cache import get_cachedata, set_flag_recalc_cache
from apps.core.cacheconfig import *


logger = logging.getLogger(__name__)


def get_participantdata(user,courseevent_id,course_id):
    logger.debug("---------- in get_particpantdata")
    cache_data = get_cachedata(
        data = {'courseevent_id': courseevent_id, 'user':user, 'course_id':course_id},
        data_id = str(courseevent_id) + str(user.id),
        flagcode = CACHE_FLAG_PARTICIPANT,
        datacode = CACHE_DATA_PARTICIPANT,
        function = calc_participantdata
    )
    return cache_data


def get_courseeventdata(slug):
    logger.debug("---------- in get_courseeventdata")
    cache_data = get_cachedata(
        data = slug,
        data_id = slug,
        flagcode = CACHE_FLAG_CLASSROOM,
        datacode = CACHE_DATA_CLASSROOM,
        function = calc_courseeventdata
    )
    return cache_data


def recalc_participantdata(user_id,courseevent_id):
    logger.debug("---------- in recalc_particpantdata")
    return set_flag_recalc_cache(
        data_id = str(courseevent_id) + str(user_id),
        flagcode = CACHE_FLAG_PARTICIPANT,
        datacode = CACHE_DATA_PARTICIPANT,
        function = calc_participantdata
    )


def recalc_courseeventdata(slug):
    logger.debug("---------- in recalc_courseeventdata")
    return set_flag_recalc_cache(
        data_id = slug,
        flagcode = CACHE_FLAG_CLASSROOM,
        datacode = CACHE_DATA_CLASSROOM,
        function = calc_courseeventdata
    )


def calc_courseeventdata(slug):
            logger.debug("---------- in calc_courseeventdata")
            courseevent = CourseEvent.objects.get(slug=slug)
            course = Course.objects.get(id=courseevent.course_id)
            # the teacher for the courseevent are fetched
            teachers = CourseOwner.objects.select_related('user').filter(course_id=course.id)
            namesstring = ""
            for teacher in teachers:
                namesstring += u'%s %s ' % (teacher.user.first_name, teacher.user.last_name)

            courseevent_teachers = namesstring

            forum = Forum.objects.get(courseevent=courseevent.id)

            courseeventdata = {
                'courseevent_id':courseevent.id,
                'courseevent_title':courseevent.title,
                'course_id':course.id,
                'course_slug':course.slug,
                'course_title':course.title,
                'courseevent_teachers':courseevent_teachers,
                'forum_id':forum.id,
            }
            return courseeventdata


def calc_participantdata(dict):
        logger.debug("---------- in calc_participantdata")
        try:
            courseeventparticipation = CourseEventParticipation.objects.select_related('user').\
                get(user=dict['user'], courseevent_id=dict['courseevent_id'])
            return  {'name' :  str("%s %s " % (courseeventparticipation.user.first_name, courseeventparticipation.user.last_name)),
                     'username': courseeventparticipation.user.username,
                     'is_owner' : False,
                     'id': courseeventparticipation.user_id
            }
        except:
            try:
                courseowner = CourseOwner.objects.select_related('user').\
                    get(user=dict['user'], course_id=dict['course_id'])
                return {
                    'name' :  str("%s %s " % (courseowner.user.first_name, courseowner.user.last_name)),
                    'username': courseowner.user.username,
                    'is_owner' : True,
                    'id': courseowner.user_id
                }
            except:
                if dict['user'].is_superuser:
                    return {
                        'name' :  dict['user'].username,
                        'is_owner' : True,
                        'id': dict['user'].id
                    }

