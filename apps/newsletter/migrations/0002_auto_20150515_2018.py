# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='text',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='excerpt',
            field=models.TextField(default='x', verbose_name='Abstract'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsletter',
            name='text_left',
            field=models.TextField(default='x', verbose_name='Linke Spalte'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsletter',
            name='text_right',
            field=models.TextField(default='x', verbose_name='Rechte Spalte'),
            preserve_default=True,
        ),
    ]
