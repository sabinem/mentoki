# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='text',
        ),
        migrations.RemoveField(
            model_name='subforum',
            name='text',
        ),
        migrations.AddField(
            model_name='forum',
            name='description',
            field=models.TextField(default=b'text', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subforum',
            name='description',
            field=models.TextField(default=b'text', blank=True),
            preserve_default=True,
        ),
    ]
