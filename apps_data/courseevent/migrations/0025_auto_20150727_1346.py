# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0024_auto_20150726_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroommenuitem',
            name='published_at',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='published_at',
        ),
        migrations.RemoveField(
            model_name='homework',
            name='published_at',
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='published_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='published'),
        ),
        migrations.AddField(
            model_name='forum',
            name='publish_status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='published'),
        ),
        migrations.AddField(
            model_name='homework',
            name='publish_status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='published'),
        ),
    ]
