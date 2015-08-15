# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_auto_20150814_0703'),
        ('courseevent', '0042_auto_20150814_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroommenuitem',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='homework',
            name='lesson',
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='classlesson',
            field=models.ForeignKey(blank=True, to='lesson.ClassLesson', null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='classlesson',
            field=models.ForeignKey(verbose_name='Bezug auf einen Lernabschnitt?', blank=True, to='lesson.ClassLesson', null=True),
        ),
    ]
