# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20151106_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='error_code',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='error_message',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='flag_payment_sucess',
        ),
        migrations.AddField(
            model_name='order',
            name='orderstatus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_status',
            field=models.IntegerField(default=0),
        ),
    ]
