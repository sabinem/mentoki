# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0035_courseproduct_product_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseproduct',
            options={'verbose_name': 'Kursprodukt', 'verbose_name_plural': 'Kursprodukte'},
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='invoice_descriptor',
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='specialoffer',
            name='courseevent',
        ),
        migrations.RemoveField(
            model_name='specialoffer',
            name='courseproduct',
        ),
        migrations.RemoveField(
            model_name='specialoffer',
            name='reach',
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='offerreach',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='ProductType',
        ),
    ]
