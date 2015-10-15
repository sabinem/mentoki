# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0013_auto_20151014_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseeventproduct',
            name='price_total',
            field=models.DecimalField(null=True, verbose_name='Verkaufspreis', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='simpleproduct',
            name='price_total',
            field=models.DecimalField(null=True, verbose_name='Verkaufspreis', max_digits=12, decimal_places=2, blank=True),
        ),
    ]
