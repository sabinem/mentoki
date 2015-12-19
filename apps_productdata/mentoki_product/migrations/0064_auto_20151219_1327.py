# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0063_auto_20151219_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseproduct',
            name='description',
            field=froala_editor.fields.FroalaField(blank=True),
        ),
    ]
