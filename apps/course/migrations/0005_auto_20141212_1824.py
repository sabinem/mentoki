# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20141211_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='excerpt',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='target_group',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='text',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
