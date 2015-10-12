# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('textchunks', '0002_auto_20151012_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicTextChunks',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('pagecode', models.CharField(max_length=10, serialize=False, verbose_name='Code', primary_key=True)),
                ('text', froala_editor.fields.FroalaField(verbose_name='text')),
                ('title', models.CharField(max_length=200, verbose_name='Titel')),
                ('description', models.CharField(max_length=250, verbose_name='description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='GeneralTextChunks',
        ),
    ]
