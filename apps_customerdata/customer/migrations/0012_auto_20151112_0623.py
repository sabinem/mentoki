# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_auto_20151111_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='braintree_error_message',
            field=models.TextField(max_length=250, verbose_name='aus braintree Fehlernachricht: besetzt im Fehlerfall ', blank=True),
        ),
    ]
