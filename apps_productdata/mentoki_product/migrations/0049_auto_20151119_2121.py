# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0048_auto_20151119_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroup',
            name='meta_description',
            field=models.CharField(default='x', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='meta_keywords',
            field=models.CharField(default='x', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Keywords'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='meta_title',
            field=models.CharField(default='x', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Titel'),
            preserve_default=False,
        ),
    ]
