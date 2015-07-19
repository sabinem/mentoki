# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0054_auto_20150719_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='title', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
