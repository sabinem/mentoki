# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_checkout_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='checkout_product_slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
