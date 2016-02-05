# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0014_auto_20160128_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlesson',
            name='description',
            field=models.CharField(help_text='diese Beschreibung erscheint nur in den \xdcbersichten', max_length=200, verbose_name='Beschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='classlesson',
            name='nr',
            field=models.IntegerField(default=1, help_text='steuert nur die Anzeigereihenfolge', verbose_name='Nr.'),
        ),
        migrations.AlterField(
            model_name='classlesson',
            name='show_number',
            field=models.BooleanField(default=True, verbose_name='Nr. ist Lektionsnummer'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.CharField(help_text='diese Beschreibung erscheint nur in den \xdcbersichten', max_length=200, verbose_name='Beschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='nr',
            field=models.IntegerField(default=1, help_text='steuert nur die Anzeigereihenfolge', verbose_name='Nr.'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='show_number',
            field=models.BooleanField(default=True, verbose_name='Nr. ist Lektionsnummer'),
        ),
    ]
