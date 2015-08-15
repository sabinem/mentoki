# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlesson',
            name='course',
            field=models.ForeignKey(to='course.Course', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='classlesson',
            name='original_lesson',
            field=models.ForeignKey(to='lesson.Lesson', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(to='course.Course', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
