# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0010_auto_20151006_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseeventproduct',
            name='mwst',
            field=models.DecimalField(null=True, verbose_name='Mehrwertsteuer', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='courseeventproduct',
            name='netto_vk',
            field=models.DecimalField(null=True, verbose_name='Netto Preis', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='simpleproduct',
            name='mwst',
            field=models.DecimalField(null=True, verbose_name='Mehrwertsteuer', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='simpleproduct',
            name='netto_vk',
            field=models.DecimalField(null=True, verbose_name='Netto Preis', max_digits=12, decimal_places=2, blank=True),
        ),
    ]
