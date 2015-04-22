# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0038_auto_20150223_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursematerialunit',
            name='fileslug',
            field=autoslug.fields.AutoSlugField(editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=b'lesson_material_name', blank=True),
            preserve_default=True,
        ),
    ]
