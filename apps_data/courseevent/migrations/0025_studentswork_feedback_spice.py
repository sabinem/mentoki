# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0024_auto_20160201_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentswork',
            name='feedback_spice',
            field=models.IntegerField(default=1),
        ),
    ]
