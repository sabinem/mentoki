# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0010_auto_20151115_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorsprofile',
            name='course_short',
            field=models.CharField(max_length=250, verbose_name='Kurzbeschreibung', blank=True),
        ),
    ]
