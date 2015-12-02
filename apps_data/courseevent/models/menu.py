# coding: utf-8

"""
Teachers establish their own menu for the courseevent for their class.
This classroom-menu is stored in the model ClassroomMenuItem.

Objects are only visible in the class once they are put into the menu.
In that way the menu influnces what is published in the class, but this
information is "soft". It is not stored in the objects, whether they are
accessible or not. Rather they have to look for themselves wether a menu entry
exists for them or not.

There a re two menus: a complete menu with everything published so far and
a shortlinksmenu for the most important items at any time.

Also the start item can be chosen: the item that is shown first when
students enter the classroom.
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError

from model_utils import Choices
from model_utils.models import TimeStampedModel
from model_utils.managers import QueryManager

from fontawesome.fields import IconField
from .courseevent import CourseEvent
from .forum import Forum
from apps_data.lesson.models.classlesson import ClassLesson


def switch_start_item(menuitem):
    """
    The start item of a courseevent is changed to a given new menuitem
    """
    menuitems = ClassroomMenuItem.objects.all_for_courseevent(courseevent=menuitem.courseevent).\
        exclude(pk=menuitem.pk)
    for item in menuitems:
        item.is_start_item = False
        item.save()


class ClassroomMenuItemManager(models.Manager):

    def all_for_courseevent(self, courseevent):
        """
        get all menu-items for a courseevent
        """
        return self.filter(courseevent=courseevent).order_by('display_nr')

    def shortlinks_for_courseevent(self, courseevent):
        """
        get all menuitems that are shortlinks for a courseevent
        """
        return self.filter(courseevent=courseevent, is_shortlink=True).order_by('display_nr')

    def lessons_published_in_class(self, courseevent):
        """
        get flat list of lesson ids that are published in class
        """
        return self.filter(courseevent=courseevent,
                           item_type__in=['lesson'],
                           ).select_related('classlesson')

    def forums_published_in_class(self, courseevent):
        """
        get flat list of lesson ids that are published in class
        """
        return self.filter(courseevent=courseevent,
                           item_type__in=['forum'],
                           ).select_related('forum')

    def lesson_ids_published_in_class(self, courseevent):
        """
        get flat list of lesson ids that are published in class
        """
        return self.filter(courseevent=courseevent,
                           item_type__in=['lessonstep', 'lesson'],
                           ).values_list('classlesson_id', flat=True)

    def homeworks_published_in_class(self, courseevent):
        """
        get flat list of lesson ids that are published in class
        """
        ids = self.filter(courseevent=courseevent,
                           item_type__in=['lessonstep', 'lesson'],
                           ).values_list('classlesson_id', flat=True)
        return ClassLesson.objects.filter(id__in=ids).get_descendants(include_self=True).\
            filter(level=3, is_homework=True)

    def forum_ids_published_in_class(self, courseevent):
        """
        get flat list of forum ids that are published in class
        """
        return self.filter(courseevent=courseevent,
                           item_type__in=['forum'],
                           ).values_list('forum_id', flat=True)


    def lessonsteps_for_courseevent(self, courseevent):
        """
        get all homeworks that are published in class
        """
        return self.filter(courseevent=courseevent,
                           item_type='lessonstep'
                           ).order_by('display_nr')

    def lessons_for_courseevent(self, courseevent):
        """
        get all lessons that are published in class
        """
        return self.filter(courseevent=courseevent,
                           item_type='lesson'
                           ).order_by('display_nr')

    def forums_for_courseevent(self, courseevent):
        """
        get all homeworks that are published in class
        """
        return self.filter(courseevent=courseevent,
                           item_type='forum'
                           ).order_by('display_nr')

    def listlinks_for_courseevent(self, courseevent):
        """
        get all menuitems that are links to a list
        """
        return self.filter(courseevent=courseevent,
                           item_type__in = [
                               'last_posts',
                               'participants',
                               'announcements',
                           ]
                           ).order_by('display_nr')

    def get_startitem_from_slug(self, slug):
        """
        get the startitem for the courseevent: there should always
        be 1 or 0 startitems
        """
        return self.get(courseevent__slug=slug, is_start_item=True )

    def create(self,
               courseevent,
               display_title,
               display_nr,
               item_type,
               classlesson=None,
               forum=None,
               is_start_item=False,
               is_shortlink=False,
               icon=None):
        """
        create a menu item from the given data
        """
        menuitem = ClassroomMenuItem(
            courseevent=courseevent,
            classlesson=classlesson,
            forum=forum,
            display_title=display_title,
            display_nr=display_nr,
            is_shortlink=is_shortlink,
            item_type=item_type,
            is_start_item=is_start_item,
            icon=icon
        )
        menuitem.save()
        return menuitem


class ClassroomMenuItem(TimeStampedModel):
    """
    Classroom Menu Items make up the Classroom Menu
    dependent on courseevent

    ClassLessons and Classlessonsteps may be published in the class through
    an entry in the menu. The same is true for forums.

    Also certain links may be published that way:
    - link to particpant list
    - link to latest forum contributions
    """
    courseevent = models.ForeignKey(CourseEvent)

    classlesson = models.ForeignKey(
        ClassLesson,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="lesson"
    )
    forum = models.ForeignKey(
        Forum,
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    icon = IconField(verbose_name="Icon",
                     help_text="Neben dem Menüeintrag kann ein Icon angezeigt werden.")
    MENU_ITEM_TYPE = Choices(
                     ('header', 'header_item', _('Überschrift')),
                     ('lesson', 'lesson_item',  _('Lektion')),
                     ('lessonstep', 'lessonstep_item', _('Lernschritt')),
                     ('forum', 'forum_item', _('Forum')),
                     ('last_posts', 'last_posts_item', _('Forum: neueste Beiträge')),
                     ('announcements', 'announcements_item', _('Ankündigungsliste')),
                     ('private', 'private_item', _('Privatbereich der Kursteilnehmer')),
                     ('participants', 'participants_item', _('Teilnehmerliste')),
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

    display_nr = models.IntegerField(
        verbose_name="Reihenfolge Nummer",
        help_text="""An welcher Position im Menü soll der Menüpunkt angezeigt werden?""",
    )
    display_title = models.CharField(max_length=200)

    is_start_item = models.BooleanField(
        verbose_name="Ist Startpunkt",
        help_text="""Welcher Menüpunkt soll im Klassenzimmer als
            erstes angesprungen werden?""",
        default=False)

    objects = ClassroomMenuItemManager()
    shortlinks = QueryManager(is_shortlink=True).order_by('display_nr')

    unique_together=('display_title', 'courseevent')

    class Meta:
        verbose_name = _("Menüeintrag")
        verbose_name_plural = _("Menüeinträge")

    def __unicode__(self):
        return u'%s' % (self.display_title)

    def save(self, *args, **kwargs):
        """
        menu item save method
        if the saved item is a start item, the start item must be switched to
        the current item, since there can be no more then one startitem
        per courseevent.
        """
        if self.is_start_item:
            switch_start_item(self)
        super(ClassroomMenuItem, self).save(*args, **kwargs)

    def clean(self):
        """
        checks input in relation to item_type
        1. header items cannot be shortlinks or startitems, since they are no
        links
        2. lesson_item: relation to lesson is required
        3. lessonstep_item: relation to lesson_step is required
        4. forum_item: relationship to forum is required
        """
        # 1. header item: not start_item, no relationships allowed
        if self.item_type == self.MENU_ITEM_TYPE.header_item:
            if self.is_start_item:
                raise ValidationError('Überschrift kann nicht Startpunkt sein!')
            if self.is_shortlink:
                raise ValidationError('Überschrift kann nicht ins Kurzmenü eingehägt werden!')

        # 2. lesson item: only relationship to lesson is required
        if self.item_type == self.MENU_ITEM_TYPE.lesson_item:
            if self.classlesson:
                if not self.classlesson.is_lesson():
                    raise ValidationError('''Lektions-Eintrag muss zu einer Lektion
                    verlinken.''', code='invalid_object'
                    )
            if self.forum:
                raise ValidationError('''Bei diesem Eintragstyp
                kann kein Forum angegeben werden.''')

        # 3. lessonstep item: only relationship to lessonstep  is required
        if self.item_type == self.MENU_ITEM_TYPE.lessonstep_item:
            if self.classlesson:
                if not self.classlesson.is_step():
                    raise ValidationError('''Lernschritt-Eintrag muss zu einem
                    Lernabschnitt verlinken.''', code='invalid_object'
                    )
            if self.forum:
                raise ValidationError('''Bei diesem Eintragstyp
                kann kein Forum angegeben werden.''')

        # 4. forum_item: only relationships forum, is required
        if self.item_type == self.MENU_ITEM_TYPE.forum_item:
            if not self.forum:
                raise ValidationError(
                    '''Forum-Eintrag muss zu einem Forum verlinken.
                    Bitte ein Forum auswählen.''')
            if self.classlesson:
                raise ValidationError(
                    '''Bei Eintragstyp kann keine Lektion
                    angegeben werden.''')








