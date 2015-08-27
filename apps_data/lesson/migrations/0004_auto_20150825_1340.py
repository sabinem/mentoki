# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
        ('lesson', '0003_auto_20150824_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classlesson',
            name='materials',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='materials',
        ),
        migrations.AddField(
            model_name='classlesson',
            name='material',
            field=models.ForeignKey(blank=True, to='material.Material', help_text='Material der Lektion', null=True, verbose_name='Kursmaterial'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='material',
            field=models.ForeignKey(blank=True, to='material.Material', help_text='Material der Lektion', null=True, verbose_name='Kursmaterial'),
        ),
    ]
