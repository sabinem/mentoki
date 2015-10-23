# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0011_auto_20151006_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simpleproduct',
            name='event_type',
        ),
    ]
