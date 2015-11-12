# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20151110_1249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='error_details',
            new_name='braintree_error_details',
        ),
        migrations.AddField(
            model_name='transaction',
            name='braintree_error_message',
            field=models.TextField(default='x', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='braintree_processor_response_code',
            field=models.TextField(default='x', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='braintree_processor_response_text',
            field=models.TextField(default='x', max_length=250),
            preserve_default=False,
        ),
    ]
