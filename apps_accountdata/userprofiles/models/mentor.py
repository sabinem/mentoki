# coding: utf-8

"""
Mentors are users that teach courses.
Here are their profile data stored. These data are
displayed on public pages.
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

from model_utils.models import TimeStampedModel

from autoslug.fields import AutoSlugField

from froala_editor.fields import FroalaField

from apps_data.course.models.course import Course
from apps_productdata.mentoki_product.models.courseproductgroup \
    import CourseProductGroup

import logging
logger = logging.getLogger('data.userprofile')


class MentorsProfileManager(models.Manager):
    def mentors_all(self):
        """
        gets all mentors ordered, including their user data
        :return: mentors queryset
        """
        return self.all()\
            .select_related('user').\
            order_by('display_nr')


def foto_location(instance, filename):
        """
        location where the teachers foto is stored
        IN: mentor instance, filename
        RETURN: path <course-slug>/<filename>
        """
        path = '/'.join([instance.user.username, filename])
        logger.info("""[%s] [filename %s]:
                    Foto gespeichert unter %s"""
                    % (instance.user,  filename, path))
        return path


class MentorsProfile(TimeStampedModel):
    """
    Mentor is the role of teaching at mentoki
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Mentor"),
        on_delete=models.PROTECT
    )
    slug = AutoSlugField(
        populate_from='get_full_name'
    )

    at_mentoki = models.CharField(
        verbose_name=_('Rolle bei Mentoki'),
        blank=True,
        max_length=250,
    )
    special_power = models.CharField(
        verbose_name=_('Spezielle Eigenschaft'),
        blank=True,
        max_length=250,
    )
    course_short = models.CharField(
        verbose_name=_('Kurzbeschreibung'),
        blank=True,
        max_length=250,
    )
    text = FroalaField(
        verbose_name=_('ausführliche Beschreibung'),
        blank=True
    )
    foto = models.ImageField(
        verbose_name=_('Foto'),
        help_text=_('''Hier kannst Du ein Foto von Dir hochladen.
                     Dieses Foto ist für die Listenansicht gedacht'''),
        upload_to=foto_location, blank=True
    )
    foto_detail_page = models.ImageField(
        verbose_name=_('Foto'),
        help_text=_('''Hier kannst Du ein Foto von Dir hochladen.
                    Dieses Foto ist für die Detailseite gedacht'''),
        upload_to=foto_location, blank=True
    )
    display_nr = models.IntegerField(
        verbose_name=_('Anzeigereihenfolge'),
    )
    meta_title_mentors = models.CharField(
        verbose_name=_('Meta Titel'),
        default="Mentoki",
        max_length=250
    )
    meta_description_mentors = models.CharField(
        verbose_name=_('Meta Description'),
        default="Mentoki",
        max_length=250
    )
    meta_keywords_mentors = models.CharField(
        verbose_name=_('Meta Keywords'),
        default="Mentoki",
        max_length=250
    )
    is_ready = models.BooleanField(
        verbose_name="fertig",
        default=False
    )

    objects = MentorsProfileManager()

    class Meta:
        verbose_name = _("Mentor")
        verbose_name_plural = _("Mentoren")

    def __unicode__(self):
        """
        The courseownership is shown as <course> <user>
        RETURN: ownership record representation
        """
        return u'%s' % (self.user)

    def get_absolute_url(self):
        return reverse_lazy('home:mentor',
                       kwargs={'slug': self.slug})

    def teaching(self):
        return Course.objects.filter(courseowner__user=self.user)

    def productgroups(self):
        return CourseProductGroup.objects.filter(
            course__in=self.teaching)

    @property
    def get_full_name(self):
        return self.user.get_full_name()
