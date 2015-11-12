# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0045_specialoffer_offerreach'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialoffer',
            name='reach',
        ),
    ]
