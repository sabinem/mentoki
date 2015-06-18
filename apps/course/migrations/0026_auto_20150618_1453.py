# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0025_auto_20150617_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentblock',
            name='course',
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='nr',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='ContentBlock',
        ),
    ]
