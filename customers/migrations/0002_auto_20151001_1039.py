# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(default='de', max_length=100, verbose_name='Land'),
        ),
        migrations.AddField(
            model_name='customer',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='house_nr',
            field=models.CharField(default=1, max_length=100, verbose_name='Hausnummer'),
        ),
        migrations.AddField(
            model_name='customer',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='street',
            field=models.CharField(default='x', max_length=100, verbose_name='Strasse'),
        ),
        migrations.AddField(
            model_name='customer',
            name='town',
            field=models.CharField(default='x', max_length=100, verbose_name='Stadt'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.CharField(unique=True, max_length=36, verbose_name='Kunden-Nr.'),
        ),
    ]
