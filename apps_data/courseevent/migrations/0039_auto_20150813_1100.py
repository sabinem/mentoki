# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0038_auto_20150813_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroommenuitem',
            name='lesson',
            field=models.ForeignKey(blank=True, to='lesson.ClassLesson', null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='lesson',
            field=models.ForeignKey(verbose_name='Bezug auf einen Lernabschnitt?', blank=True, to='lesson.ClassLesson', null=True),
        ),
    ]
