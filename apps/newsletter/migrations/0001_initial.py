# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django.utils.timezone
import model_utils.fields
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='Thema')),
                ('excerpt', models.TextField(verbose_name='Abstrakt', blank=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('content', django_markdown.models.MarkdownField(verbose_name='Text', blank=True)),
                ('published', models.BooleanField(default=False, verbose_name='jetzt ver\xf6ffentlichen?')),
                ('published_at_date', models.DateTimeField(null=True, verbose_name='ver\xf6ffentlicht am', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
