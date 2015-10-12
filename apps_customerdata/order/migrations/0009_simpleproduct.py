# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0008_auto_20151002_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(default='Kurs-Teilnahme', max_length=200)),
                ('brutto', models.DecimalField(null=True, verbose_name='Preis', max_digits=12, decimal_places=2, blank=True)),
                ('tax', models.DecimalField(null=True, verbose_name='Preis', max_digits=12, decimal_places=2, blank=True)),
            ],
            options={
                'verbose_name': 'Produk',
                'verbose_name_plural': 'Produkte',
            },
        ),
    ]
