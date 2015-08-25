# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_auto_20150823_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='publish_status_changed',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='published',
        ),
        migrations.AlterField(
            model_name='classlesson',
            name='original_lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='lesson.Lesson', null=True),
        ),
    ]
