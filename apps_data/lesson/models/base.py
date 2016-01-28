# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_enumfield import enum

from mptt.models import MPTTModel, TreeForeignKey, TreeManager

from fontawesome.fields import IconField

from model_utils.choices import Choices

from apps_data.course.models.course import Course
from apps_data.material.models.material import Material

from ..constants import LessonType



class BaseLessonManager(TreeManager):

    def start_tree_for_course(self, course):
        """
        fetches the complete tree for the course including material
        :param course
        :return: all nodes with material for a course in tree order
        """
        return self.filter(course=course, level=0)\
            .get_descendants(include_self=True).select_related('material')

    def lessons_for_course(self, course):
        """
        fetches lessons for the course
        :param course
        :return: all lessons for the course
        """
        return self.filter(course=course, level=2)

    def blocks_for_course(self, course):
        """
        fetches blocks for the course
        :param course
        :return: all blocks for the course
        """
        return self.filter(course=course, level=1)\
            .order_by('nr')

    def homeworks(self, course):
        return self.filter(course=course,
                           is_homework=True,
                           )


def lesson_nr_block(nr):
    """
    computed field in model: lesson_nr for blocks
    :return: empty for blocks
    """
    return u'(%s)' % str(nr)

def lesson_nr_lesson(nr):
    """
    computed field in model: lesson_nr for lessons
    :return: is just <nr> for lessons
    """
    return u'%s' % str(nr)

def lesson_nr_step(nr, parent_nr):
    """
    computed field in model: lesson_nr for lessons
    :return: is just <parent.nr>.<nr> for lessonsteps
    """
    return u'%s.%s' % (str(parent_nr), str(nr))


