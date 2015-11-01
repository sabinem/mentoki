# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20151029_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='braintree_error_code',
            field=models.CharField(max_length=6, blank=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='braintree_error_details',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
