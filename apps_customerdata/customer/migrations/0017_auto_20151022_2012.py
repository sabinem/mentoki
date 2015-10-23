# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_auto_20151022_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporder',
            name='error_code_braintree_customer',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='temporder',
            name='error_code_braintree_transaction',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='temporder',
            name='success',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='temporder',
            name='participant_username',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
