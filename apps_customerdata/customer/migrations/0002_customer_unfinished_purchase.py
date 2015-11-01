# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0033_auto_20151023_2118'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='unfinished_purchase',
            field=models.ForeignKey(blank=True, to='mentoki_product.CourseProduct', null=True),
        ),
    ]
