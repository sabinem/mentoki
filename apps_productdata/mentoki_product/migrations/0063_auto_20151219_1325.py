# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0062_auto_20151216_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseproductsubgroup',
            name='description',
            field=froala_editor.fields.FroalaField(blank=True),
        ),
    ]
