# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20151029_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='initial', max_length=12, choices=[('initial', 'aufgenommen'), ('paid', 'bezahlt'), ('failed', 'Zahlung fehlgeschlagen'), ('error', 'Zahlungsfehler'), ('canceled', 'storniert'), ('refunded', 'zur\xfcckerstattet')]),
        ),
    ]
