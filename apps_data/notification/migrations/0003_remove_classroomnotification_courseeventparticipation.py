# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20160110_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroomnotification',
            name='courseeventparticipation',
        ),
    ]
