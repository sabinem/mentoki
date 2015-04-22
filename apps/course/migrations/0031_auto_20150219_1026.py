# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0030_auto_20150213_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(null=True, upload_to=b'lessonmaterial', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='slug',
            field=models.SlugField(default="x"),
            preserve_default=True,
        ),
    ]
