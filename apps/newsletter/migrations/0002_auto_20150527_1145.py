# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import autoslug.fields
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_squashed_0008_auto_20150524_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False),
            preserve_default=True,
        ),
    ]
