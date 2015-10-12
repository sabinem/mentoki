# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseeventproduct',
            name='in_one_sentence',
            field=models.CharField(help_text='beschreibe den Kurs in einem Satz', max_length=250, verbose_name='in einem Satz'),
        ),
    ]
