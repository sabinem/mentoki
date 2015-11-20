# coding: utf-8


"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

import logging
logger = logging.getLogger(__name__)

from froala_editor.fields import FroalaField

from model_utils.models import TimeStampedModel

from apps_data.course.models.course import Course


class CourseProductGroupManager(models.Manager):
    """
    Querysets for CourseEvents
    """
    def published_by_mentor(self, user):
        return self\
            .filter(course__courseowner__user=user,
                    published=True)\
            .select_related('course')\
            .order_by('display_nr')

    def published(self):
        return self\
            .filter(published=True)\
            .select_related('course')\
            .order_by('display_nr')

    def book_now(self):
        return self\
            .filter(published=True,
                    can_be_booked_now=True)\
            .select_related('course')\
            .order_by('display_nr')

    def preview(self):
        return self\
            .filter(published=True,
                    can_be_booked_now=False)\
            .select_related('course')\
            .order_by('display_nr')


def foto_location(instance, filename):
        """
        location where the teachers foto is stored
        IN: CourseOwner, filename
        RETURN: path <course-slug>/<filename>
        """
        title = instance.course.title
        path = '/'.join([title, filename])
        logger.info("""[%s] [filename %s]:
                    Foto gespeichert unter %s"""
                    % (title,  filename, path))
        return path


class CourseProductGroup(TimeStampedModel):

    course = models.OneToOneField(Course)
    foto = models.ImageField(
        verbose_name=_('Foto'),
        help_text=_('''Hier kannst Du ein Foto für Deinen Kurs hochladen.'''),
        upload_to=foto_location, blank=True
    )
    in_one_sentence = models.CharField(
        verbose_name=_("in einem Satz"),
        help_text=_('beschreibe den Kurs in einem Satz'),
        max_length=250)

    meta_keywords_description = models.CharField(
        verbose_name=_('Meta Keywords'),
        default="Mentoki",
        help_text=_('HTML Meta Information zur Seite.'),
        max_length=250
    )
    meta_description_description = models.CharField(
        verbose_name=_('Meta Description'),
        default="Mentoki",
        help_text=_('HTML Meta Information zur Seite.'),
        max_length=250
    )
    meta_title_description = models.CharField(
        verbose_name=_('Meta Titel'),
        default="Mentoki",
        help_text=_('HTML Meta Information zur Seite.'),
        max_length=250
    )
    meta_keywords_offers = models.CharField(
        verbose_name=_('Meta Keywords'),
        default="Mentoki",
        help_text=_('HTML Meta Information zur Seite.'),
        max_length=250
    )
    meta_description_offers = models.CharField(
        verbose_name=_('Meta Description'),
        default="Mentoki",
        help_text=_('HTML Meta Information zur Seite.'),
        max_length=250
    )
    meta_title_offers  = models.CharField(
        verbose_name=_('Meta Titel'),
        default="Mentoki",
        help_text=_('HTML Meta Information zur Seite.'),
        max_length=250
    )
    meta_keywords_mentors = models.CharField(
        verbose_name=_('Meta Keywords'),
        default="Mentoki",
        help_text=_('HTML Meta Information zur Seite.'),
        max_length=250
    )
    meta_description_mentors = models.CharField(
        verbose_name=_('Meta Description'),
        default="Mentoki",
        help_text=_('HTML Meta Information zur Seite.'),
        max_length=250
    )
    meta_title_mentors = models.CharField(
        verbose_name=_('Meta Titel'),
        default="Mentoki",
        help_text=_('HTML Meta Information zur Seite.'),
        max_length=250
    )

    published = models.BooleanField(default=False)
    can_be_booked_now = models.BooleanField(default=False)
    display_nr = models.IntegerField(default=1)

    slug = models.SlugField(default="x")
    title = models.CharField(max_length=100, default="x")
    conditions = FroalaField()
    about = FroalaField()
    mentors = FroalaField()
    discount_text = models.CharField(max_length=100, blank=True, default="")
    discount_text_long = models.CharField(max_length=200, blank=True, default="")

    objects = CourseProductGroupManager()

    class Meta:
        verbose_name = _("Kursproduktgruppe")
        verbose_name_plural = _("Kursproduktgruppen")

    def __unicode__(self):
        return self.course.title

    def get_absolute_url(self):
        return reverse_lazy('storefront:offer',
                       kwargs={'slug': self.slug})



class CourseProductSubGroup(TimeStampedModel):
    """
    These are courseproducts that can not be bought together since they are
    paralell to each other, for example the same courseevent starting at
    different dates
    """
    name = models.CharField(max_length=250)
    course = models.ForeignKey(Course)
    courseproductgroup = models.ForeignKey(CourseProductGroup, default=1)

    class Meta:
        verbose_name = _("Kursproduktuntergruppe")
        verbose_name_plural = _("Kursproduktuntergruppen")

    def __unicode__(self):
        return self.name