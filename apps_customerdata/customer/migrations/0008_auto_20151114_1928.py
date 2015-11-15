# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_order_valid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='nr_part_paid',
            new_name='nr_parts_paid',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='valid',
            new_name='started_to_pay',
        ),
        migrations.AddField(
            model_name='order',
            name='amount_outstanding',
            field=models.DecimalField(default=0, verbose_name='Betrag', max_digits=20, decimal_places=4),
        ),
        migrations.AddField(
            model_name='order',
            name='fully_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='pay_in_parts',
            field=models.BooleanField(default=False),
        ),
    ]
