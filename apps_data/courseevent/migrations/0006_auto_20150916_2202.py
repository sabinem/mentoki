# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0005_auto_20150916_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='has_published_decendants',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='hidden',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='hidden_status_changed',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='publish_status_changed',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='published',
        ),
    ]
