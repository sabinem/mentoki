# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_course_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursematerialunit',
            name='excerpt',
            field=models.TextField(default=b'x'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseunit',
            name='excerpt',
            field=models.TextField(default=b'x'),
            preserve_default=True,
        ),
    ]
