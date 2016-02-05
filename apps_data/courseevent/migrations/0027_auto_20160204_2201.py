# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0026_auto_20160204_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroommenuitem',
            name='classlesson',
            field=models.ForeignKey(related_name='lesson', blank=True, to='lesson.ClassLesson', null=True),
        ),
    ]
