# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.functional import cached_property
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey, TreeManager

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField
from model_utils.choices import Choices


from .course import Course
from .material import Material
from .oldcoursepart import CourseBlock, CourseMaterialUnit, CourseUnit
from apps_data.courseevent.models.courseevent import CourseEvent

from model_utils.managers import QueryManager
from django.db.models import Q


class LessonManager(TreeManager):

    def blocks_for_course(self, course):
        return self.filter(course=course, level=0).\
            get_descendants(include_self=True)

    def lessons_published_in_courseevent(self, courseevent):
        return self.filter(lessonpublisher__courseevent=courseevent,
                           lessonpublisher__published=True,
                           level=1).\
                           get_descendants(include_self=True)

def lesson_material_name(instance, filename):
        path = '/'.join([instance.course.slug, slugify(instance.title), filename])
        return path

class Lesson(MPTTModel, TimeStampedModel):

    course = models.ForeignKey(Course)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name="einhängen unter")

    nr = models.IntegerField(default=1)
    lesson_nr = models.CharField(blank=True, max_length=10)

    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    description = models.CharField(max_length=200, blank=True, verbose_name='kurze Beschreibung')

    material = models.ManyToManyField(Material, blank=True)

    published_in_courseevent = models.ManyToManyField(CourseEvent, through="LessonPublisher", blank=True)

    #just for the data_migration: refers to old data-structure (oldcourseparts),
    # will be deleted after data-transfer
    courseblock = models.ForeignKey(CourseBlock, null=True, blank=True)
    unit = models.ForeignKey(CourseUnit, null=True, blank=True)
    unitmaterial = models.ForeignKey(CourseMaterialUnit, null=True, blank=True)

    objects = LessonManager()
    block = QueryManager(level=0)
    lesson = QueryManager(level=1)
    lesson_step = QueryManager(level=2)
    parent_choice_new = QueryManager(level__lte=1).order_by('tree_id', 'level', 'nr')

    LESSON_TYPE = Choices(
                     ('block', _('Block')),
                     ('lesson', _('Lesson')),
                     ('step', _('Step')),)

    class Meta:
        verbose_name = "Lektion"
        verbose_name_plural = "Lektionen"

    class MPTTMeta:
        order_insertion_by = ['course', 'nr']

    def save(self, *args, **kwargs):
        # lesson_nr is calculated and stored in the database for performance
        if self.level == 0 :
            self.lesson_nr = ""
        elif self.level == 1 :
            self.lesson_nr = u'%s' % str(self.nr)
        elif self.level == 2 :
            self.lesson_nr = u'%s.%s' % (str(self.parent.nr), str(self.nr))
        else:
            raise ValueError('unexpected lesson level')
        super(Lesson, self).save(*args, **kwargs)

    @property
    def lesson_type(self):
        if self.level == 0 :
            return self.LESSON_TYPE.block
        elif self.level == 1 :
            return self.LESSON_TYPE.lesson
        elif self.level == 2 :
            return self.LESSON_TYPE.step
        else:
            raise ValueError('unexpected lesson level')

    def __unicode__(self):
        return u'%s: %s %s' % (str(self.course_id), self.lesson_nr, self.title)

    def display_with_nr(self):
        return u'%s: %s %s' % (str(self.course_id), str(self.lesson_nr), self.title)

    @cached_property
    def course_slug(self):
        return self.course.slug

    def get_next_sibling(self):
        next = super(Lesson, self).get_next_sibling()
        try:
            if next.course_id == self.course_id:
                return next
            else:
                return None
        except:
            return None

    def get_previous_sibling(self):
        previous = super(Lesson, self).get_previous_sibling()
        try:
            if previous.course_id == self.course_id:
                return previous
            else:
                return None
        except:
            return None

    def get_tree_with_material(self):
        return self.get_descendants(include_self=True).prefetch_related('material')

    @cached_property
    def is_block(self):
        if self.get_level() == 0:
            return True
        else:
            return False

    @cached_property
    def is_lesson(self):
        if self.get_level() == 1:
            return True
        else:
            return False

    @cached_property
    def is_lesson_step(self):
        if self.get_level() == 2:
            return True
        else:
            return False

    def is_owner(self, user):
        """
        Is this person a teacher in this course? (Then he may work on it.)
        """
        if self.course.is_owner(user):
            return True
        else:
            return False


    def get_absolute_url(self):
        return reverse('coursebackend:lesson:detail', kwargs={'course_slug':self.course_slug, 'pk':self.pk })


    def possible_parents(self):
        qs = Lesson.objects.none()
        if self.is_block:
            pass
        elif self.is_leaf_node():
           qs = Lesson.objects.filter(level__lte=1, course=self.course)
        else:
           qs = Lesson.objects.filter(level=0, course=self.course)
        return qs.exclude(pk=self.pk).order_by('tree_id', 'level', 'nr')


class LessonPublisher(models.Model):
    """
    Units (Lessons) are published in a class, when the instructor decides
    students are ready for them. Publication is decided on the level of the
    CourseUnit. See app course for details.
    """
    courseevent = models.ForeignKey(CourseEvent)
    lesson = models.ForeignKey(Lesson)
    publish_status_changed = MonitorField(monitor='published')
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s / %s' % (self.courseevent, self.lesson)

    class Meta:
        verbose_name = "LessonPublisher"
