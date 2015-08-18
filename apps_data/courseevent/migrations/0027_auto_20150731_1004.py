# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0026_auto_20150727_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentswork',
            name='comments',
            field=models.TextField(default='x', verbose_name='Kommentare'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homework',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='studentswork',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='studentswork',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titel f\xfcr Deinen Beitrag'),
        ),
    ]
