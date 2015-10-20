# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0005_auto_20151001_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseeventproduct',
            old_name='price',
            new_name='netto',
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='agb',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='provision',
            field=models.DecimalField(null=True, verbose_name='Preis', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='tax',
            field=models.DecimalField(null=True, verbose_name='Preis', max_digits=12, decimal_places=2, blank=True),
        ),
    ]
