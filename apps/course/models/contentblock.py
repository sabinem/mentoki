# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property

from model_utils.models import TimeStampedModel

from ..managers import CourseBlockQuerySet
from .course import Course

class ContentBlock(TimeStampedModel):

    course  = models.ForeignKey(Course, verbose_name='Kurs')

    title = models.CharField(max_length=100, verbose_name='Ueberschrift')
    description = models.CharField(max_length=200, blank=True, verbose_name='kurze Beschreibung')
    text = models.TextField(blank=True, verbose_name='Beschreibung')
    status = models.TextField(blank=True,verbose_name='Status')


    class Meta:
        verbose_name = "Unterrichtsblock"
        verbose_name_plural = "Unterrichtsblöcke"

    def __unicode__(self):
        return u'%s/%s' % (self.course, self.title)

    @cached_property
    def course_slug(self):
        return self.course.slug

    def get_absolute_url(self):
        return reverse('course:blockdetail', kwargs={'block':self.pk, 'course_slug': self.course_slug })
