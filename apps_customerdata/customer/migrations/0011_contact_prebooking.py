# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0047_auto_20151118_1334'),
        ('customer', '0010_order_last_transaction_had_success'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('first_name', models.CharField(max_length=40, blank=True)),
                ('last_name', models.CharField(max_length=40, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('contact_reason', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Kontakte',
                'verbose_name_plural': 'Kontakte',
            },
        ),
        migrations.CreateModel(
            name='Prebooking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('first_name', models.CharField(max_length=40, blank=True)),
                ('last_name', models.CharField(max_length=40, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('interested_in_learning', models.ForeignKey(to='mentoki_product.CourseProductGroup')),
            ],
            options={
                'verbose_name': 'Vorbestellung',
                'verbose_name_plural': 'Vorbestellungen',
            },
        ),
    ]
