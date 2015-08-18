# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0023_auto_20150726_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='forum',
            name='published_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([True]), monitor='published'),
        ),
        migrations.AddField(
            model_name='homework',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='homework',
            name='published_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([True]), monitor='published'),
        ),
    ]
