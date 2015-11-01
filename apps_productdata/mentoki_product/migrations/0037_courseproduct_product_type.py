# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0036_auto_20151029_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproduct',
            name='product_type',
            field=models.ForeignKey(default=1, verbose_name='Produktart', to='mentoki_product.ProductType'),
            preserve_default=False,
        ),
    ]
