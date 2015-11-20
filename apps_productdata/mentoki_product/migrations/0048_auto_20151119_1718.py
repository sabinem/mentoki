# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0047_auto_20151118_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproduct',
            name='prebook',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='courseproduct',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='courseproduct',
            name='ready_for_sale',
            field=models.BooleanField(default=False),
        ),
    ]
