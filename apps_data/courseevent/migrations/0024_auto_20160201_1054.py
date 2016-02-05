# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0023_auto_20160119_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroommenuitem',
            name='menuitemtype',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterUniqueTogether(
            name='courseeventparticipation',
            unique_together=set([('user', 'courseevent')]),
        ),
        migrations.RemoveField(
            model_name='courseeventparticipation',
            name='participation_type',
        ),
    ]
