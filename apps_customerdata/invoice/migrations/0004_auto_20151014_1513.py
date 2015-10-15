# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_invoice_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='title',
            field=models.CharField(default='c', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
