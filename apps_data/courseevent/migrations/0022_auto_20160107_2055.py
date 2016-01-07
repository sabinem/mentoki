# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0021_courseevent_classroom_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(to='courseevent.Thread'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='forum',
            field=models.ForeignKey(to='courseevent.Forum'),
        ),
    ]
