# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0010_auto_20150724_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='item_type',
            field=models.CharField(max_length=15, choices=[('forum', 'forum'), ('lesson', 'lesson or lesson block'), ('anouncements', 'announcements'), ('homework', 'homework'), ('last_posts', 'latest forum posts')]),
        ),
    ]
