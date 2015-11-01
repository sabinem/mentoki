# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20151029_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='braintree_error_code',
        ),
    ]
