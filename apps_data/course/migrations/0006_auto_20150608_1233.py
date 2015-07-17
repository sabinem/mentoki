# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20150607_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='description',
            field=models.CharField(max_length=200, verbose_name='kurze Beschreibung', blank=True),
        ),
        migrations.AddField(
            model_name='material',
            name='title',
            field=models.CharField(default='x', unique=True, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
