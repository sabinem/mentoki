# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from mentoki import settings

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField

from apps_data.lesson.models.classlesson import ClassLesson

from .courseevent import CourseEvent


class StudentsWorkManager(models.Manager):

    def turnedin_homework(self, homework):
        return self.filter(homework=homework, published=True).order_by('published_at')

    def mywork(self, user, courseevent):
        return self.filter(courseevent=courseevent, workers=user).select_related('homework').order_by('created')

    def create(self, courseevent, homework, text, title, user):
        studentswork = StudentsWork(courseevent=courseevent,
                                    homework=homework,
                                    text=text,
                                    title=title)
        studentswork.save()
        studentswork.workers.add(user)
        return studentswork

class StudentsWork(TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)
    workers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     verbose_name="Team",
                                     related_name='teammembers')
    homework = models.ForeignKey(ClassLesson)

    title = models.CharField(verbose_name="Titel", max_length=100)
    text = models.TextField(verbose_name="Text")
    comments = models.TextField(verbose_name="Kommentare", blank=True)

    published = models.BooleanField(verbose_name="veröffentlichen", default=False)
    published_at = MonitorField(monitor='published', when=[True])

    objects = StudentsWorkManager()

    def __unicode__(self):
        return self.title

    def team(self):
        """
        Returns all the accounts of users who are students in the courseevent
        """
        return self.workers.all().order_by('username').prefetch_related('teammembers')

    def team_size(self):
        return self.team.count()

    def get_absolute_url(self):
        return reverse('classroom:studentswork:detail',
                       kwargs={'slug':self.slug,
                               'pk':self.pk})


class CommentManager(models.Manager):

    def comment_to_studentswork(self, studentswork):
        return self.filter(studentswork=studentswork).order_by('created')

    def create_comment(self, courseevent, text, title, author, studentswork):
        comment = Comment(
            courseevent=courseevent, studentswork=studentswork,
            text=text, title=title, author=author)
        comment.save()
        return comment



class Comment(TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    studentswork = models.ForeignKey(StudentsWork)

    title = models.CharField(verbose_name="Titel", max_length=100)
    text = models.TextField(verbose_name="Text")

    objects = CommentManager()

    def __unicode__(self):
        return self.title

