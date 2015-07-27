# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0013_auto_20150724_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroommenuitem',
            name='item_type',
            field=models.CharField(max_length=15, choices=[('forum', 'forum'), ('lesson', 'lesson or lesson block'), ('anouncements', 'announcements'), ('homework', 'homework'), ('last_posts', 'latest forum posts'), ('private', 'students private place')]),
        ),
    ]
