# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property
from mentoki import settings

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField, StatusField
from model_utils import Choices

from apps_data.lesson.models.classlesson import ClassLesson

from .courseevent import CourseEvent


class HomeworkManager(models.Manager):

    def homeworks_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent)

    def published_homework_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent, published=True).\
            order_by('due_date').\
            select_related('lesson')

    def unpublished_per_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent, published=False).\
            order_by('published', 'due_date').select_related('lesson')

    def create(self, courseevent, text, title, due_date=None, lesson=None):
        homework = Homework(courseevent=courseevent,
                                classlesson=lesson,
                                text=text,
                                title=title,
                                published=False,
                                due_date=due_date)
        homework.save()
        return homework

def limit_courseevent_choice():
    return


class Homework(TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)

    classlesson = models.ForeignKey(ClassLesson,
                               verbose_name="Bezug auf einen Lernabschnitt?",
                               null=True, blank=True)

    title = models.CharField(verbose_name="Überschrift", max_length=100)
    text = models.TextField(verbose_name="Text")

    published = models.BooleanField(verbose_name="veröffentlichen",
                                    default=False)
    publish_status_changed = MonitorField(monitor='published')

    hidden = models.BooleanField(
        verbose_name=_('versteckt'),
        default=False)
    hidden_status_changed = MonitorField(monitor='hidden')

    due_date = models.DateField(blank=True, null=True)
    objects = HomeworkManager()

    def __unicode__(self):
        return self.title

    @cached_property
    def course_slug(self):
        return self.courseevent.course_slug

    @cached_property
    def slug(self):
        return self.courseevent.slug

    def get_absolute_url(self):
        return reverse('coursebackend:homework:detail',
                       kwargs={'course_slug':self.course_slug,
                               'slug':self.slug,
                               'pk':self.pk})

    def get_classroom_url(self):
        return reverse('classroom:homework:list',
               kwargs={'slug':self.slug,
                       'pk':self.pk})



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
    workers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='teammembers')
    homework = models.ForeignKey(Homework)

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

    def get_absolute_url(self):
        return reverse('classroom:studentswork:detail',
                       kwargs={'slug':self.slug,
                               'pk':self.pk})