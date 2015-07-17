# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.core.urlresolvers import reverse
from apps_data.courseevent.models import CourseEvent
from django_markdown.models import MarkdownField
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from .querysets import NewsletterQuerySet



class Newsletter(TimeStampedModel):
    """
    Newsletters are appear once a month
    """
    title = models.CharField(max_length=100, verbose_name="Thema")
    # abstract that appears on the list page for newsletters
    excerpt =  models.TextField(verbose_name='Abstrakt', blank=True)
    # slug for the newsletter
    slug = AutoSlugField(populate_from='title')
    # content of the newsletter
    content = MarkdownField(verbose_name='Text', blank=True)
    # is the newsletter published?
    published = models.BooleanField(default=False, verbose_name="jetzt veröffentlichen?")
    # if published: this contains the date of publication
    published_at_date = models.DateTimeField(null=True, blank=True,
                                             verbose_name="veröffentlicht am")

    objects = NewsletterQuerySet.as_manager()

    class meta:
        verbose_name = "Der Mentoki Newletter"
        verbose_name_plural = "Die Mentoki Newletter"
        ordering = ['published_at_date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newsletter:detail', kwargs={'slug':self.slug})
