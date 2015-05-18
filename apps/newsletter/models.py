# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.core.urlresolvers import reverse
from apps.courseevent.models import CourseEvent
from django_markdown.models import MarkdownField


class Tag(models.Model):
     slug = models.SlugField(max_length=100, unique=True)

     def __unicode__(self):
         return self.slug



class NewsletterQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)


class Newsletter(models.Model):
    """
    Newsletters are appear once a month
    """
    title = models.CharField(max_length=100, verbose_name="Thema")
    # abstract that appears on the list page for newsletters
    excerpt = models.TextField(verbose_name="Abstract", default="x")
    # left newsletter column
    slug = models.SlugField(max_length=100, unique=True)
    content = MarkdownField()
    # right newsletter column
    published = models.BooleanField(default=False, verbose_name="jetzt veröffentlichen?")
    # if published: this contains the date of publication
    published_at_date = models.DateTimeField(null=True, blank=True,
                                             verbose_name="veröffentlicht am")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    objects = NewsletterQuerySet.as_manager()

    class meta:
        verbose_name = "Der Mentoki Newletter"
        verbose_name_plural = "Die Mentoki Newletter"
        ordering = ['created']


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newsletters:single', kwargs={'slug':self.slug})
