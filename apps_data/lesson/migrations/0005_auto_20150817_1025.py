# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_auto_20150817_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlesson',
            name='publish_status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='published'),
        ),
        migrations.AddField(
            model_name='classlesson',
            name='published',
            field=models.BooleanField(default=False, verbose_name='ver\xf6ffentlichen', editable=False),
        ),
    ]
