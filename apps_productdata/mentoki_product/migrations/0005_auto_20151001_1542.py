# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0004_courseeventproduct_format_card'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseeventproduct',
            old_name='format_card',
            new_name='format',
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='duration',
            field=models.CharField(max_length=250, verbose_name='Kursdauer', blank=True),
        ),
    ]
