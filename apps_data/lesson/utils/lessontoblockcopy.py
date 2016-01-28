# coding: utf-8
"""
copies a lesson from one block to another in the course

"""
from __future__ import unicode_literals, absolute_import

from django.core.validators import ValidationError
from django.core.exceptions import ObjectDoesNotExist

from apps_data.course.models.course import Course

from ..models.lesson import Lesson

import logging

logger = logging.getLogger('activity.lessoncopy')


def copy_lesson_to_block(block, lesson_pk):
    """
    copies a complete lesson from Lesson (in course) from one block
    to another block in the same course
    """
    logger.info('---------------------------')
    logger.info(    'Lektion [%s] soll kopiert werden für die Kursvorlage [%s] '
                    'und in den Block [%s]'
                    % (lesson_pk, block.course_id, block.pk))
    logger.info('---------------------------')
    try:
        # check arguments
        lessonblock_to = block
        lesson = Lesson.objects.get(pk=lesson_pk)
        lessonblock_from = lesson.parent
        assert lessonblock_to.course_id == lesson.course_id
    except ObjectDoesNotExist:
        logger.info('Eines der übergebenen Objekte wurde nicht gefunden')
        #TODO andere Fehlerbehandlung
        raise ValidationError('Eines der übergebenen Objekte wurde nicht gefunden')
    except AssertionError:
        #TODO andere Fehlerbehandlung
        logger.info('Eines der übergebenen Objekte ist der falschen Kursvorlage zugeordnet.')
        raise ValidationError('Eines der übergebenen Objekte ist der falschen Kursvorlage zugeordnet.')

    # copy block
    new_lesson = _copy_any_level_lesson(
        old_lesson = lesson,
        new_parent = lessonblock_to)
    logger.info('Lektion kopiert mit Ergebnis: [%s]' % new_lesson)

    # copy lessonsteps
    lessonsteps = lesson.get_children()

    for lessonstep in lessonsteps:
        new_lessonstep = _copy_any_level_lesson(
            old_lesson=lessonstep,
            new_parent=new_lesson)

        logger.info('Lernschritte kopiert [%s]' % new_lessonstep)
    Lesson.objects.rebuild()
    logger.info('Der Baum wird neu aufgebaut')
    return new_lesson

def _copy_any_level_lesson(old_lesson, new_parent):
    # from lesson
    new_lesson = Lesson()
    new_lesson.nr = old_lesson.nr
    new_lesson.lesson_nr = old_lesson.lesson_nr
    new_lesson.title = old_lesson.title
    new_lesson.text = old_lesson.text
    new_lesson.show_number = old_lesson.show_number
    new_lesson.description = old_lesson.description
    new_lesson.material = old_lesson.material
    new_lesson.is_homework = old_lesson.is_homework
    new_lesson.show_work_area = old_lesson.show_work_area
    new_lesson.allow_questions = old_lesson.allow_questions
    new_lesson.course = old_lesson.course
    new_lesson.insert_at(new_parent)
    new_lesson.save()
    return new_lesson

