# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_is_female'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='checkout_product_slug',
            field=models.SlugField(blank=True),
        ),
    ]
