# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_products', '0003_courseeventproduct_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseeventproduct',
            name='format_card',
            field=models.CharField(max_length=250, verbose_name='Kursformart kurz', blank=True),
        ),
    ]
