# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_auto_20150517_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='content',
            field=django_markdown.models.MarkdownField(),
            preserve_default=True,
        ),
    ]
