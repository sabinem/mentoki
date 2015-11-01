# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0016_auto_20150929_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseeventparticipation',
            name='participation_type',
            field=models.CharField(default=b'preview', max_length=10, choices=[(b'preview', 'Feedbackgeber'), (b'full', 'komplett'), (b'part', 'Teile gebucht')]),
        ),
    ]
