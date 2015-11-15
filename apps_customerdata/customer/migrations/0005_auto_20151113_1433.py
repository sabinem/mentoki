# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_order_currency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='amount',
            new_name='amount_paid',
        ),
        migrations.AddField(
            model_name='order',
            name='valid_until',
            field=models.DateField(null=True, verbose_name='g\xfcltig bis', blank=True),
        ),
    ]
