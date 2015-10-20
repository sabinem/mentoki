# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0015_auto_20151018_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroup',
            name='conditions',
            field=froala_editor.fields.FroalaField(default='x'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='slug',
            field=models.SlugField(default='x'),
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='title',
            field=models.CharField(default='x', max_length=100),
        ),
    ]
