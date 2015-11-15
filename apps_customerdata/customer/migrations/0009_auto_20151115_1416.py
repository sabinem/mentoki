# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20151114_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount_outstanding',
        ),
        migrations.RemoveField(
            model_name='order',
            name='amount_paid',
        ),
        migrations.AddField(
            model_name='order',
            name='amount_per_payment',
            field=models.DecimalField(default=0, verbose_name='Betrag per Zahlung', max_digits=20, decimal_places=4),
        ),
        migrations.AddField(
            model_name='order',
            name='total_parts',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='success',
            field=models.BooleanField(default=False, verbose_name='erfolgreich?.'),
        ),
    ]
