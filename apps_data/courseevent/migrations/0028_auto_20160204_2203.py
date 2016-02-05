# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0027_auto_20160204_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroommenuitem',
            name='classlesson',
            field=models.ForeignKey(related_name='lesson', on_delete=django.db.models.deletion.PROTECT, blank=True, to='lesson.ClassLesson', null=True),
        ),
    ]
