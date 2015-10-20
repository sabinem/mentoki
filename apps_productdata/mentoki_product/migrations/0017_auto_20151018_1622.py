# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0016_auto_20151018_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseproduct',
            name='product_type',
            field=models.CharField(default='courseevent', max_length=12, verbose_name='Produktart', choices=[('courseevent', 'Kursteilnahme'), ('part', 'Teilabschnitt einer Kurses'), ('addon', 'anderes Produkt'), ('selflearn', 'Material und Forum-Zugang')]),
        ),
    ]
