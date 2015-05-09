# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0007_courseevent_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseeventparticipation',
            name='url',
            field=models.URLField(default=b'x', blank=True),
            preserve_default=True,
        ),
    ]
