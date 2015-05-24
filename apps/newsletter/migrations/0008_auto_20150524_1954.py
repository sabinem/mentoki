# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_auto_20150517_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='content',
            field=django_markdown.models.MarkdownField(verbose_name='Text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='excerpt',
            field=models.TextField(verbose_name='Abstrakt'),
            preserve_default=True,
        ),
    ]
