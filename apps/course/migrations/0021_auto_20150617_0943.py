# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_auto_20150616_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
