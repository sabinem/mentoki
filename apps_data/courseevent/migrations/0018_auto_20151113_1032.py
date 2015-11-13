# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0017_courseeventparticipation_participation_type'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='courseevent',
            unique_together=set([('title', 'start_date')]),
        ),
    ]
