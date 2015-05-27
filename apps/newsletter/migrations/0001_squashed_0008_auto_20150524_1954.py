# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    replaces = [(b'newsletter', '0001_initial'), (b'newsletter', '0002_auto_20150515_2018'), (b'newsletter', '0003_auto_20150517_0859'), (b'newsletter', '0004_auto_20150517_0905'), (b'newsletter', '0005_auto_20150517_1023'), (b'newsletter', '0006_auto_20150517_1137'), (b'newsletter', '0007_auto_20150517_1544'), (b'newsletter', '0008_auto_20150524_1954')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Thema')),
                ('published', models.BooleanField(default=False, verbose_name='jetzt ver\xf6ffentlichen?')),
                ('published_at_date', models.DateTimeField(null=True, verbose_name='ver\xf6ffentlicht am', blank=True)),
                ('excerpt', models.TextField(default='x', verbose_name='Abstract')),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('content', django_markdown.models.MarkdownField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='tags',
            field=models.ManyToManyField(to=b'newsletter.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='content',
            field=django_markdown.models.MarkdownField(verbose_name='Text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='excerpt',
            field=models.TextField(verbose_name='Abstrakt'),
            preserve_default=True,
        ),
    ]
