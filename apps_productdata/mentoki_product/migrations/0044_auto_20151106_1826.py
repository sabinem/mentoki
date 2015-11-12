# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0043_delete_producttype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseproduct',
            options={'verbose_name': 'Kursprodukt', 'verbose_name_plural': 'Kursprodukte'},
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='oldcurrency',
        ),
    ]
