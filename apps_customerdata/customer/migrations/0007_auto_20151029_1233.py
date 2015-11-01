# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_remove_transaction_braintree_error_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='braintree_error_details',
            field=models.TextField(blank=True),
        ),
    ]
