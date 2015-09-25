# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0012_auto_20150924_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentswork',
            name='republished',
        ),
        migrations.AlterField(
            model_name='studentswork',
            name='republished_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='publish_count'),
        ),
    ]
