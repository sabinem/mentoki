# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0045_auto_20151030_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseproduct',
            old_name='dependencies',
            new_name='dependency',
        ),
    ]
