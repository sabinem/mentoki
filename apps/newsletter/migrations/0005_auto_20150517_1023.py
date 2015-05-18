# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20150517_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='text_left',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='text_right',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='content',
            field=models.TextField(default='x', verbose_name='Inhalt'),
            preserve_default=True,
        ),
    ]
