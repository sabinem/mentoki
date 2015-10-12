# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0007_auto_20151001_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseeventproduct',
            old_name='netto',
            new_name='brutto',
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='name',
            field=models.CharField(default='Kurs-Teilnahme', max_length=200),
        ),
    ]
