# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0007_auto_20151001_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorsprofile',
            name='course_short',
            field=models.CharField(max_length=250, verbose_name='Rolle bei Mentoki', blank=True),
        ),
        migrations.AlterField(
            model_name='mentorsprofile',
            name='at_mentoki',
            field=models.CharField(max_length=250, verbose_name='Rolle bei Mentoki', blank=True),
        ),
        migrations.AlterField(
            model_name='mentorsprofile',
            name='special_power',
            field=models.CharField(max_length=250, verbose_name='Spezielle Eigenschaft', blank=True),
        ),
    ]
