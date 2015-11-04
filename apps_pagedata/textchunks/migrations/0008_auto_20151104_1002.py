# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps_pagedata.textchunks.models
import django.utils.timezone
import model_utils.fields
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('textchunks', '0007_auto_20151104_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publictextchunks',
            name='text',
            field=froala_editor.fields.FroalaField(help_text='Dieser Text wird als html chunk auf der Seite integriert. Der pagecode ordnet die Seite zu', verbose_name='Textchunk', blank=True),
        ),
        migrations.AlterField(
            model_name='publictextchunks',
            name='title',
            field=models.CharField(help_text='Der Seitentitel wird ebenfalls benutzt zum Aufbau der  zugeordenten html Seite', max_length=200, verbose_name='Seitentitel', blank=True),
        ),
    ]
