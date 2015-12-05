# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0056_courseproductgroupfield_display_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseproductgroup',
            name='in_one_sentence',
            field=models.TextField(help_text='Beschreibe den Kurs in einem Satz', verbose_name='in einem Satz'),
        ),
    ]
