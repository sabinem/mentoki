# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20150527_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='content',
            field=django_markdown.models.MarkdownField(verbose_name='Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='excerpt',
            field=models.TextField(verbose_name='Abstrakt', blank=True),
            preserve_default=True,
        ),
    ]
