# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('textchunks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaltextchunks',
            name='description',
            field=models.CharField(max_length=250, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='generaltextchunks',
            name='text',
            field=froala_editor.fields.FroalaField(verbose_name='text'),
        ),
    ]
