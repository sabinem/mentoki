# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_transaction_payment_error_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='payment_error_code',
            new_name='error_code',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='braintree_error_details',
            new_name='error_details',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_status',
        ),
        migrations.AddField(
            model_name='transaction',
            name='success',
            field=models.BooleanField(default=False),
        ),
    ]
