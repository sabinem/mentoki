# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.core.validators import ValidationError

from model_utils.fields import MonitorField
from model_utils import Choices
from model_utils.models import TimeStampedModel

from apps_data.course.models.lesson import Lesson

from .courseevent import CourseEvent
from .forum import Forum
from .homework import Homework



class ClassroomMenuItemManager(models.Manager):

    def published(self, courseevent):
        return self.filter(courseevent=courseevent, published=True).order_by('display_nr')

    def courseevent(self, courseevent):
        return self.filter(courseevent=courseevent).order_by('display_nr')

    def get_startitem_from_slug(self, courseevent_slug):
        courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)

        return get_object_or_404(self, courseevent=courseevent, is_start_item=True )

    def published_forums(self, courseevent):
        #obj.classroommenuitem_set.all()

        forum_ids = self.filter(courseevent=self.courseevent,
                        item_type=ClassroomMenuItem.MENU_ITEM_TYPE.forum_item)

        forum_set = Forum.objects.filter(forum )

        return x

class ClassroomMenuItem(TimeStampedModel):
    """
    Classroom Menu Items make up the Classroom Menu
    """
    courseevent = models.ForeignKey(CourseEvent)

    lesson = models.ForeignKey(Lesson, blank=True, null=True,
                               )
    forum = models.ForeignKey(Forum, blank=True, null=True)
    homework = models.ForeignKey(Homework, blank=True, null=True )

    MENU_ITEM_TYPE = Choices(('forum', 'forum_item', _('Forum')),
                     ('lesson', 'lesson_item', _('Unterricht')),
                     ('anouncements', 'announcements', _('Ankündigungen')),
                     ('homework', 'homework', _('homework')),
                     ('last_posts', 'forum_last_posts', _('latest forum posts')),
                     ('private', 'student_private', _('students private place')),
                     ('header', 'header', _('header')),
                     ('participants', 'participants_list', _('participants list')),
                    )

    item_type = models.CharField(choices=MENU_ITEM_TYPE, max_length=15)
    display_nr = models.IntegerField()
    display_title = models.CharField(max_length=200, blank=True)

    published = models.BooleanField(default=False)
    publish_status_changed = MonitorField(monitor='published')

    is_start_item = models.BooleanField()

    objects = ClassroomMenuItemManager()

    def save(self, *args, **kwargs):

        # there can only be one start-item per courseevent

        if self.is_start_item :
            courseevents = ClassroomMenuItem.objects.courseevent(courseevent=self.courseevent).\
                exclude(pk=self.pk)
            for courseevent in courseevents:
                courseevent.is_start_item = False
                courseevent.save()

        # the display field will be filled automatically, if no value
        # is given, also by making the menu entry, the related objects counts as published
        # and will be updated accordingly

        if self.item_type == self.MENU_ITEM_TYPE.forum_item and self.display_title == "" :
            self.display_title = self.forum.title
            self.display_title = self.forum.title
            forum = Forum.objects.get(id=self.forum_id)
            forum.published = True
            forum.save()
            forum = Forum.objects.get(id=self.forum_id)
            print "*****in save of menu*****"
            print forum.id
            print forum.published
        if self.item_type == self.MENU_ITEM_TYPE.lesson_item and self.display_title == "" :
            self.display_title = self.lesson.title
        if self.item_type == self.MENU_ITEM_TYPE.homework and self.display_title == "" :
            self.display_title = self.homework.title
        if self.item_type == self.MENU_ITEM_TYPE.announcements and self.display_title == "" :
            self.display_title = u'Ankündigungen'
        if self.item_type == self.MENU_ITEM_TYPE.forum_last_posts and self.display_title == "" :
            self.display_title = u'aktuelle Beiträge'
        if self.item_type == self.MENU_ITEM_TYPE.student_private and self.display_title == "" :
            self.display_title = u'privater Arbeitsbereich'
        if self.item_type == self.MENU_ITEM_TYPE.participants_list and self.display_title == "" :
            self.display_title = u'Teilnehmerliste'

        super(ClassroomMenuItem, self).save(*args, **kwargs)

    def clean(self):
        """
        checks input in relation to item_type
        """

        # more helpful validations errors for the two main fields

        if not self.item_type:
           raise ValidationError('Bitte einen Eitragstyp wählen für den Menüeintrag!')
        if not self.display_nr:
           raise ValidationError('Bitte angeben an wievielter Stelle der Menüeintrag erscheinen soll!')

        if self.item_type == self.MENU_ITEM_TYPE.header:

            # header item: not start_item, no relationships allowed

            if self.is_start_item:
                raise ValidationError('Überschrift kann nicht Startpunkt sein!')

        if self.item_type in [self.MENU_ITEM_TYPE.header,
                              self.MENU_ITEM_TYPE.announcements,
                              self.MENU_ITEM_TYPE.student_private,
                              self.MENU_ITEM_TYPE.forum_last_posts,
                              self.MENU_ITEM_TYPE.participants_list]:
                raise ValidationError("""Eintragsart kann keinen Bezug zu einem Forum,
                                      einer Aufgabe oder einer Lektion haben.""")

        if self.item_type == self.MENU_ITEM_TYPE.lesson_item:

             # lesson item: only relationships lesson, is required

            if not self.lesson:
                raise ValidationError('''Lektions-Eintrag muss zu einer Lektion verlinken.
                                      Bitte eine Lektion auswählen.''', code='invalid_object'
                                      )
            if self.forum or self.homework:
                raise ValidationError('''Bei Eintragstyp Lektion bitte nur eine Lektion
                                      als Link-Objekt angeben.''')

        if self.item_type == self.MENU_ITEM_TYPE.forum_item:

             # forum item: only relationships forum, is required

            if not self.forum:
                raise ValidationError('''Forum-Eintrag muss zu einem Forum verlinken.
                                      Bitte ein Forum auswählen.''')
            if self.lesson or self.homework:
                raise ValidationError('Bei Eintragstyp Forum bitte nur Forum als Link-Objekt angeben.')

        if self.item_type == self.MENU_ITEM_TYPE.homework:

             # homework item: only relationships homework, is required

            if not self.homework:
                raise ValidationError('''Aufgaben-Eintrag muss zu einer Aufgabe verlinken.
                                      Bitte eine Aufgabe auswählen.''')
            if self.lesson or self.forum:
                raise ValidationError('''Bei diesem Eintragstyp bitte nur eine Aufgabe als
                                      Link-Objekt auswählen.''')


    def __unicode__(self):
        return u'menu %s / %s' % (self.courseevent, str(self.display_nr))







