# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0040_auto_20150814_0703'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumMenuItem',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('courseevent.classroommenuitem',),
        ),
        migrations.AddField(
            model_name='courseeventparticipation',
            name='hidden_status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='hidden'),
        ),
        migrations.AddField(
            model_name='forum',
            name='hidden_status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='hidden'),
        ),
        migrations.AddField(
            model_name='homework',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='versteckt'),
        ),
        migrations.AddField(
            model_name='homework',
            name='hidden_status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='hidden'),
        ),
        migrations.AddField(
            model_name='post',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='versteckt'),
        ),
        migrations.AddField(
            model_name='post',
            name='hidden_status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='hidden'),
        ),
        migrations.AddField(
            model_name='thread',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='versteckt'),
        ),
        migrations.AddField(
            model_name='thread',
            name='hidden_status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='hidden'),
        ),
    ]
