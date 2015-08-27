# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0004_auto_20150827_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='price',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True),
        ),
    ]
