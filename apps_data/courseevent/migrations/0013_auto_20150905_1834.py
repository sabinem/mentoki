# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0012_auto_20150905_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='classlesson',
        ),
        migrations.RemoveField(
            model_name='homework',
            name='courseevent',
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='classlesson',
            field=models.ForeignKey(related_name='lesson', on_delete=django.db.models.deletion.PROTECT, blank=True, to='lesson.ClassLesson', null=True),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='homework',
            field=models.ForeignKey(related_name='homework', on_delete=django.db.models.deletion.PROTECT, blank=True, to='lesson.ClassLesson', null=True),
        ),
        migrations.AlterField(
            model_name='studentswork',
            name='homework',
            field=models.ForeignKey(to='lesson.ClassLesson'),
        ),
        migrations.DeleteModel(
            name='Homework',
        ),
    ]
