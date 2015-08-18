# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError

from model_utils import Choices
from model_utils.models import TimeStampedModel

from apps_data.lesson.models.classlesson import ClassLesson

from .courseevent import CourseEvent
from .forum import Forum
from .homework import Homework


def switch_start_item(menuitem):
    """
    The start item of a courseevent is changed to a given new menuitem
    :param menuitem: the menuitem that should be the new startitem
    :return: None
    """
    menuitems = ClassroomMenuItem.objects.all_for_courseevent(courseevent=menuitem.courseevent).\
        exclude(pk=menuitem.pk)
    for item in menuitems:
        item.is_start_item = False
        item.save()


def switch_item_object_published_status(menuitem, publish):
    if menuitem.item_type ==  menuitem.MENU_ITEM_TYPE.forum_item:
        forum = Forum.objects.get(pk=menuitem.forum_id)
        forum.published = publish
        forum.save()
    elif menuitem.item_type ==  menuitem.MENU_ITEM_TYPE.lesson_item:
        classlesson = ClassLesson.objects.get(pk=menuitem.classlesson_id)
        classlesson.published = publish
        classlesson.save()
    elif menuitem.item_type ==  menuitem.MENU_ITEM_TYPE.homework_item:
        homework = Homework.objects.get(pk=menuitem.forum_id)
        homework.published = publish
        homework.save()


class ClassroomMenuItemManager(models.Manager):

    def all_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent).order_by('display_nr')

    def get_startitem_from_slug(self, slug):
        return self.get(courseevent__slug=slug, is_start_item=True )

    def create(self, courseevent, homework, classlesson, forum, display_title,
               display_nr, item_type, is_start_item, active):
        menuitem = ClassroomMenuItem(
            courseevent=courseevent,
            homework=homework,
            classlesson=classlesson,
            forum=forum,
            display_title=display_title,
            display_nr=display_nr,
            active=active,
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

    classlesson = models.ForeignKey(
        ClassLesson,
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    forum = models.ForeignKey(
        Forum,
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    homework = models.ForeignKey(
        Homework,
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )

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

    active = models.BooleanField(default=True)

    display_nr = models.IntegerField(
        verbose_name="Reihenfolge Nummer",
        help_text="""An welcher Position im Menü soll der Menüpunkt angezeigt werden?""",
    )
    display_title = models.CharField(max_length=200)

    is_start_item = models.BooleanField(
        verbose_name="Ist Startpunkt",
        help_text="""Welcher Menüpunkt soll im Klassenzimmer als
            erstes angesprungen werden?""")

    objects = ClassroomMenuItemManager()

    unique_together=('display_title', 'courseevent')

    def is_classroom_link(self):
        """
        checks whether the menuitem links to anything in the classroom
        :return: True or False
        """
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

    def is_object_link(self):
        """
        checks whether the menuitem links to an object in the classroom
        :return: True or False
        """
        if self.item_type in [self.MENU_ITEM_TYPE.forum_item,
                              self.MENU_ITEM_TYPE.lesson_item,
                              self.MENU_ITEM_TYPE.homework_item,
                              ]:
            return True
        else:
            return False

    def save(self, *args, **kwargs):
        """
        menu item save method
        :param args:
        :param kwargs:
        :return:
        """
        if self.is_start_item:
            # there can only be one start-item per courseevent
            switch_start_item(self)

        if self.is_object_link:
            #set object to status published:
            switch_item_object_published_status(menuitem=self, publish=True)

        super(ClassroomMenuItem, self).save(*args, **kwargs)

    def delete(self):
        if self.is_object_link:
            if self.item_type == self.MENU_ITEM_TYPE.homework_item:
                if not self.homework.can_be_pulled_from_classroom:
                    raise ValidationError('''Die Aufgabe kann
                       nicht zurückgezogen werden, da sie schon in Berabeitung ist.''')
            elif self.item_type == self.MENU_ITEM_TYPE.lesson_item:
                    raise ValidationError('''Die Lektion kann
                       nicht zurückgezogen werden, da sich eine veröffentlichter
                       Aufgabe darauf bezieht.''')

            switch_item_object_published_status(menuitem=self, publish=False)
        super(ClassroomMenuItem, self).delete()

    def clean(self):
        """
        checks input in relation to item_type
        """
        # more helpful validations errors for the two main fields
        if not self.item_type:
           raise ValidationError('Bitte einen Eintragstyp wählen für den Menüeintrag!')
        if not self.display_nr:
           raise ValidationError('Bitte angeben an wievielter Stelle der Menüeintrag erscheinen soll!')

        # header item: not start_item, no relationships allowed
        if self.item_type == self.MENU_ITEM_TYPE.header_item:
            if self.is_start_item:
                raise ValidationError('Überschrift kann nicht Startpunkt sein!')

        # no object item: object link not allowed
        if not self.is_object_link:
                if self.classlesson or self.forum or self.homework:
                    raise ValidationError("""Eintragsart kann keinen Bezug zu einem Forum,
                                      einer Aufgabe oder einer Lektion haben.""")

        # lesson item: only relationships lesson, is required
        if self.item_type == self.MENU_ITEM_TYPE.lesson_item:
            if not self.classlesson:
                raise ValidationError('''Lektions-Eintrag muss zu einer Lektion verlinken.
                                      Bitte eine Lektion auswählen.''', code='invalid_object'
                                      )
            if self.forum or self.homework:
                raise ValidationError('''Bei Eintragstyp Lektion bitte nur eine Lektion
                                      als Link-Objekt angeben.''')

        # forum item: only relationships forum, is required
        if self.item_type == self.MENU_ITEM_TYPE.forum_item:
            if not self.forum:
                raise ValidationError('''Forum-Eintrag muss zu einem Forum verlinken.
                                      Bitte ein Forum auswählen.''')
            if self.classlesson or self.homework:
                raise ValidationError('Bei Eintragstyp Forum bitte nur Forum als Link-Objekt angeben.')

        # homework item: only relationships homework, is required
        # lesson must be published first
        if self.item_type == self.MENU_ITEM_TYPE.homework_item:
            if not self.homework:
                raise ValidationError('''Aufgaben-Eintrag muss zu einer Aufgabe verlinken.
                                      Bitte eine Aufgabe auswählen.''')
            if self.classlesson or self.forum:
                raise ValidationError('''Bei diesem Eintragstyp bitte nur eine Aufgabe als
                                      Link-Objekt auswählen.''')
            if not self.homework.classlesson.published:
                raise ValidationError('''Bitte zuerst die Lektion veröffentlichen,
                auf die sich die Aufgabe bezieht.''')


    def __unicode__(self):
        return u'%s: %s' % (self.get_item_type_display(), self.display_title)







