# coding: utf-8

from __future__ import unicode_literals, absolute_import

import datetime

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.core.validators import ValidationError
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from braces.views import MessageMixin
from apps_data.courseevent.models.courseevent import CourseEvent

from ..models.lesson import Lesson
from ..models.classlesson import ClassLesson

import logging

logger = logging.getLogger('activity.lessoncopy')


def copy_block_for_courseevent(self, block_pk, courseevent_pk):
    """
    copies a complete lesson from Lesson (in course) to ClassLesson (in a courseevent)
    """
    logger.info('---------------------------')
    logger.info(    'Lektion soll kopiert werden für das Kursereignis [%s] '
                    'und den Block [%s]'
                    % (courseevent_pk, block_pk))
    logger.info('---------------------------')
    try:
        lessonblock=Lesson.objects.get(pk=block_pk)
        logger.info('Block gefunden [%s]' % lessonblock)
    except ObjectDoesNotExist:
        logger.info('Block nicht gefunden')
        #TODO andere Fehlerbehandlung
        raise ValidationError('Der Unterrichtsblock wurde nicht gefunden')

    if not lessonblock.is_block:
        #TODO andere Fehlerbehandlung
        logger.info('Das ist kein Block, nur Blöcke können kopiert werden.')
        raise ValidationError('Das ist kein Block. Nur Blöcke können kopiert werden.')

    courseevent = CourseEvent.objects.get(pk=courseevent_pk)
    #TODO andere Fehlerbehandlung falls nicht da
    logger.info('Kursereignis gefunden  [%s]' % courseevent)

    lessonroot = get_object_or_404(Lesson,
                                   level=0,
                                   course=courseevent.course)
    logger.info('Vorlagewurzel gefunden [%s]' % lessonroot)

    classlessonroot = ClassLesson.objects.get(
            original_lesson_id=lessonroot.id,
            courseevent=courseevent)
    logger.info('Kurswurzel gefunden [%s] [%s]' % (classlessonroot,
                classlessonroot.id))

    # copy block
    classblock = _copy_any_level_lesson(lesson=lessonblock,
                                        courseevent=courseevent,
                                        parent=classlessonroot)
    logger.info('Block kopiert mit Ergebnis: [%s]' % classblock)

    # copy lesson
    lessons = lessonblock.get_children()
    for lesson in lessons:
        classlesson = _copy_any_level_lesson(lesson=lesson,
                                        courseevent=courseevent,
                                        parent=classblock)

        lessonsteps = lesson.get_children()

        for lessonstep in lessonsteps:
            classlessonstep = _copy_any_level_lesson(lesson=lessonstep,
                               courseevent=courseevent,
                               parent=classlesson)


    logger.info('Unterbaum kopiert')
    ClassLesson.objects.rebuild()
    logger.info('Der Baum wird neu aufgebaut')
    #TODO Fehlerseite einbauen
    return(HttpResponseRedirect(reverse('coursebackend:classlesson:start',
                                kwargs={'course_slug': courseevent.course.slug,
                                       'slug': courseevent.slug})))


def _copy_any_level_lesson(lesson, courseevent, parent):
    try:
        classlesson = ClassLesson.objects.get(
            courseevent=courseevent,
            is_original_lesson=True,
            original_lesson=lesson
        )
    except ObjectDoesNotExist:
        classlesson = ClassLesson()

    # from lesson
    classlesson.title=lesson.title
    classlesson.text=lesson.text
    classlesson.lesson_nr=lesson.lesson_nr
    classlesson.nr=lesson.nr

    classlesson.description=lesson.description
    classlesson.material=lesson.material
    classlesson.is_homework=lesson.is_homework

    # move or insert
    if not classlesson.pk:
        classlesson.course=lesson.course
        classlesson.courseevent=courseevent
        classlesson.original_lesson=lesson
        classlesson.is_original_lesson=True
        classlesson.insert_at(parent)
    # save
    classlesson.save()
    return classlesson

