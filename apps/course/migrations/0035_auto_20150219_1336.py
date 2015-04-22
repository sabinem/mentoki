# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0034_auto_20150219_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(default=b'x', upload_to=b'lessonmaterial', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='slug',
            field=models.SlugField(blank=True),
            preserve_default=True,
        ),
    ]
