# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='prerequisites',
            field=models.TextField(default=b'text'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='target_group',
            field=models.TextField(default=b'text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='excerpt',
            field=models.TextField(default=b'text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='text',
            field=models.TextField(default=b'text'),
            preserve_default=True,
        ),
    ]
