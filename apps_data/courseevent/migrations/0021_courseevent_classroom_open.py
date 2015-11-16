# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0020_auto_20151115_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseevent',
            name='classroom_open',
            field=models.BooleanField(default=False),
        ),
    ]
