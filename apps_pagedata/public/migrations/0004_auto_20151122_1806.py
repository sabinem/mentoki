# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_auto_20151120_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageSEO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('meta_title', models.CharField(max_length=250, verbose_name='Meta Titel')),
                ('meta_description', models.CharField(max_length=250, verbose_name='Meta Description')),
                ('meta_keywords', models.CharField(max_length=250, verbose_name='Meta Keywords')),
                ('include_in_sitemap', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='staticpublicpages',
            name='page_seo',
            field=models.ForeignKey(blank=True, to='public.PageSEO', null=True),
        ),
    ]
