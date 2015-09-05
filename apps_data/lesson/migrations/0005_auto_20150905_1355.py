# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_auto_20150831_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlesson',
            name='due_date',
            field=models.DateField(null=True, verbose_name='Abgabedatum', blank=True),
        ),
        migrations.AddField(
            model_name='classlesson',
            name='extra_text',
            field=models.TextField(help_text='Anhang zu Aufgaben', verbose_name='Anhang Aufgabe', blank=True),
        ),
        migrations.AddField(
            model_name='classlesson',
            name='is_homework',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lesson',
            name='is_homework',
            field=models.BooleanField(default=False),
        ),
    ]
