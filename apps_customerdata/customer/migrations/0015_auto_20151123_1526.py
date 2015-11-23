# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_braintreelog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='braintreelog',
            old_name='transaction',
            new_name='mentoki_transaction',
        ),
        migrations.RenameField(
            model_name='braintreelog',
            old_name='input',
            new_name='transaction_data',
        ),
        migrations.RemoveField(
            model_name='braintreelog',
            name='result',
        ),
    ]
