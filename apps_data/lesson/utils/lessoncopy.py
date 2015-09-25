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


def copy_block_for_courseevent(self, block_pk, courseevent_pk):
    """
    copies a complete lesson from Lesson (in course) to ClassLesson (in a courseevent)
    """
    try:
        lessonblock=get_object_or_404(Lesson, pk=block_pk)
    except ObjectDoesNotExist:
         raise ValidationError('Der Unterrichtsblock wurde nicht gefunden')

    if not lessonblock.is_block:
        raise ValidationError('Das ist kein Block. Nur Blöcke können kopiert werden.')

    courseevent = get_object_or_404(CourseEvent, pk=courseevent_pk)
    lessonroot = get_object_or_404(Lesson, level=0, course=courseevent.course)
    classlessonroot = ClassLesson.objects.get(
            original_lesson_id=lessonroot.id,
            courseevent=courseevent)

    # copy block
    classblock = _copy_any_level_lesson(lesson=lessonblock,
                                        courseevent=courseevent,
                                        parent=classlessonroot)
    # copy lesson
    lessons = lessonblock.get_children()
    lessonsteps_moved = []
    for lesson in lessons:
        classlesson = _copy_any_level_lesson(lesson=lesson,
                                        courseevent=courseevent,
                                        parent=classblock)

        lessonsteps = lesson.get_children()

        for lessonstep in lessonsteps:
            classlessonstep = _copy_any_level_lesson(lesson=lessonstep,
                               courseevent=courseevent,
                               parent=classlesson)
            if not classlessonstep:
                lessonsteps_moved.append(lessonstep)

    for lessonstep in lessonsteps_moved:
        classparent = ClassLesson.objects.get(courseevent=courseevent,
                                              original_lesson=lessonstep.parent)
        classlesson = _copy_any_level_lesson(lesson=lessonstep,
                                        courseevent=courseevent,
                                        parent=classparent,
                                        move=True)


    ClassLesson.objects.rebuild()


    return(HttpResponseRedirect(reverse('coursebackend:classlesson:start',
                                kwargs={'course_slug': courseevent.course.slug,
                                       'slug': courseevent.slug})))


def _copy_any_level_lesson(lesson, courseevent, parent, move=False):
    now = datetime.datetime.now()
    try:
        classlesson = ClassLesson.objects.get(original_lesson=lesson)
        if lesson.level == 3:
            if classlesson.parent.original_lesson != parent and not move:
                return None
    except:
        classlesson = ClassLesson(created=now)

    classlesson.title=lesson.title
    classlesson.text=lesson.text
    classlesson.lesson_nr=lesson.lesson_nr
    classlesson.nr=lesson.nr
    classlesson.course=lesson.course
    classlesson.description=lesson.description
    classlesson.courseevent=courseevent
    classlesson.material=lesson.material
    classlesson.original_lesson=lesson
    classlesson.modified=now
    classlesson.is_homework=lesson.is_homework
    classlesson.is_original_lesson=True
    if not classlesson.pk:
        classlesson.insert_at(parent)
    elif move:
        classlesson.move_to(parent)
    print "--- before save"
    print classlesson
    classlesson.save(copy=True)
    return classlesson

