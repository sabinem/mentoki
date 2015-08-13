# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.functional import cached_property
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.validators import ValidationError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from mptt.models import MPTTModel, TreeForeignKey, TreeManager

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField
from model_utils.choices import Choices

from apps_data.course.models.course import Course
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.material.models.material import Material

from model_utils.managers import QueryManager
from django.db.models import Q

from .models.lesson import Lesson
from .models.classlesson import ClassLesson


def copy_lesson_for_courseevent(self, lesson_pk, courseevent_pk):

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
        classblock = copy_any_level_lesson(lesson=lessonblock, courseevent=courseevent, parent=None)

    classlesson= copy_any_level_lesson(lesson=lesson, courseevent=courseevent, parent=classblock)

    for step in lessonsteps:
        copy_any_level_lesson(lesson=step, courseevent=courseevent, parent=classlesson)

    return(HttpResponseRedirect(reverse('coursebackend:lesson_courseevent:copy',
                               kwargs={'course_slug': courseevent.course.slug, 'slug': courseevent.slug})))



def copy_any_level_lesson(lesson, courseevent, parent):
    classlesson = ClassLesson(
        title=lesson.title,
        text=lesson.text,
        lesson_nr=lesson.lesson_nr,
        nr=lesson.nr,
        course=lesson.course,
        description=lesson.description,
        courseevent=courseevent,
        original_lesson=lesson
    )
    classlesson.insert_at(parent)
    classlesson.save()
    for item in lesson.materials.all():
        classlesson.materials.add(item)

    return classlesson

