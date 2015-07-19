# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0036_auto_20150715_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='owners',
        ),
    ]
