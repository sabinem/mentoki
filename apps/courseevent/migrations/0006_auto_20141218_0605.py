# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0005_auto_20141215_0603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseeventunitpublish',
            name='created',
        ),
        migrations.RemoveField(
            model_name='courseeventunitpublish',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='courseeventunitpublish',
            name='published',
        ),
        migrations.AlterField(
            model_name='courseeventunitpublish',
            name='published_at_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
