# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0003_auto_20150930_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorsprofile',
            name='at_mentoki',
            field=models.CharField(max_length=200, verbose_name='Rolle bei Mentoki', blank=True),
        ),
        migrations.AlterField(
            model_name='mentorsprofile',
            name='special_power',
            field=models.CharField(max_length=200, verbose_name='Spezielle Eigenschaft', blank=True),
        ),
    ]
