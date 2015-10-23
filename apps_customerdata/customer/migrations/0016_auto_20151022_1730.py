# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_auto_20151022_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporder',
            name='participant_email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email des Teilnehmers', blank=True),
        ),
        migrations.AlterField(
            model_name='temporder',
            name='participant_username',
            field=models.CharField(default='x', max_length=40, blank=True),
        ),
    ]
