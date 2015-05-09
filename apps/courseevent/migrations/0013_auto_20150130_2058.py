# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0012_auto_20150105_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseeventparticipation',
            name='courseevent',
        ),
        migrations.RemoveField(
            model_name='courseeventparticipation',
            name='user',
        ),
        migrations.DeleteModel(
            name='CourseEventParticipation',
        ),
        migrations.RemoveField(
            model_name='participantpage',
            name='courseevent',
        ),
        migrations.RemoveField(
            model_name='participantpage',
            name='user',
        ),
        migrations.DeleteModel(
            name='ParticipantPage',
        ),
    ]
