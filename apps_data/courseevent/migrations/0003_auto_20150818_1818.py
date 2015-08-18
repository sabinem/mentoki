# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
        ('courseevent', '0002_auto_20150818_1818'),
        ('forum', '0002_auto_20150818_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='classlesson',
            field=models.ForeignKey(verbose_name='Bezug auf einen Lernabschnitt?', blank=True, to='lesson.ClassLesson', null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
        migrations.AddField(
            model_name='forum',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
        migrations.AddField(
            model_name='forum',
            name='oldforum',
            field=models.ForeignKey(blank=True, to='forum.Forum', null=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='oldsubforum',
            field=models.ForeignKey(related_name='Unterforum_alt', blank=True, to='forum.SubForum', null=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='einh\xe4ngen unter', blank=True, to='courseevent.Forum', null=True),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='classlesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='lesson.ClassLesson', null=True),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='courseevent.Homework', null=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='courseevent',
            field=models.ForeignKey(related_name='courseeventnews', to='courseevent.CourseEvent'),
        ),
    ]
