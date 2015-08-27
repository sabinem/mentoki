# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0008_auto_20150825_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='classlesson',
            field=models.ForeignKey(default=1, verbose_name='Bezug auf einen Lernabschnitt?', to='lesson.ClassLesson'),
            preserve_default=False,
        ),
    ]
