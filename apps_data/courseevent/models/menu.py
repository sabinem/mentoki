# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError

from model_utils import Choices
from model_utils.models import TimeStampedModel
from model_utils.managers import QueryManager

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


def switch_item_forum_published_status(forum, publish):
        if publish == True:
            forum.publish()
        else:
            forum.unpublish()

def switch_item_lesson_published_status(classlesson, publish):
        if publish == True:
            classlesson.publish()
        else:
            classlesson.unpublish()


class ClassroomMenuItemManager(models.Manager):

    def all_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent).order_by('display_nr')

    def published_for_courseevent(self, courseevent, is_publishlink=True):
        return self.filter(courseevent=courseevent).order_by('display_nr')

    def shortlinks_for_courseevent(self, courseevent, is_shortlink=True):
        return self.filter(courseevent=courseevent).order_by('display_nr')



    def homeworks_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent,
                           item_type='homework'
                           ).order_by('display_nr')

    def lessons_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent,
                           item_type='lesson'
                           ).order_by('display_nr')

    def forums_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent,
                           item_type='forum'
                           ).order_by('display_nr')

    def listlinks_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent,
                           item_type__in = [
                               'last_posts',
                               'participants',
                               'announcements',
                           ]
                           ).order_by('display_nr')

    def active_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent, active=True).order_by('display_nr')

    def get_startitem_from_slug(self, slug):
        return self.get(courseevent__slug=slug, is_start_item=True )

    def create(self, courseevent, homework, classlesson, forum, display_title,
               display_nr, item_type, is_start_item, is_shortlink):
        menuitem = ClassroomMenuItem(
            courseevent=courseevent,
            homework=homework,
            classlesson=classlesson,
            forum=forum,
            display_title=display_title,
            display_nr=display_nr,
            is_shortlink=is_shortlink,
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


    MENU_ITEM_TYPE = Choices(('forum', 'forum_item', _('Forum: Forum wird publiziert')),
                     ('lesson', 'lesson_item',  _('Unterricht: Lektion wird publiziert ')),
                     ('announcements', 'announcements_item', _('Link zu Ankündigungsliste')),
                     ('homework', 'homework_item', _('Link zu einer Hausaufgabe')),
                     ('last_posts', 'last_posts_item', _('Link zu den neuesten Beiträge')),
                     ('private', 'private_item', _('Link zum Privatbereich der Kursteilnehmer')),
                     ('header', 'header_item', _('Überschrift')),
                     ('participants', 'participants_item', _('Link zur Teilnehmerliste')),
                    )
    item_type = models.CharField(
        verbose_name="Typ des Menüpunkts",
        help_text="""Welcher Art ist der Menüeintrag: Überschrift, Link, etc?""",
        choices=MENU_ITEM_TYPE,
        max_length=15)

    is_shortlink = models.BooleanField(
        verbose_name='Kurzlink',
        help_text="""die wichtigsten Links werden als Kurzlinks angezeigt.
        Es sollte nicht mehr als 10 Kurzlinks geben""",
        default=False)

    is_publishlink = models.BooleanField(
        verbose_name='publishlink',
        help_text="""Links deren setzen Objekte im Klassenzimmer veröffentlicht.
        Das ist bei Lektionen und Foren der Fall""",
        default=True)

    is_listlink = models.BooleanField(
        verbose_name='Liste',
        help_text="""Links deren setzen Objekte im Klassenzimmer veröffentlicht.
        Das ist bei Lektionen und Foren der Fall""",
        default=True)

    is_forumlink = models.BooleanField(
        verbose_name='Forum',
        help_text="""Links deren setzen Objekte im Klassenzimmer veröffentlicht.
        Das ist bei Lektionen und Foren der Fall""",
        default=False)

    is_lessonlink = models.BooleanField(
        verbose_name='Lektion',
        help_text="""Links deren setzen Objekte im Klassenzimmer veröffentlicht.
        Das ist bei Lektionen und Foren der Fall""",
        default=False)

    is_homeworklink = models.BooleanField(
        verbose_name='Aufgabe',
        help_text="""Links deren setzen Objekte im Klassenzimmer veröffentlicht.
        Das ist bei Lektionen und Foren der Fall""",
        default=False)

    active = models.BooleanField(default=True)
    optional = models.BooleanField(default=True)

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
    published = QueryManager(is_publishlink=True).order_by('display_nr')
    shortlinks = QueryManager(is_shortlink=True).order_by('display_nr')

    unique_together=('display_title', 'courseevent')

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

        if self.forum:
            self.is_forumlink = True
            switch_item_forum_published_status(forum=self.forum,
                                               publish=True)

        elif self.classlesson:
            self.is_lessonlink = True
            switch_item_lesson_published_status(classlesson=self.classlesson,
                                                publish=True)
        elif self.homework:
            self.is_homeworklink = True

        super(ClassroomMenuItem, self).save(*args, **kwargs)

    def delete_possible(self):
        if self.is_listlink:
            return True
        elif self.item_type == self.MENU_ITEM_TYPE.header_item:
            return True
        if self.is_homeworklink:
            return True
        if self.is_forumlink:
            if not self.forum.used:
                return True
        if self.is_lessonlink:
            if not self.classlesson.used:
                return True
        return False

    def delete(self):
        #if not self.delete_possible():
        #    raise ValidationError('Löschung nicht möglich')
        if self.forum:
            self.forum.unpublish()
        if self.classlesson:
            self.classlesson.unpublish()
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
        if self.is_forumlink:
            return u'Forum: %s' % (self.forum.title)
        elif self.is_homeworklink:
            return u'Aufgabe: %s' % (self.homework.title)
        elif self.is_lessonlink:
            return u'Lektion: %s' % (self.classlesson.title)
        elif self.is_listlink:
            return u'%s' % (self.get_item_type_display)
        elif self.header_item:
            return u'%s' % (self.display_title)







