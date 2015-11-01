# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0034_auto_20151101_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproduct',
            name='product_type',
            field=models.ForeignKey(verbose_name='Produktart', blank=True, to='mentoki_product.ProductType', null=True),
        ),
    ]
