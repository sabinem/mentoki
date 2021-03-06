# coding: utf-8

from __future__ import unicode_literals, absolute_import

from apps_data.lesson.models.classlesson import ClassLesson

from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.conf import settings

from django_enumfield import enum

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField

from apps_data.courseevent.models.courseevent import CourseEvent
from ..constants import FeedbackSpice



class StudentsWorkManager(models.Manager):

    def turnedin_homework_count(self, classlesson):
        self.filter(homework=classlesson, published=True).count()

    def turnedin_homework(self, homework):
        return self.filter(homework=homework, published=True).order_by('-published_at')

    def unpublished_homework(self, homework, user):
        return self.filter(homework=homework, published=False,
                           workers=user)\
            .select_related('homework').order_by('-created')

    def turnedin_homework_courseevent(self, courseevent, user):
        return self.filter(courseevent=courseevent, published=True,
                           workers=user).order_by('-published_at')

    def unpublished_homework_courseevent(self, courseevent, user):
        return self.filter(courseevent=courseevent, published=False,
                           workers=user)\
            .select_related('homework').order_by('-created')

    def mywork(self, user, courseevent):
        return self.filter(courseevent=courseevent, workers=user).select_related('homework').order_by('created')

    def create(self, courseevent, homework, text, title, user, published, publish_count=0):
        studentswork = StudentsWork(courseevent=courseevent,
                                    homework=homework,
                                    text=text,
                                    published=published,
                                    publish_count=publish_count,
                                    title=title)
        if published:
            studentswork.publish_count = 1
        studentswork.save()
        studentswork.workers.add(user)
        return studentswork

class StudentsWork(TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)
    workers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     verbose_name="Team",
                                     related_name='teammembers')
    homework = models.ForeignKey(ClassLesson,
                                 verbose_name="Aufgabe")

    title = models.CharField(
        verbose_name="Titel",
        max_length=100)
    text = models.TextField(
        verbose_name="Text")
    comments = models.TextField(
        verbose_name="Kommentare",
        blank=True)
    feedback_spice = enum.EnumField(FeedbackSpice, default=FeedbackSpice.MEDIUM)
    published = models.BooleanField(verbose_name="veröffentlichen", default=False)
    published_at = MonitorField(monitor='published', when=[True])

    publish_count = models.IntegerField(default=0)
    republished_at = MonitorField(monitor='publish_count')

    objects = StudentsWorkManager()

    class Meta:
        verbose_name = _("Teilnehmer-Arbeit")
        verbose_name_plural = _("Teilnehmer-Arbeiten")

    def __unicode__(self):
        return self.title

    def team(self):
        """
        Returns all the accounts of users who are students in the courseevent
        """
        return self.workers.all().order_by('username').prefetch_related('teammembers')

    def team_display(self):
        """
        Returns all the accounts of users who are students in the courseevent
        """
        teachers = self.team
        namesstring = ""
        for worker in self.workers.all():
            if namesstring != "":
                namesstring += ", "
            namesstring += worker.get_full_name()
        return namesstring

    def workers_emails(self):
        return self.workers.all().values_list('email', flat=True, )

    def comment_count(self):
        return Comment.objects.filter(studentswork=self).count()

    def team_size(self):
        return self.team.count()

    #def get_absolute_url(self):
    #    return reverse('classroom:studentswork:detail',
    #                   kwargs={'slug':self.slug,
    #                           'pk':self.pk})


class CommentManager(models.Manager):

    def comment_to_studentswork(self, studentswork):
        return self.filter(studentswork=studentswork).order_by('created')

    def commentors_emails(self, studentswork):
        return set(self.filter(studentswork=studentswork).select_related('author')\
            .values_list('author__email', flat=True))

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

    class Meta:
        verbose_name = _("Kommentar")
        verbose_name_plural = _("Kommentare")

    def __unicode__(self):
        return self.title

