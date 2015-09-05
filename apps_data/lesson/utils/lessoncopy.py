# coding: utf-8

from __future__ import unicode_literals, absolute_import

import datetime

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.core.validators import ValidationError
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from apps_data.courseevent.models.courseevent import CourseEvent

from ..models.lesson import Lesson
from ..models.classlesson import ClassLesson


def copy_lesson_selected(self, lesson, lessonsteps, copy_lesson):
    """
    copies selected parts of a lesson from Lesson (in course) to ClassLesson (in a courseevent)
    :param lesson_pk:
    :param courseevent_pk:
    :return: Redirects to the ClassLesson start page in the Coursebackend
    """
    if copy_lesson:
        classlesson=_update_lesson(lesson)
    else:
        classlesson = ClassLesson.objects.get(original_lesson=lesson)

    for lessonstep in lessonsteps:
        _update_or_create_lessonstep(lessonstep, classlesson, published=classlesson.published)

    ClassLesson.objects.rebuild()
    return classlesson


def copy_lesson_for_courseevent(self, lesson_pk, courseevent_pk):
    """
    copies a complete lesson from Lesson (in course) to ClassLesson (in a courseevent)
    :param lesson_pk: id of the lesson that should be copied
    :param courseevent_pk: id of the courseevent to which the lesson should be copied
    :return: Redirects to the ClassLesson start page in the Coursebackend
    """
    try:
        lesson=get_object_or_404(Lesson, pk=lesson_pk)
    except ObjectDoesNotExist:
         raise ValidationError('Die Lektion wurde nicht gefunden')

    lessonsteps = lesson.get_children()

    if not lesson.is_lesson:
        raise ValidationError('Das ist keine Lektion. Nur Lektionen können kopiert werden.')

    courseevent=get_object_or_404(CourseEvent, pk=courseevent_pk)
    lessonblock=get_object_or_404(Lesson, pk=lesson.parent_id)

    try:
        classblock = ClassLesson.objects.get(original_lesson_id=lessonblock.id)
    except:
        classblock = _copy_any_level_lesson(lesson=lessonblock,
                                            courseevent=courseevent,
                                            parent=None)

    classlesson= _copy_any_level_lesson(lesson=lesson,
                                        courseevent=courseevent,
                                        parent=classblock)

    for step in lessonsteps:
        _copy_any_level_lesson(lesson=step,
                               courseevent=courseevent,
                               parent=classlesson)

    ClassLesson.objects.rebuild()

    return(HttpResponseRedirect(reverse('coursebackend:classlesson:start',
                               kwargs={'course_slug': courseevent.course.slug, 'slug': courseevent.slug})))


def _copy_any_level_lesson(lesson, courseevent, parent):
    now = datetime.datetime.now()
    classlesson = ClassLesson(
        title=lesson.title,
        text=lesson.text,
        lesson_nr=lesson.lesson_nr,
        nr=lesson.nr,
        course=lesson.course,
        description=lesson.description,
        courseevent=courseevent,
        material=lesson.material,
        original_lesson=lesson,
        modified=now,
        created=now,
        is_homework=lesson.is_homework,
        is_original_lesson=True
    )
    classlesson.insert_at(parent)
    classlesson.save(copy=True)

    return classlesson


def _update_lesson(lesson):
    classlesson = ClassLesson.objects.get(original_lesson=lesson)
    classlesson.title=lesson.title
    classlesson.text=lesson.text
    classlesson.lesson_nr=lesson.lesson_nr
    classlesson.nr=lesson.nr
    classlesson.course=lesson.course
    classlesson.description=lesson.description
    classlesson.is_original_lesson = True

    now = datetime.datetime.now()
    classlesson.created = now
    classlesson.modified = now

    classlesson.save(copy=True)
    return classlesson


def _update_or_create_lessonstep(lessonstep, classlesson, published=False):
    try:
        classlessonstep = ClassLesson.objects.get(original_lesson=lessonstep)
        classlessonstep.title=lessonstep.title
        classlessonstep.text=lessonstep.text
        classlessonstep.lesson_nr=lessonstep.lesson_nr
        classlessonstep.nr=lessonstep.nr
        classlessonstep.course=lessonstep.course
        classlessonstep.description=lessonstep.description
        classlessonstep.material=lessonstep.material
        classlessonstep.is_homework=lessonstep.is_homework
        classlessonstep.courseevent=classlesson.courseevent
        classlessonstep.is_original_lesson = True
        classlessonstep.published = published

        now = datetime.datetime.now()
        classlessonstep.created = now
        classlessonstep.modified = now

        classlessonstep.save(copy=True)

    except ObjectDoesNotExist:
        classlessonstep = _copy_any_level_lesson(
            lesson=lessonstep,
            courseevent=classlesson.courseevent,
            parent=classlesson)

    return classlessonstep