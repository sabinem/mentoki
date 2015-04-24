# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0053_course_structure'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseowner',
            name='display',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseowner',
            name='display_nr',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
