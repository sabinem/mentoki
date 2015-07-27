# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0062_auto_20150724_1548'),
        ('courseevent', '0014_auto_20150724_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='lesson',
            field=models.ForeignKey(blank=True, to='course.Lesson', null=True),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='item_type',
            field=models.CharField(max_length=15, choices=[('forum', 'Forum'), ('lesson', 'Unterricht'), ('anouncements', 'Ank\xfcndigungen'), ('homework', 'homework'), ('last_posts', 'latest forum posts'), ('private', 'students private place')]),
        ),
    ]
