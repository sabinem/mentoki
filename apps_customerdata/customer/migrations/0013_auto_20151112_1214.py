# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_auto_20151112_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='braintree_error_message',
            field=models.CharField(max_length=250, verbose_name='aus braintree Fehlernachricht: besetzt im Fehlerfall ', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='braintree_processor_response_code',
            field=models.CharField(max_length=4, verbose_name='Banken Processor Code: besetzt im Fehlerfall ', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='braintree_processor_response_text',
            field=models.CharField(max_length=250, verbose_name='Banken Processor Text: besetzt im Fehlerfall ', blank=True),
        ),
    ]
