# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0008_courseevent_participation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='event_type',
            field=models.CharField(default='selflearn', max_length=12, choices=[('guided', 'gef\xfchrter Gruppenkurs'), ('selflearn', 'Selbstlernen'), ('coached', 'with coaching')]),
        ),
    ]
