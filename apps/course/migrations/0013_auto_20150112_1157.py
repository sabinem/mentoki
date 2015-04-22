# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20150106_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursematerialunit',
            name='required',
        ),
        migrations.RemoveField(
            model_name='coursematerialunit',
            name='url',
        ),
        migrations.RemoveField(
            model_name='coursematerialunit',
            name='urltype',
        ),
        migrations.RemoveField(
            model_name='courseunit',
            name='url',
        ),
        migrations.RemoveField(
            model_name='courseunit',
            name='urltype',
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='document_is_rule',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='document_link',
            field=models.CharField(default=b'', max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='document_type',
            field=models.CharField(default=b'1', max_length=2, choices=[(b'g', b'PDF'), (b'1', b'normal')]),
            preserve_default=True,
        ),
    ]
