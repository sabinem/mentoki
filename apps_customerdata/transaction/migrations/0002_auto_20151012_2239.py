# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='braintree_customer_id',
            field=models.CharField(default=b'x', max_length=36, verbose_name=b'braintree_customer_id'),
        ),
    ]
