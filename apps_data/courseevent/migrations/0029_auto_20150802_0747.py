# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0028_auto_20150731_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentswork',
            name='published',
            field=models.BooleanField(default=False, verbose_name='ver\xf6ffentlichen'),
        ),
    ]
