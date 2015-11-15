# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_checkout_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='checkout_product_slug',
        ),
        migrations.AddField(
            model_name='user',
            name='checkout_product_pk',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
