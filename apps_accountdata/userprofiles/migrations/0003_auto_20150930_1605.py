# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20150930_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorsprofile',
            name='at_mentoki',
            field=models.TextField(verbose_name='Rolle bei Mentoki', blank=True),
        ),
        migrations.AddField(
            model_name='mentorsprofile',
            name='special_power',
            field=models.TextField(verbose_name='Spezielle Eigenschaft', blank=True),
        ),
    ]
