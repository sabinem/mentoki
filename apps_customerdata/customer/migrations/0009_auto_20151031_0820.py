# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20151030_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='error_code',
            field=models.CharField(default=b'', max_length=12, blank=True, choices=[('already_paid', 'Order wurde bereits bezahlt.')]),
        ),
        migrations.AddField(
            model_name='transaction',
            name='error_message',
            field=models.CharField(default=b'', max_length=250, blank=True),
        ),
    ]
