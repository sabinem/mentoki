# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20150606_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='description',
            field=models.CharField(max_length=200, verbose_name='kurze Beschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
