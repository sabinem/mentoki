# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_auto_20151022_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporder',
            name='participant_username',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
    ]
