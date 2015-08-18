# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0027_auto_20150731_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='last_post',
        ),
        migrations.AlterField(
            model_name='studentswork',
            name='comments',
            field=models.TextField(verbose_name='Kommentare', blank=True),
        ),
    ]
