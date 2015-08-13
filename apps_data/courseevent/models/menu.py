# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.core.validators import ValidationError

from model_utils.fields import MonitorField
from model_utils import Choices
from model_utils.models import TimeStampedModel

from apps_data.lesson.models.classlesson import ClassLesson

from .courseevent import CourseEvent
from .announcement import Announcement
from .forum import Forum
from .homework import Homework



class ClassroomMenuItemManager(models.Manager):

    def all_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent).order_by('display_nr')

    def get_startitem_from_slug(self, slug):
        return self.get(courseevent__slug=slug, is_start_item=True )

    def create(self, courseevent, homework, lesson, forum, display_title,
               display_nr, item_type, published, is_start_item):
        menuitem = ClassroomMenuItem(
            courseevent=courseevent,
            homework=homework,
            lesson=lesson,
            forum=forum,
            display_title=display_title,
            display_nr=display_nr,
            item_type=item_type,
            is_start_item=is_start_item
        )
        menuitem.save()
        return menuitem


class ClassroomMenuItem(TimeStampedModel):
    """
    Classroom Menu Items make up the Classroom Menu
    """
    courseevent = models.ForeignKey(CourseEvent)

    lesson = models.ForeignKey(ClassLesson, blank=True, null=True)
    forum = models.ForeignKey(Forum, blank=True, null=True)
    homework = models.ForeignKey(Homework, blank=True, null=True )

    MENU_ITEM_TYPE = Choices(('forum', 'forum_item', _('Forum')),
                     ('lesson', 'lesson_item',  _('Unterricht')),
                     ('announcements', 'announcements_item', _('Ankündigungen')),
                     ('homework', 'homework_item', _('Hausaufgabe')),
                     ('last_posts', 'last_posts_item', _('Neueste Beiträge')),
                     ('private', 'private_item', _('Privatbereich')),
                     ('header', 'header_item', _('Überschrift')),
                     ('participants', 'participants_item', _('Teilnehmerliste')),
                    )
    item_type = models.CharField(
        verbose_name="Typ des Menüpunkts",
        help_text="""Welcher Art ist der Menüeintrag: Überschrift, Link, etc?""",
        choices=MENU_ITEM_TYPE,
        max_length=15)

    display_nr = models.IntegerField(
        verbose_name="Reihenfolge Nummer",
        help_text="""An welcher Position im Menü soll der Menüpunkt angezeigt werden?""",
    )
    display_title = models.CharField(max_length=200, blank=True)

    is_start_item = models.BooleanField(
        verbose_name="Ist Startpunkt",
        help_text="""Welcher Menüpunkt soll im Klassenzimmer als
            erstes angesprungen werden?""")

    objects = ClassroomMenuItemManager()

    unique_together=('display_title', 'courseevent')

    def preset_menu_item_display_title(self):
        if self.item_type == self.MENU_ITEM_TYPE.lesson_item and self.display_title == "" :
            return u'Forum: %s' % (self.forum)
        if self.item_type == self.MENU_ITEM_TYPE.homework_item and self.display_title == "" :
            return u'Aufgabe: %s' % (self.homework)
        if self.item_type == self.MENU_ITEM_TYPE.lesson_item and self.display_title == "" :
            return u'Unterricht: %s' % (self.lesson)
        else:
            return u'-'

    def get_menu_item_classroom_url(self):

        if self.item_type == self.MENU_ITEM_TYPE.forum_item:
            return Announcement.get_classroom_list_url(slug=self.slug)
        if self.item_type == self.MENU_ITEM_TYPE.lesson_item:
            return Announcement.get_classroom_list_url(slug=self.slug)
        if self.item_type == self.MENU_ITEM_TYPE.homework_item:
            return Announcement.get_classroom_list_url(slug=self.slug)
        if self.item_type == self.MENU_ITEM_TYPE.announcements_item:
            return Announcement.get_classroom_list_url(slug=self.slug)
        if self.item_type == self.MENU_ITEM_TYPE.participants_item:
            return Announcement.get_classroom_list_url(slug=self.slug)
        if self.item_type == self.MENU_ITEM_TYPE.last_posts_item:
            return Announcement.get_classroom_list_url(slug=self.slug)
        if self.item_type == self.MENU_ITEM_TYPE.private_item:
            return Announcement.get_classroom_list_url(slug=self.slug)

    def get_menu_item_work_url(self):
        if self.item_type == self.MENU_ITEM_TYPE.announcements_item:
            return Announcement.get_list_url(slug=self.slug, course_slug=self.course_slug)

    def is_classroom_link(self):
        if self.item_type in [self.MENU_ITEM_TYPE.forum_item,
                              self.MENU_ITEM_TYPE.lesson_item,
                              self.MENU_ITEM_TYPE.homework_item,
                              self.MENU_ITEM_TYPE.announcements_item,
                              self.MENU_ITEM_TYPE.last_posts_item,
                              self.MENU_ITEM_TYPE.private_item,
                              self.MENU_ITEM_TYPE.participants_item,
                              ]:
            return True
        else:
            return False

    def save(self, *args, **kwargs):

        # there can only be one start-item per courseevent

        if self.is_start_item :
            courseevents = ClassroomMenuItem.objects.all_for_courseevent(courseevent=self.courseevent).\
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
        if self.item_type == self.MENU_ITEM_TYPE.lesson_item and self.display_title == "" :
            self.display_title = self.lesson.title
        if self.item_type == self.MENU_ITEM_TYPE.homework_item and self.display_title == "" :
            self.display_title = self.homework.title
        if self.item_type == self.MENU_ITEM_TYPE.announcements_item and self.display_title == "" :
            self.display_title = u'Ankündigungen'
        if self.item_type == self.MENU_ITEM_TYPE.last_posts_item and self.display_title == "" :
            self.display_title = u'aktuelle Beiträge'
        if self.item_type == self.MENU_ITEM_TYPE.private_item and self.display_title == "" :
            self.display_title = u'privater Arbeitsbereich'
        if self.item_type == self.MENU_ITEM_TYPE.participants_item and self.display_title == "" :
            self.display_title = u'Teilnehmerliste'

        super(ClassroomMenuItem, self).save(*args, **kwargs)

    def clean(self):
        """
        checks input in relation to item_type
        """

        # more helpful validations errors for the two main fields

        if not self.item_type:
           raise ValidationError('Bitte einen Eintragstyp wählen für den Menüeintrag!')
        if not self.display_nr:
           raise ValidationError('Bitte angeben an wievielter Stelle der Menüeintrag erscheinen soll!')

        if self.item_type == self.MENU_ITEM_TYPE.header_item:

            # header item: not start_item, no relationships allowed

            if self.is_start_item:
                raise ValidationError('Überschrift kann nicht Startpunkt sein!')

        if self.item_type in [self.MENU_ITEM_TYPE.header_item,
                              self.MENU_ITEM_TYPE.announcements_item,
                              self.MENU_ITEM_TYPE.private_item,
                              self.MENU_ITEM_TYPE.last_posts_item,
                              self.MENU_ITEM_TYPE.participants_item]:
                if self.lesson or self.forum or self.homework:
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

        if self.item_type == self.MENU_ITEM_TYPE.homework_item:

             # homework item: only relationships homework, is required

            if not self.homework:
                raise ValidationError('''Aufgaben-Eintrag muss zu einer Aufgabe verlinken.
                                      Bitte eine Aufgabe auswählen.''')
            if self.lesson or self.forum:
                raise ValidationError('''Bei diesem Eintragstyp bitte nur eine Aufgabe als
                                      Link-Objekt auswählen.''')


    def __unicode__(self):
        return u'%s: %s' % (self.get_item_type_display(), self.display_title)







