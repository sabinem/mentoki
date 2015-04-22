# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0025_courseunit_unit_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecomment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursecomment',
            name='user',
        ),
        migrations.DeleteModel(
            name='CourseComment',
        ),
    ]
