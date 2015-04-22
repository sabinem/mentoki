# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_classrules_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='published',
            field=models.BooleanField(default=False, verbose_name='jetzt ver\xf6ffentlichen?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='announcement',
            name='published_at_date',
            field=models.DateTimeField(null=True, verbose_name='ver\xf6ffentlicht am', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='announcement',
            name='text',
            field=models.TextField(verbose_name='Text der Ank\xfcndigung: Vorsicht Bilder werden noch nicht mitgeschickt'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Thema'),
            preserve_default=True,
        ),
    ]
