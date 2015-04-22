# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0004_auto_20141212_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseeventunitpublish',
            old_name='publish_at_date',
            new_name='published_at_date',
        ),
        migrations.AddField(
            model_name='courseeventunitpublish',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
