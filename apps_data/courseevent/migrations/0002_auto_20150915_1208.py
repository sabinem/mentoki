# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseevent', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentswork',
            name='homework',
            field=models.ForeignKey(verbose_name='Aufgabe', to='lesson.ClassLesson'),
        ),
        migrations.AddField(
            model_name='studentswork',
            name='workers',
            field=models.ManyToManyField(related_name='teammembers', verbose_name='Team', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(related_name='post_author', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(to='courseevent.Thread', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='forum',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
        migrations.AddField(
            model_name='forum',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='einh\xe4ngen unter', blank=True, to='courseevent.Forum', null=True),
        ),
        migrations.AddField(
            model_name='courseeventparticipation',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
        migrations.AddField(
            model_name='courseeventparticipation',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='course',
            field=models.ForeignKey(to='course.Course', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='participation',
            field=models.ManyToManyField(related_name='participation', through='courseevent.CourseEventParticipation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
        migrations.AddField(
            model_name='comment',
            name='studentswork',
            field=models.ForeignKey(to='courseevent.StudentsWork'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='classlesson',
            field=models.ForeignKey(related_name='lesson', on_delete=django.db.models.deletion.PROTECT, blank=True, to='lesson.ClassLesson', null=True),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='courseevent.Forum', null=True),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='homework',
            field=models.ForeignKey(related_name='homework', on_delete=django.db.models.deletion.PROTECT, blank=True, to='lesson.ClassLesson', null=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='courseevent',
            field=models.ForeignKey(related_name='courseeventnews', to='courseevent.CourseEvent'),
        ),
    ]
