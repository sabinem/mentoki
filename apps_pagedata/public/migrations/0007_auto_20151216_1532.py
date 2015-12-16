# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0006_staticpublicpages_is_ready'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpublicpages',
            name='is_ready',
            field=models.BooleanField(default=False, verbose_name='fertig'),
        ),
    ]
