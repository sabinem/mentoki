# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20150515_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='slug',
            field=models.SlugField(default='x', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='modified',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
