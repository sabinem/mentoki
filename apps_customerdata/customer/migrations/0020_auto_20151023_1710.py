# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0019_auto_20151023_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='currency',
            field=models.CharField(default=b'EUR', max_length=3, choices=[(b'EUR', 'Euro'), (b'CHF', 'Schweizer Franken')]),
        ),
        migrations.AddField(
            model_name='order',
            name='income',
            field=models.DecimalField(default=0, verbose_name='amount', max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='failedtransaction',
            name='currency',
            field=models.CharField(default=b'EUR', max_length=3, choices=[(b'EUR', 'Euro'), (b'CHF', 'Schweizer Franken')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='paid', max_length=12, choices=[('fix', 'Nicht mehr erstattbar'), ('paid', 'bezahlt'), ('canceled', 'storniert'), ('refunded', 'zur\xfcckerstattet')]),
        ),
        migrations.AlterField(
            model_name='successfultransaction',
            name='currency',
            field=models.CharField(default=b'EUR', max_length=3, choices=[(b'EUR', 'Euro'), (b'CHF', 'Schweizer Franken')]),
        ),
    ]