class BaseLesson(MPTTModel):
    """
    Base Lessons is an abstract model and a blueprint for both
    Lessons an ClassLessons. It depends on course.
    """
    parent = TreeForeignKey('self',
        verbose_name="einhängen unter",
        null=True,
        blank=True,
        related_name='children',
        db_index=True,

        )

    # dependant on course
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT)

    nr = models.IntegerField(
        verbose_name=_('Nr.'),
        default=1)
    icon = IconField(
        verbose_name="Icon",
        help_text="Neben dem Menüeintrag kann ein Icon angezeigt werden.")
    # this field is derived from nr and and parent.nr depending on the level
    # see save_method
    lesson_nr = models.CharField(
        verbose_name=_('Lektionsnr.'),
        help_text='abgeleitetes Feld: keine manuelle Eingabe',
        blank=True,
        max_length=10,
        editable=False)
    title = models.CharField(
        verbose_name="Überschrift",
        help_text="Lektions-Titel",
        max_length=100)
    text = models.TextField(
        verbose_name="Lektionstext",
        help_text="Text der Lektion",
        blank=True)
    description = models.CharField(
        verbose_name='kurze Beschreibung',
        help_text="diese Beschreibung erscheint nur in den Übersichten",
        max_length=200,
        blank=True)

    material = models.ForeignKey(Material,
        verbose_name="Kursmaterial",
        help_text="Material der Lektion",
        blank=True,
        null=True)
    show_number = models.BooleanField(
        default=True,
        verbose_name="Nummerierung anzeigen")
    is_homework = models.BooleanField(default=False)
    allow_questions = models.BooleanField(default=False)
    show_work_area = models.BooleanField(default=False)

    objects = BaseLessonManager()

    # lesson type: blocks > lesson > step having levels: 0, 1, 2
    #LESSON_TYPE = Choices(
    #                 ('block', _('Block')),
    #                 ('lesson', _('Lesson')),
    #                 ('step', _('Step')),)

    class Meta:
        verbose_name = "Lektion"
        verbose_name_plural = "Lektionen"
        abstract = True

    class MPTTMeta:
        order_insertion_by = ['course', 'nr']

    def __unicode__(self):
        """
        blocks are just shown by their title,
        lessons are shown as <block-title>: <lesson_nr>. <lesson_title>
        and lessonsteps are shown as <lesson_nr>. <lesson_title>
        :return: self representation
        """
        if self.level == 0:
            return u'Wurzel: %s' % (self.course)
        elif self.level == 1:
            return u'Block: %s' % (self.title)
        elif self.level == 2:
            return u'%s: %s. %s' % (self.parent.title, self.lesson_nr, self.title)
        elif self.level == 3:
            return u'%s %s' % (self.lesson_nr, self.title)

    def save(self, *args, **kwargs):
        """
        lesson_nr is calculated and stored in the database for performance
        """
        if self.level:
            if self.level == 1:
                self.lesson_nr = lesson_nr_block(nr=self.nr)
            elif self.level == 2 :
                self.lesson_nr = lesson_nr_lesson(nr=self.nr)
            elif self.level == 3 :
                self.lesson_nr = lesson_nr_step(nr=self.nr, parent_nr=self.parent.nr)
        super(BaseLesson, self).save(*args, **kwargs)

    #@property
    #def lesson_type(self):
    #    """
    #    this just translates the internal level of the lesson into a level type,
    #    see above.
    #    :return: lesson_type: block, lesson or step
    #    """
    #    if self.level == 1 :
    #        return self.LESSON_TYPE.block
    #    elif self.level == 2 :
    #        return self.LESSON_TYPE.lesson
    #    elif self.level == 3 :
    #        return self.LESSON_TYPE.step

    @property
    def lesson_type(self):
        """
        this just translates the internal level of the lesson into a level type,
        see above.
        :return: lesson_type: block, lesson or step
        """
        if self.level == 0 :
            return LessonType.ROOT
        elif self.level == 1 :
            return LessonType.BLOCK
        elif self.level == 2 :
            return LessonType.LESSON
        elif self.level == 3 :
            return LessonType.LESSONSTEP


    def breadcrumb(self):
        """
        in breadcrumbs a different representation is chosen for block. lesson and step
        block: <title>
        lesson: <lesson_nr>. <title>
        lessonstep: <lesson_nr> <title>
        :return: representation in breadcrumbs
        """
        if self.level == 1 or not self.show_number:
            return u'%s' % (self.title)
        elif self.level == 2:
            return u'%s. %s' % (self.lesson_nr, self.title)
        elif self.level == 3:
            return u'%s %s' % (self.lesson_nr, self.title)

    def get_delete_tree(self):
        return self.get_descendants(include_self=True).select_related('material')

    def get_next_sibling(self):
        """
        for blocks the mptt method get_next_sibling needs to be overwritten, so that
        it stays into the course
        :return: None or next mptt-sibiling
        """
        next = super(BaseLesson, self).get_next_sibling()
        try:
            if next.course_id == self.course_id:
                return next
            else:
                return None
        except:
            return None

    def get_previous_sibling(self):
        """
        for blocks the mptt method get_previous_sibling needs to be overwritten, so that
        it stays into the course
        :return: None or previous mptt-sibiling
        """
        previous = super(BaseLesson, self).get_previous_sibling()
        try:
            if previous.course_id == self.course_id:
                return previous
            else:
                return None
        except:
            return None

    def get_breadcrumbs_with_self(self):
        return self.get_ancestors(include_self=True).exclude(level=0)

    def get_tree_without_self_with_material(self):
        """
        gets real decendants and materials of a node
        :return: real decendants with material
        """
        return self.get_descendants(include_self=False).select_related('material')

    def get_tree_without_self_without_material(self):
        """
        gets real decendants but not the materials of a node
        :return: real decendants without material
        """
        return self.get_descendants(include_self=False)

    def is_block(self):
        """
        bool that decides wether a lesson is a block
        :return: bool
        """
        if self.get_level() == 1:
            return True
        else:
            return False

    def is_lesson(self):
        """
        bool that decides wether a lesson is a lesson
        :return: bool
        """
        if self.get_level() == 2:
            return True
        else:
            return False

    def is_step(self):
        """
        bool that decides wether a lesson is a step
        :return: bool
        """
        if self.get_level() == 3:
            return True
        else:
            return False

    def is_owner(self, user):
        """
        Is this person a teacher in this course? (Then he may work on it.)
        :param user
        :return: bool
        """
        if self.course.is_owner(user):
            return True
        else:
            return False

